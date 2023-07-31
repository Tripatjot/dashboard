from django.db import models

# Role Model
class Role(models.Model):
    ROLE_CHOICES = [
        ('1', 'SA'),
        ('2', 'CTM'),
        ('3', 'Fellow'),
    ]

    STATUS_CHOICES = [
        (0, 'Inactive'),
        (1, 'Active'),
    ]

    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

# User Model
class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10)
    email_id = models.EmailField()
    emp_code = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

# class AdminUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE) # Email
#     password = models.CharField(max_length=1024)