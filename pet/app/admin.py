from django.contrib import admin

from .models import User, Passport, Sitter, Pet, Owner, Admin, Keep, Feedback

admin.site.register(
    [
        User,
        Passport,
        Sitter,
        Pet,
        Owner,
        Admin,
        Keep,
        Feedback
    ]
)
