from django.db import models
from teachers.models import Teacher
# Create your models here.
# her bir özellik tabloda bir ütun alana gelir
# classın kendisi de bir tablo


class Category(models.Model):
    title = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    teacher=models.ForeignKey(Teacher,null=True,on_delete=models.CASCADE)
    #CASCADE = öğretmen silinirse tüm kursları silinsin demek
    name = models.CharField(
        max_length=200,
        unique=True
        # verbose_name="Kurs adı",
        # help_text='Kurs adını yazınız'
    )
    category = models.ForeignKey(
        Category, null=True, on_delete=models.DO_NOTHING
    )  # models.Donthing =kategoriyi ssilersem kurslar alsın alamıına gelir
    tags = models.ManyToManyField(Tag, #ilişki sağlanancak vt modeli
                                  null=True, blank=True)
    description = models.TextField(
        blank=True, null=True  # son kullanıcı  # developer açısı
    )
    image = models.ImageField(
        upload_to="courses/%Y/%m/%d/",
        default="courses/messi.jpg",  # resim yüklenmez ise
    )
    date = models.DateTimeField(
        auto_now=True,  # o anın tarihini otomatik ver
    )
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # model ım oluştu bunlar da alanları
    # kurs tablo diğerleri de tablonaıun sütunları
