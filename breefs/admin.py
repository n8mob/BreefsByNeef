from django.contrib import admin

# Register your models here.
from breefs.models import Breef, Section, Page, PageBreef

admin.site.register(Breef)
admin.site.register(Section)
admin.site.register(Page)
admin.site.register(PageBreef)
