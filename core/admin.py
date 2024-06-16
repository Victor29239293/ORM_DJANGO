from django.contrib import admin

from .models import Period,Subject,Teacher,Student,Note, DetailNote


# Register your models here.
admin.site.register(Period)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Note)
admin.site.register(DetailNote)