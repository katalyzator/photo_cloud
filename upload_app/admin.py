from django.contrib import admin
from .models import *


# Register your models here.

class FolderImageAdmin(admin.ModelAdmin):
    pass


class FolderImageInline(admin.StackedInline):
    model = FolderImage
    max_num = 10
    extra = 0


class SubFolderImageInline(admin.ModelAdmin):
    inlines = [FolderImageInline, ]


admin.site.register(FolderImage, FolderImageAdmin)
admin.site.register(SubFolder, SubFolderImageInline)
admin.site.register(Folder)
