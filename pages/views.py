# ilgili istekleri burdaki functs ile karşılarım
from django.shortcuts import render

# Create your views here.


def index(req):
    # return HttpResponse("<h1>INDEX SAYFASI</h1>")
    return render(req, "index.html")


# render(parametre olarak gelen requeste karşılık,templates klasörü içinde bulunan index.hmtl i göster)
#! templates klasörü manuel olarak uygulamanın içine templates isimli kallasör olarak açılır
# bunun yerine tek bir template kullanımı da olabilir,projenin büyüklüğüne göre tek bir template klasör yeterli olacaktır
# çünkü benim her bir uygulamam bu projede ayrı html leri var #! böyle yapacaksam ana dizinde settings.py a bunu bildirmem gerekir
def about(req):
    return render(req, "about.html")
