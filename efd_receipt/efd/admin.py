from django.contrib import admin
from .models import Taxpayer,Address,Business,Receipt

# Register your models here.
admin.site.register(Taxpayer)
admin.site.register(Address)
admin.site.register(Business)
admin.site.register(Receipt)
