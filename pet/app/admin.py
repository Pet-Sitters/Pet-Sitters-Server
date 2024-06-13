from django.contrib import admin

from .models import CustomUser, Passport, Sitter, Pet, Owner, Admin, ActiveKeep, Feedback, HomeImages, SitterFeedback, \
    NewKeepFrom

admin.site.register(
    [
        CustomUser,
        Passport,
        Sitter,
        Pet,
        Owner,
        Admin,
        ActiveKeep,
        Feedback,
        HomeImages,
        SitterFeedback,
        NewKeepFrom
    ]
)
