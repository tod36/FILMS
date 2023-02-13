from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


class FilmAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    title = models.CharField(max_length=120)
    length = models.CharField(max_length=120)
    year = models.DateField(auto_now_add=True)
    genre = models.TextField()


admin.site.register(Film, FilmAdmin)
