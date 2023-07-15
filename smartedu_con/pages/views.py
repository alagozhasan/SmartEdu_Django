# ilgili istekleri burdaki functs ile karşılarım
from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Course
from django.views.generic.edit import FormView
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


# def index(req):
#     # return HttpResponse("<h1>INDEX SAYFASI</h1>")
#     return render(req, "index.html")


# # render(parametre olarak gelen requeste karşılık,templates klasörü içinde bulunan index.hmtl i göster)
# #! templates klasörü manuel olarak uygulamanın içine templates isimli kallasör olarak açılır
# # bunun yerine tek bir template kullanımı da olabilir,projenin büyüklüğüne göre tek bir template klasör yeterli olacaktır
# # çünkü benim her bir uygulamam bu projede ayrı html leri var #! böyle yapacaksam ana dizinde settings.py a bunu bildirmem gerekir
# def about(req):
#     return render(req, "about.html")


# sadece fonkksiyon değil class tabalı view de yazabiliim aşağıda yukarıdaki fonksiyonların class tabanlı halleri mevcut
#! genelde sitatik sayfalrda kullanılr
class AboutView(TemplateView):
    template_name = "about.html"  # kullanacağım html sayfası için


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(available=True).order_by("-date")[:2]
        context["total_course"] = Course.objects.filter(available=True).count()
        return context


class ContactView(SuccessMessageMixin,FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url=reverse_lazy('contact')
    success_message='Mesajını aldık sana dönüş yapacağız.'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
