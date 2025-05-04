from django.contrib import admin

#admin.site.register(Student)
#admin.site.register(Album)

from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["Id","name","roll","city"]