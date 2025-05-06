from django.shortcuts import render
from .models import Course,Topic,Technology,Placement, Student,Course,Instructor
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
import json
from cities_light.models import City
from .models import CarrierOpportunities,Contact
from academy.models import Contact# Sirf models ko import karo
from academy.forms import ContactForm
from broucher.models import Broucher
from django.http import FileResponse, Http404
from .models import CompanyTieUps
import re
from cities_light.models import SubRegion
from django.contrib.messages import constants as message_constants


 # Form ko forms.py se import karo



# Create your views here.

def courses(request):
    all_courses=Course.objects.all()
    # print(all_courses)
    
    for i in all_courses:
        names=i.course_name
        # print(names)
    
    context={
        'all_courses':all_courses
    }
    return render(request,'home/courses.html',context)

# from django.shortcuts import render
# from academy.models import Course
# Create your views he

def detail(request,id):
    course=Course.objects.filter(id=id).first()
    technologies = course.technologies.all() if course else [] 
    # print(f"ye course ka naa leke aayega",course,technologies)
    
    # Technologies=Topic.objects.all()
    tech_with_topics=[]
    for tech in technologies:
        topics=tech.topics.all()
        tech_with_topics.append({'tech':tech,'topics':topics})
        # print(f"yeh mere saare topics hai ................",tech_with_topics)
        
        
    context={
        'course':course,
        'tech_with_topics':tech_with_topics,
    }
    
    return render(request,'home/detail.html',context)


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            # Email should end with @gmail.com
            if not cd['email'].endswith('@gmail.com'):
                messages.error(request, "Please use a valid Gmail address (must end with @gmail.com).", extra_tags='popup')
                return redirect('home')

            # Check for duplicate email
            if Contact.objects.filter(email=cd['email']).exists():
                messages.error(request, "This email has already been used.", extra_tags='popup')
                return redirect('home')

            # Check for duplicate mobile number
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











from django.shortcuts import render, redirect
from django.contrib import messages
import re
from .models import Contact, Course, CompanyTieUps, Instructor
import json


def home(request):
    courses = Course.objects.all()
    course=Course.objects.filter(course_name__in=["Data Science","Python Full Stack","Digital Marketing"]).prefetch_related('technologies')
    companies = CompanyTieUps.objects.all()
    instructors = Instructor.objects.all()

    # Students data (placement)
    students_data = {
        course.id: [
            {
                "name": f"{student.student.user.first_name} {student.student.user.last_name}",
                "photo": student.student.image.url if student.student.image else "/static/default-avatar.png",
                "company": student.company_tie_up.company_name,
                "package": f"₹{student.packages} LPA",
                "job_role": student.job_role
            }
            for student in course.placement_set.all()
        ]
        for course in courses
    }
    students_json = json.dumps(students_data)

    context = {
        'course':course,
        'students_json': students_json,
        'companies': companies,
        'instructors': instructors,
        'courses': courses,
    }
    
    if request.method == 'POST' and 'contact_submit' in request.POST:
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        mob_no = request.POST.get('mobile')
        email_add = request.POST.get('email')

        errors = []

        # Validation for first name
        if not f_name or not f_name.isalpha():
            errors.append("First name should contain only alphabets.")

        # Validation for last name
        if not l_name or not l_name.isalpha():
            errors.append("Last name should contain only alphabets.")

        # Validation for mobile number
        if not mob_no or not mob_no.isdigit() or len(mob_no) != 10:
            errors.append("Mobile number should be exactly 10 digits.")

        # Validation for email address format (only @gmail.com allowed)
        email_regex = r'^[\w\.-]+@gmail\.com$'
        if not email_add or not re.match(email_regex, email_add):
            errors.append("Enter a valid email address with @gmail.com domain.")

        # Check if mobile number already exists in the database
        if Contact.objects.filter(mobile=mob_no).exists():
            errors.append("This mobile number has already been used.")

        # Check if email address already exists in the database
        if Contact.objects.filter(email=email_add).exists():
            errors.append("This email address has already been used.")

        # If there are any errors, show them and redirect
        if errors:
            for error in errors:
                messages.error(request, error, extra_tags='normal')
            return redirect('home')

    # Save contact if all validations pass
        Contact.objects.create(
                first_name=f_name,
                last_name=l_name,
                mobile=mob_no,
                email=email_add,
            )

            # Show success message
        messages.success(request, "Your message has been sent successfully!", extra_tags='normal')
        return redirect('home')
    return render(request, 'home/home.html', context)


    

def download_datascience_brochure(request):
    try:
        # Pehle Data Science course ko fetch karo
        data_science_course = get_object_or_404(Course, course_name="Data Science")
        
        # Uske brochure ko fetch karo
        brochure = Broucher.objects.get(course=data_science_course)
        
        # Agar brochure mil gaya to file return karo
        return FileResponse(brochure.file.open(), as_attachment=True, filename="DataScience_Brochure.pdf")

    except Broucher.DoesNotExist:
        messages.error(request, "Data Science brochure not found")  # Error message
        return redirect("home")  # Home page pe redirect karega
    
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

        # ✅ Only allow Gmail addresses
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








