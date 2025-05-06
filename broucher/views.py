from django.shortcuts import render, get_object_or_404, redirect
from academy.models import Course
from academy.forms import ContactForm
from .models import Broucher
from django.contrib import messages
from django.http import HttpResponse


def broucher(request, id):
    # Course fetch karo
    single_course = get_object_or_404(Course, id=id)

    # Us course ka brochure lao
    broucher = Broucher.objects.filter(course=single_course).first()

    # Agar POST request sirf flag clear karne ke liye aayi hai (via JS)
    if request.method == "POST" and request.POST.get("clear_flag") == "1":
        request.session.pop('download_ready', None)
        return HttpResponse("")

    if request.method == "POST":
        # Form submit hua hai
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # Success message dikhao aur download ke liye flag set karo
            messages.success(request, "Form submitted successfully! Brochure Downloaded Successfully")
            request.session['download_ready'] = True

            # Redirect karo taaki message show ho aur HTML side se download trigger ho
            return redirect('broucher', id=id)

        else:
            # Form valid nahi hai — error message dikhao
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ContactForm()

    return render(request, 'home/broucher.html', {
        'single_course': single_course,
        'form': form,
        'broucher': broucher,
    })

























