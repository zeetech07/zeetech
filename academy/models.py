from django.db import models
from cities_light.models import City

# UserReg Model
class UserReg(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('staff', 'Staff'),
    )

    salutation = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"

# Student Model
class Student(models.Model):
    user = models.ForeignKey(UserReg, on_delete=models.CASCADE, limit_choices_to={'role': 'student'}, null=True, blank=True)
    course_enrolled_in = models.ManyToManyField('Course', blank=True)
    admission_no = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(upload_to='student_images/', null=True, blank=True, default='default-avatar.png')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.admission_no}"

# Enrollment Model
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, limit_choices_to={'user__role': 'student'}, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    enrollment_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    course_completion_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('completed', 'Completed'), ('dropout', 'Dropout'), ('placed', 'Placed')], null=True, blank=True)

# Instructor Model
class Instructor(models.Model):
    instructor_name = models.CharField(max_length=100, blank=True, null=True)
    edu_qualification = models.CharField(max_length=100)
    instructor_Exp = models.PositiveIntegerField(default=0)
    designation = models.CharField(max_length=50)
    no_of_student = models.PositiveIntegerField(default=0)
    is_trainer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='instructor_images/')

    def __str__(self):
        return self.instructor_name

# Course Model
class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, unique=True)
    course_desc = models.TextField(max_length=500)
    course_duration = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    banner = models.ImageField(upload_to='course_banners/', blank=True, null=True)  # Added for course-specific banner
    technologies = models.ManyToManyField('Technology', related_name='courses', blank=True)

    def __str__(self):
        return self.course_name

# Technology Model
class Technology(models.Model):
    tech_name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.tech_name if self.tech_name else "Unnamed Technology"

# Topic Model
class Topic(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='topics')
    topic_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.topic_name if self.topic_name else "Unnamed Technology"

# Company Tie-ups Model
class CompanyTieUps(models.Model):
    company_name = models.CharField(max_length=255, null=True, blank=True)
    contact_person = models.CharField(max_length=50, null=True, blank=True)
    contact_email = models.EmailField(unique=True, null=True, blank=True)
    agreement_date = models.DateField(auto_now_add=True, null=True, blank=True)
    placement_date = models.DateField(auto_now=True, null=True, blank=True)
    company_image = models.ImageField(upload_to='company_images/', blank=True, null=True)

    def __str__(self):
        return self.company_name

# Placement Model
class Placement(models.Model):
    student_name = models.CharField(max_length=255, null=True, blank=True)
    student_photo = models.ImageField(upload_to='placement_photos/', null=True, blank=True)
    company_tie_up = models.ForeignKey(CompanyTieUps, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    job_role = models.CharField(max_length=100, blank=True, null=True)
    # packages = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    placement_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.job_role} at {self.company_tie_up.company_name}"

# Carrier Opportunities Model
class CarrierOpportunities(models.Model):
    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'),
        ('1-3 years', '1-3 years'),
        ('3+ years', '3+ years'),
    ]

    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    mob_no = models.CharField(max_length=12)
    email_add = models.EmailField(max_length=255, unique=True)
    qualification = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    city = models.CharField(max_length=50, null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    upload_resume = models.FileField(upload_to='carrier_resumes/', blank=True, null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

# Footer Model
class Footer(models.Model):
    address = models.TextField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    facebook = models.URLField(max_length=3000, blank=True, null=True)
    instagram = models.URLField(max_length=3000, blank=True, null=True)
    whatsapp = models.URLField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return f"Footer - {self.email}"

# Contact Model
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null=True, blank=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Banner Model (for homepage)
class Banner(models.Model):
    image = models.ImageField(upload_to='banner_images/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Order in which images appear in the slideshow")
    is_active = models.BooleanField(default=True, help_text="Active banners will be shown in the slideshow")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Banner {self.id} - Order {self.order}"