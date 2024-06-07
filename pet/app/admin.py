from django.contrib import admin

from .models import CustomUser, Passport, Sitter, Pet, Owner, Admin, Keep, Feedback, HomeImages, SitterFeedback

admin.site.register(
    [
        CustomUser,
        Passport,
        Sitter,
        Pet,
        Owner,
        Admin,
        Keep,
        Feedback,
        HomeImages,
        SitterFeedback,
    ]
)
