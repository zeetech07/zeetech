from .models import Course,Footer

def course_context(request):
    footer_data = Footer.objects.first()
    # print(footer_data)
    all_course=Course.objects.all()
    # print(all_course)
    
    return {
        'footer_data':footer_data,
        'all_course':all_course,
    }
