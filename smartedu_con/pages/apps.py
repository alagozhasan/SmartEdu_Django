from django.apps import AppConfig
#uygulama ayarları gibi

class PagesConfig(AppConfig):
    #kayıt edilecek class ismi
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
