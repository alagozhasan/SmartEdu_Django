from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Teacher
from courses.models import Course
#class list view bir kursun üyeleri gibi listeleri gösteriirken uygulanan yöntemdir
class TeacherListView(ListView):
    model = Teacher
    template_name = "teachers.html"
    context_object_name='teachers'
    # paginate_by=1 #her bir sayfada kaç eleman sayısı
    # queryset=Teacher.objects.all()
    
    # def get_queryset(self):
    #     return Teacher.objects.all()[:2]
    
class TeacherDetailView(DetailView):
    model=Teacher
    template_name='teacher.html'
    context_object_name='hoca'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(
            available=True,
            teacher=self.kwargs['pk']                                       
                                                   )
        return context
    
    