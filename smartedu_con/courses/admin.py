from django.contrib import admin
from .models import Course, Category,Tag


# Register your models here.
# modelimi adminde görmek için
# admin.site.register(
#     Course
# )  # admine import edeceğim modülleri yazdığım kod  kaydedicem neyi => Course
@admin.register(Course)
# admin alanına özellik eklerim
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        # sıralama şekli
        "name",
        "available",
    )
    list_filter = (
        "available",
    )  # filtreleme özelliği virgül tuple olması için eklendii
    search_fields = ("name", "description")  # arama özelliği


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
