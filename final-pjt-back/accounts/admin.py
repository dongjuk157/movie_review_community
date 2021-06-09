from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from movies.models import Movie
from review.models import Review,Comment

admin.site.register(User, UserAdmin)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Comment)
