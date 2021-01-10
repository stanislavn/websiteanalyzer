from .models import FacebookPage, FacebookPost
from django import forms
from django.contrib import admin
import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, dialect='excel')

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class FacebookPostForm(forms.ModelForm):

    class Meta:
        model = FacebookPost
        exclude = ['link','description','pub_date','time']


class FacebookPostAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ('text',)
    autocomplete_fields = ['facebook_page_id']
    list_filter = ('facebook_page','time')
    list_display = ('text','facebook_page','likes','comments','shares', 'like', 'love', 'wow', 'haha', 'sorry', 'anger')
    #form = FacebookPostForm
    #exclude = ['link','description','pub_date','time']
    actions = ["export_as_csv"]


class FacebookPageAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ('name',)
    list_display = ('id','name','link','description')
    actions = ["export_as_csv"]


admin.site.site_header = 'Trust rank'


#admin.site.register(Website)
admin.site.register(FacebookPage, FacebookPageAdmin)
admin.site.register(FacebookPost, FacebookPostAdmin)




