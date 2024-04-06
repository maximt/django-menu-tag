from django.contrib import admin
from .models import Menu, MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    fields = (
        'title',
        'parent',
        'url',
        'named_url',
        'named_url_kwargs'
    )

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['parent'].queryset = MenuItem.objects.filter(
            menu=obj
        )
        return formset


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)

    inlines = [
        MenuItemInline,
    ]


admin.site.register(Menu, MenuAdmin)
