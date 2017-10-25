from django.contrib import admin

# Register your models here.
from .forms import Stage1Form
from stage1.models import Stage1
class Stage1Admin(admin.ModelAdmin):
 list_display=("__unicode__","address","city","state")
 form=Stage1Form
 #class Meta:
    #model=Stage1

admin.site.register(Stage1,Stage1Admin)