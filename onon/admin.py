from django.contrib import admin
from onon.models import Zahltag, Feature, NonfeatureContent
import autocomplete_light
from lstory.models import Story


class ZahltagAdmin(admin.ModelAdmin):
    pass
admin.site.register(Zahltag, ZahltagAdmin)
admin.site.register(NonfeatureContent, ZahltagAdmin)

class AutocompleteOnonItems(autocomplete_light.AutocompleteGenericBase):
    choices = (
            Story.objects.all(),
            Zahltag.objects.all(),
            NonfeatureContent.objects.all(),
        )
    search_fields = (('title',),('name','url', 'image',),('text','url',))
autocomplete_light.register(AutocompleteOnonItems)

class FeatureAdminForm(autocomplete_light.GenericModelForm):
    main_story = autocomplete_light.GenericModelChoiceField(
        widget=autocomplete_light.ChoiceWidget(
            autocomplete='AutocompleteOnonItems',
            autocomplete_js_attributes={'minimum_characters': 0}))
    other_story = autocomplete_light.GenericModelChoiceField(
        widget=autocomplete_light.ChoiceWidget(
            autocomplete='AutocompleteOnonItems',
            autocomplete_js_attributes={'minimum_characters': 0}))

    class Meta:
        model = Feature
        exclude = ('main_content_type', 'main_object_id', 'other_content_type','other_object_id',)


class FeatureAdmin(admin.ModelAdmin):
    form = FeatureAdminForm
admin.site.register(Feature, FeatureAdmin)
