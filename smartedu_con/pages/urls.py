from django.urls import path
# from . import views
from pages.views import AboutView,IndexView,ContactView


urlpatterns = [
     path('',IndexView.as_view(),name="index"),
     path('about',AboutView.as_view(),name="about"),
     path('about',AboutView.as_view(),name="about"),
     path('contact',ContactView.as_view(),name="contact"),
     
    #  path('test/',views.arin)

    # path('root yönü',dönecek istek,opsiyonel(kısayol ismi))

]
