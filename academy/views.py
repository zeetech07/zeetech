from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse, FileResponse, Http404
from .models import Course, Topic, Technology, Placement, Student, Instructor, CompanyTieUps, CarrierOpportunities, Contact, Banner
from .forms import ContactForm
from broucher.models import Broucher
import json
import re
from cities_light.models import SubRegion

def courses(request):
    all_courses = Course.objects.all()
    context = {
        'all_courses': all_courses
    }
    return render(request, 'home/courses.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Course, Technology

def detail(request, id):
    course = get_object_or_404(Course, id=id)
    technologies = course.technologies.all()
    tech_with_topics = [{'tech': tech, 'topics': tech.topics.all()} for tech in technologies]

    context = {
        'course': course,
        'tech_with_topics': tech_with_topics,
    }
    return render(request, 'home/detail.html', context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd['email'].endswith('@gmail.com'):
                messages.error(request, "Please use a valid Gmail address (must end with @gmail.com).", extra_tags='popup')
                return redirect('home')
            if Contact.objects.filter(email=cd['email']).exists():
                messages.error(request, "This email has already been used.", extra_tags='popup')
                return redirect('home')
            if Contact.objects.filter(mobile=cd['mobile']).exists():
                messages.error(request, "This mobile number has already been used.", extra_tags='popup')
                return redirect('home')
            Contact.objects.create(
                first_name=cd['first_name'],
                last_name=cd['last_name'],
                mobile=cd['mobile'],
                email=cd['email'],
                message=cd['message']
            )
            messages.success(request, "Your message has been sent successfully!", extra_tags='popup')
            return redirect('home')
        else:
            messages.error(request, "Please fill the form correctly", extra_tags='popup')
    return redirect('home')

def home(request):
    courses = Course.objects.all()
    # Fetch the first 4 courses or adjust the filter to include 4 specific courses
    course = Course.objects.all()[:4].prefetch_related('technologies')
    companies = CompanyTieUps.objects.all()
    instructors = Instructor.objects.all()
    banners = Banner.objects.filter(is_active=True).order_by('order')

    students_data = {
        course.id: [
            {
                "name": student.student_name,
                "photo": student.student_photo.url if student.student_photo else "/static/default-avatar.png",
                "company": student.company_tie_up.company_name,
                "job_role": student.job_role
            }
            for student in course.placement_set.all()
        ]
        for course in courses
    }
    students_json = json.dumps(students_data)

    context = {
        'course': course,  # This will now contain 4 courses
        'students_json': students_json,
        'companies': companies,
        'instructors': instructors,
        'courses': courses,
        'banners': banners,
    }

    if request.method == 'POST' and 'contact_submit' in request.POST:
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        mob_no = request.POST.get('mobile')
        email_add = request.POST.get('email')

        errors = []
        if not f_name or not f_name.isalpha():
            errors.append("First name should contain only alphabets.")
        if not l_name or not l_name.isalpha():
            errors.append("Last name should contain only alphabets.")
        if not mob_no or not mob_no.isdigit() or len(mob_no) != 10:
            errors.append("Mobile number should be exactly 10 digits.")
        email_regex = r'^[\w\.-]+@gmail\.com$'
        if not email_add or not re.match(email_regex, email_add):
            errors.append("Enter a valid email address with @gmail.com domain.")
        if Contact.objects.filter(mobile=mob_no).exists():
            errors.append("This mobile number has already been used.")
        if Contact.objects.filter(email=email_add).exists():
            errors.append("This email address has already been used.")
        if errors:
            for error in errors:
                messages.error(request, error, extra_tags='normal')
            return redirect('home')

        Contact.objects.create(
            first_name=f_name,
            last_name=l_name,
            mobile=mob_no,
            email=email_add,
        )
        messages.success(request, "Your message has been sent successfully!", extra_tags='normal')
        return redirect('home')

    return render(request, 'home/home.html', context)

def download_datascience_brochure(request):
    try:
        data_science_course = get_object_or_404(Course, course_name="Data Science")
        brochure = Broucher.objects.get(course=data_science_course)
        return FileResponse(brochure.file.open(), as_attachment=True, filename="DataScience_Brochure.pdf")
    except Broucher.DoesNotExist:
        messages.error(request, "Data Science brochure not found")
        return redirect("home")

def experts(request):
    instructors = Instructor.objects.all()
    return render(request, 'home/home.html', {'instructors': instructors})

def carrier(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        mob_no = request.POST.get('mobile')
        email_add = request.POST.get('email')
        qualification = request.POST.get('qualification')
        department = request.POST.get('position')
        city = request.POST.get('city')
        experience = request.POST.get('experience')
        upload_resume = request.FILES.get('resume')

        errors = []
        if not f_name.isalpha():
            errors.append("First name should contain only alphabets.")
        if not l_name.isalpha():
            errors.append("Last name should contain only alphabets.")
        if not mob_no.isdigit() or len(mob_no) != 10:
            errors.append("Mobile number should be exactly 10 digits.")
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email_add):
            errors.append("Enter a valid email address.")
        if not email_add.endswith("@gmail.com"):
            errors.append("Only Gmail addresses are allowed.")
        if errors:
            for error in errors:
                messages.error(request, error, extra_tags='normal')
            return redirect('home')
        if CarrierOpportunities.objects.filter(email_add=email_add).exists():
            messages.error(request, "This email has already been used to apply.")
            return redirect('carrier')
        if CarrierOpportunities.objects.filter(mob_no=mob_no).exists():
            messages.error(request, "This mobile number has already been used to apply.")
            return redirect('carrier')
        CarrierOpportunities.objects.create(
            f_name=f_name,
            l_name=l_name,
            mob_no=mob_no,
            email_add=email_add,
            qualification=qualification,
            department=department,
            city=city,
            experience=experience,
            upload_resume=upload_resume,
        )
        messages.success(request, "Application submitted successfully!", extra_tags='normal')
        return redirect('home')

    return render(request, 'home/career.html')


