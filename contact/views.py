from django.shortcuts import render,redirect
from academy.models import Contact
import re 
from django.contrib import messages


def contactus(request):
    context = {}

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        mobile = request.POST.get('mobile', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('Your-Message', '').strip()

        errors = []

        # === Validations ===
        if not first_name or not first_name.isalpha():
            errors.append("First name should contain only alphabets.")

        if not last_name or not last_name.isalpha():
            errors.append("Last name should contain only alphabets.")

        if not mobile.isdigit() or len(mobile) != 10:
            errors.append("Mobile number must be exactly 10 digits.")
        
        # Check if mobile number already exists in the database
        if Contact.objects.filter(mobile=mobile).exists():
            errors.append("This mobile number is already registered.")
        
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, email):
            errors.append("Invalid email address format. Please use a valid format like 'example@gmail.com'.")
        
        # Check if email already exists in the database
        if Contact.objects.filter(email=email).exists():
            errors.append("This email is already registered.")

        # === If errors, show them ===
        if errors:
            context['errors'] = errors
            return render(request, "contact/contactus.html", context)

        # === Save if no errors ===
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            email=email,
            message=message,
        )
        contact.save()

        context['success'] = "Your message has been submitted successfully!"
        return render(request, "contact/contactus.html", context)

    return render(request, "contact/contactus.html", context)





       


def councelling(request):
    if request.method == "POST":
        mobile = request.POST['mobile']

        # Check if the mobile number already exists in the database
        if Contact.objects.filter(mobile=mobile).exists():
            messages.error(request, "Mobile number already exists.", extra_tags='popup')
            return redirect('councelling')  # redirect is important to prevent resubmission
        
        # If no duplicate mobile number, save the new entry
        councelling = Contact(mobile=mobile)
        councelling.save()

        messages.success(request, "Your form has been submitted successfully!", extra_tags='popup')
        return redirect('councelling')

    return render(request, "contact/councelling.html")



