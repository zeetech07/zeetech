from django.contrib import admin
from django.utils.html import format_html
from .models import Instructor, Course, CompanyTieUps, Placement, CarrierOpportunities, Footer, Contact, Technology, Topic, Enrollment, Student, UserReg, Banner

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['instructor_name', 'edu_qualification', 'instructor_Exp', 'designation', 'no_of_student', 'image']

class CompanyTieUpsAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'contact_email', 'agreement_date', 'placement_date']

class PlacementAdmin(admin.ModelAdmin):
    list_display = ['company_tie_up', 'job_role', 'placement_date']

class CarrierOpportunitiesAdmin(admin.ModelAdmin):
    list_display = ['f_name', 'l_name', 'mob_no', 'email_add', 'qualification', 'department', 'city', 'experience', 'upload_resume']

class FooterAdmin(admin.ModelAdmin):
    list_display = ['contact_no', 'email']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'mobile', 'message']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'course_name', 'course_desc', 'course_duration', 'image', 'banner']  # Added banner
    filter_horizontal = ('technologies',)

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['tech_name']

class TopicAdmin(admin.ModelAdmin):
    list_display = ['technology', 'topic_name']

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrollment_date', 'course_completion_date', 'status']

@admin.register(UserReg)
class UserRegAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'contact')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'admission_no', 'get_courses', 'get_image')
    search_fields = ('user__first_name', 'user__last_name', 'admission_no')
    filter_horizontal = ('course_enrolled_in',)

    def get_courses(self, obj):
        return ", ".join([course.course_name for course in obj.course_enrolled_in.all()])
    
    get_courses.short_description = "Courses Enrolled"

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"
    get_image.short_description = "Profile Photo"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_display_links = ['id']

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CompanyTieUps, CompanyTieUpsAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(CarrierOpportunities, CarrierOpportunitiesAdmin)
admin.site.register(Footer, FooterAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)