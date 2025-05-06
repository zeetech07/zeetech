from django import forms
from academy.models import Contact,CarrierOpportunities
import re  

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'mobile', 'email','message']
        
        def clean_first_name(self):
            first_name = self.cleaned_data.get('first_name')
            if not first_name:
                raise forms.ValidationError("First name is required.")
            if len(first_name) < 2:
                raise forms.ValidationError("First name must be at least 2 characters long.")
            if not re.match("^[a-zA-Z]*$", first_name):
                raise forms.ValidationError("First name can only contain letters.")
            return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("Last name is required.")
        if len(last_name) < 2:
            raise forms.ValidationError("Last name must be at least 2 characters long.")
        if not re.match("^[a-zA-Z]*$", last_name):
            raise forms.ValidationError("Last name can only contain letters.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        # Basic email regex for validation
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        
        if Contact.objects.filter(email=email).exists():
           raise forms.ValidationError("This email is already registered.")
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not mobile:
            raise forms.ValidationError("Mobile number is required.")
        if not mobile.isdigit() or len(mobile) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits.")
        if Contact.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError("This mobile number is already registered.")
        return mobile































# from django import forms
# from academy.models import Contact,CarrierOpportunities
# import re  

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['first_name', 'last_name', 'mobile', 'email','message']
        
#         def clean_first_name(self):
#             first_name = self.cleaned_data.get('first_name')
#             if not first_name:
#                 raise forms.ValidationError("First name is required.")
#             if len(first_name) < 2:
#                 raise forms.ValidationError("First name must be at least 2 characters long.")
#             if not re.match("^[a-zA-Z]*$", first_name):
#                 raise forms.ValidationError("First name can only contain letters.")
#             return first_name

#     def clean_last_name(self):
#         last_name = self.cleaned_data.get('last_name')
#         if not last_name:
#             raise forms.ValidationError("Last name is required.")
#         if len(last_name) < 2:
#             raise forms.ValidationError("Last name must be at least 2 characters long.")
#         if not re.match("^[a-zA-Z]*$", last_name):
#             raise forms.ValidationError("Last name can only contain letters.")
#         return last_name

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not email:
#             raise forms.ValidationError("Email is required.")
        
#         if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
#             raise forms.ValidationError("Enter a valid email address.")
#         return email

#     def clean_mobile(self):
#         mobile = self.cleaned_data.get('mobile')
#         if not mobile:
#             raise forms.ValidationError("Mobile number is required.")
#         if not mobile.isdigit() or len(mobile) != 10:
#             raise forms.ValidationError("Phone number must be exactly 10 digits.")
#         return mobile
        
        
        
        
        
        
        
     
        
