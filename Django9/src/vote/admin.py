from django.contrib import admin
from .models import Question, Choice, Comment
# Register your models here.


admin.site.register(Question)#45
admin.site.register(Choice)
admin.site.register(Comment)