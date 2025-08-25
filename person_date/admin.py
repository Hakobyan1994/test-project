from django.contrib import admin
from .models import PersonDate
# Register your models here.



class PersonDateAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "city","country","index"]
    list_filter = ("city", "country", "index")
    search_fields = ("first_name", "last_name", "city", "country", "index")
    ordering = ("last_name", "first_name")
    list_display_links = ("first_name", "last_name")


admin.site.register(PersonDate,PersonDateAdmin)
