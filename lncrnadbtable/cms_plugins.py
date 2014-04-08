from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from models import Annotation, Expression, Species, Literature, Nomenclature, Sequences, Associatedcomp
from forms import AnnotationForm, ExpressionForm, SpeciesForm, LiteratureForm, NomenclatureForm, SequencesForm, AssociatedcompForm
from django.utils import simplejson
from utils import static_url
from django.http import HttpResponseRedirect
import re

class AssociatedcompPlugin(CMSPluginBase):
    model = Associatedcomp
    form = AssociatedcompForm
    render_template = "templates/cms/plugins/associatedcomp.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:

            data = simplejson.loads(instance.table_data)

        except:
            data = "error"
        context.update({
            'name': instance.name,
            'data': data,
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
        
        response = super(AssociatedcompPlugin, self).response_change(request, obj)
        
        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response

class SequencesPlugin(CMSPluginBase):
    model = Sequences
    form = SequencesForm
    render_template = "templates/cms/plugins/sequences.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (None, {
            'fields':('sequence_prefix',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:

            data = simplejson.loads(instance.table_data)

        except:
            data = "error"
        context.update({
            'name': instance.name,
            'data': data,
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
        
        response = super(SequencesPlugin, self).response_change(request, obj)
        
        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response



class NomenclaturePlugin(CMSPluginBase):
    model = Nomenclature
    form = NomenclatureForm
    render_template = "templates/cms/plugins/nomenclature.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:

            data = simplejson.loads(instance.table_data)

        except:
            data = "error"
        context.update({
            'name': instance.name,
            'data': data,
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
        
        response = super(NomenclaturePlugin, self).response_change(request, obj)
        
        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response





class AnnotationPlugin(CMSPluginBase):
    model = Annotation
    form = AnnotationForm
    render_template = "templates/cms/plugins/annotation.html"
    text_enabled = True
    

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:
            
            data = instance.table_data
            data = simplejson.loads(data)
        except:
            data = "error"
            
            
        context.update({
            'name': instance.name,
            'data': simplejson.loads(instance.table_data),
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
        
        response = super(AnnotationPlugin, self).response_change(request, obj)
        
        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response


class ExpressionPlugin(CMSPluginBase):
    model = Expression
    form = ExpressionForm
    render_template = "templates/cms/plugins/expression.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:
            #$ print instance.table_data
            #instance.table_data = instance.table_data.replace("is","are")
            data = simplejson.loads(instance.table_data)
            #if type(data) == list:
            #    print data
            #    data = [[x.replace("is","are") for x in i] for i in data]

        except:
            data = "error"
        context.update({
            'name': instance.name,
            'data': data,
            'instance':instance,
            'json_data': instance.table_data,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
         
        response = super(ExpressionPlugin, self).response_change(request, obj)

        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response
        
        
class SpeciesPlugin(CMSPluginBase):
    model = Species
    form = SpeciesForm
    render_template = "templates/cms/plugins/species.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )
    
    
    def render(self, context, instance, placeholder):
        try:
            
            data = instance.table_data
            data = simplejson.loads(data)
        except:
            data = "error"
            
            
        context.update({
            'name': instance.name,
            'data': simplejson.loads(instance.table_data),
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
         
        response = super(SpeciesPlugin, self).response_change(request, obj)

        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response
        
        
        

class LiteraturePlugin(CMSPluginBase):
    model = Literature
    form = LiteratureForm
    render_template = "templates/cms/plugins/literature.html"
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
        (_('Headers'), {

            'fields': (('headers_top', 'headers_left', 'headers_bottom'),)
        }),
        (None, {
            'fields': ('table_data', 'csv_upload')
        })
    )

    def render(self, context, instance, placeholder):
        try:
            data = instance.table_data
            data = simplejson.loads(instance.data)
        except:
            data = "error"
        context.update({
            'name': instance.name,
            'data': simplejson.loads(instance.table_data),
            'instance':instance,
        })
        return context

    def icon_src(self, instance):
        return static_url("img/table.png")

    def response_change(self, request, obj):
         
        response = super(LiteraturePlugin, self).response_change(request, obj)

        if 'csv_upload' in request.FILES.keys():
            self.object_successfully_changed = False
        return response

plugin_pool.register_plugin(AnnotationPlugin)
plugin_pool.register_plugin(ExpressionPlugin)
plugin_pool.register_plugin(SpeciesPlugin)
plugin_pool.register_plugin(LiteraturePlugin)
plugin_pool.register_plugin(NomenclaturePlugin)
plugin_pool.register_plugin(SequencesPlugin)
plugin_pool.register_plugin(AssociatedcompPlugin)


        #data_2 = obj.table_data
        #print type(data_2)
        #data_2 = data_2.replace("ky","kyness")
        #obj.table_data = data_2
       ## data_2 = request.POST.get("table_data")
       ## print data_2
       ## data_2 = data_2.replace("ky", "kyness")
       ## print data_2
       ## request.POST.__setitem__("table_data", data_2)
       ## data_2 = request.POST.get("table_data")
       ## print data_2
       ## print dir(obj)
       ##