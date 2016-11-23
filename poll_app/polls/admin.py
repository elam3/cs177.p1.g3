from django.contrib import admin

# Register your models here.

#from .models import Quiz
#admin.site.register(Quiz)
from .models import Question
admin.site.register(Question)
