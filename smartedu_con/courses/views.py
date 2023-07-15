from django.shortcuts import render,get_object_or_404
from .models import Course, Category, Tag
# Create your views here.


def course_list(req, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()
    if category_slug != None:
        category_page = get_object_or_404(
             #varsa obje göster yoksa 404 at
             Category,
             slug=category_slug
        )
        courses=Course.objects.filter(available=True,category=category_page)
    elif tag_slug != None:
        tag_page = get_object_or_404(
             #varsa obje göster yoksa 404 at
             Tag,
             slug=tag_slug
        )
        courses=Course.objects.filter(available=True,tags=tag_page)
    else:
        courses = Course.objects.all().filter(available=True).order_by('-date')
    context = {"courses": courses, "categories": categories, "tags": tags}
    return render(req, "courses.html", context)    
  

def course_detail(req, category_slug, course_id):
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    context = {
        "course": course,
    }
    return render(req, "course.html", context)
def search(req):
    courses=Course.objects.filter(name__contains=req.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {"courses": courses, "categories": categories, "tags": tags}
    return render(req,'courses.html',context)
# def category_list(req, category_slug):
#     #!category__slug course üzerinden doğrudan parent category ye git anlamına gelmektedir
#     courses = Course.objects.all().filter(category__slug=category_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {"courses": courses, "categories": categories, "tags": tags}
#     return render(req, "courses.html", context)


# def tag_lists(req, tag_slug):
#     courses = Course.objects.all().filter(tags__slug=tag_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {"courses": courses, "categories": categories, "tags": tags}
#     return render(req, "courses.html", context)


# def tag_lists(req, tag_slug):
#     courses = Course.objects.all().filter(tags__slug=tag_slug)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {"courses": courses, "categories": categories, "tags": tags}
#     return render(req, "courses.html", context)


# def course_list(req):
#     courses = Course.objects.all().order_by("-date")
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {"courses": courses, "categories": categories, "tags": tags}
#     return render(req, "courses.html", context)