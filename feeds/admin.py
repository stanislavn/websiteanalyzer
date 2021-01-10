from django.contrib import admin
from django.utils.safestring import mark_safe
import csv
from django.http import HttpResponse
# Register your models here.
from feeds import models

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


class SourceAdmin(admin.ModelAdmin):

    readonly_fields = (
        'posts_link',
    )

    def posts_link(self, obj=None):
        if obj.id is None:
            return ''
        qs = obj.posts.all()
        return mark_safe('<a href="/admin/feeds/post/?source__id=%i" target="_blank">%i Posts</a>' % (obj.id, qs.count()))
    posts_link.short_description = 'posts'

class PostAdmin(admin.ModelAdmin, ExportCsvMixin):

    raw_id_fields = ('source',)

    list_display = ('title', 'source', 'created', 'guid', 'author')
    list_filter = ('source', 'created')
    search_fields = ('title',)

    readonly_fields = (
        'enclosures_link',
    )

    def enclosures_link(self, obj=None):
        if obj.id is None:
            return ''
        qs = obj.enclosures.all()
        return mark_safe('<a href="/admin/feeds/enclosure/?post__id=%i" target="_blank">%i Enclosures</a>' % (obj.id, qs.count()))
    enclosures_link.short_description = 'enclosures'
    actions = ["export_as_csv"]

class EnclosureAdmin(admin.ModelAdmin):

    raw_id_fields = ('post',)

    list_display = ('href', 'type')

admin.site.register(models.Source, SourceAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Enclosure, EnclosureAdmin)
admin.site.register(models.WebProxy)
