from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_is_main = len([form for form in self.forms if form.cleaned_data.get('is_main')])
        if count_is_main > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif count_is_main == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1
    formset = ScopeInlineFormset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
