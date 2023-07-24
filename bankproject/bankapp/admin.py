from django.contrib import admin

# Register your models here.
from.models import District,Branch,Account,Material

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(Material)