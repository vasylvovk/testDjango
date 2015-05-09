from django.contrib import admin
from .models import Choice, Question

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #inlines = [ChoiceInline]

list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)