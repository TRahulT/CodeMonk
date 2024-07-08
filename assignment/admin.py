from django.contrib import admin
from .models import Paragraph,Word,CustomUser
# Register your models here.
admin.site.register(Paragraph)
admin.site.register(Word)
admin.site.register(CustomUser)
