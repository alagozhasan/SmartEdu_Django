from django.urls import path
from . import views


urlpatterns = [
     path('',views.index,name="index"),
     path('about',views.about,name="about"),
     
    #  path('test/',views.arin)

    # path('root yönü',dönecek istek,opsiyonel(kısayol ismi))

]
