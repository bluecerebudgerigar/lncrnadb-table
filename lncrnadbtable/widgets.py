from django.conf import settings
from django.forms import Textarea
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.translation.trans_real import get_language
from utils import static_url
import re


class AssociatedcompTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )], 
        }

    def render_textarea(self, name, value, attrs=None):
        return super(AssociatedcompTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]

        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        
        return mark_safe(render_to_string(
            'cms/plugins/widgets/associatedcomp.html', context))
            
            
    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)




class SequencesTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
                'js/sequence_ajax.js'
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )], 
        }

    def render_textarea(self, name, value, attrs=None):
        return super(SequencesTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]

        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        
        return mark_safe(render_to_string(
            'cms/plugins/widgets/sequences.html', context))
            
            
    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)






class NomenclatureTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )], 
        }

    def render_textarea(self, name, value, attrs=None):
        return super(NomenclatureTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]

        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        
        return mark_safe(render_to_string(
            'cms/plugins/widgets/nomenclature.html', context))
            
            
    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)
            

class AnnotationTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )], 
        }

    def render_textarea(self, name, value, attrs=None):
        return super(AnnotationTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]
  

        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        
        
        return mark_safe(render_to_string(
            'cms/plugins/widgets/annotation.html', context))

    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)
            
            
class ExpressionTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )],
        }

    def render_textarea(self, name, value, attrs=None):
        return super(ExpressionTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]


        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        return mark_safe(render_to_string(
            'cms/plugins/widgets/expression.html', context))

    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)

            
class SpeciesTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )],
        }

    def render_textarea(self, name, value, attrs=None):
        return super(SpeciesTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]
   
        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        return mark_safe(render_to_string(
            'cms/plugins/widgets/species.html', context))

    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)


            
class LiteratureTableWidget(Textarea):
    class Media:
        js = [static_url(path) for path in (
                'js/jquery-1.8.3.min.js',
                'js/jquery.handsontable.full.js',
                'js/jquery.contextMenu.js',
                'js/jquery.ui.position.js',
                'js/json2.js',
                'js/bootstrap-typeahead.js',
            )]
        css = {
            'all': [static_url(path) for path in (
                'css/jquery.handsontable.full.css',
                'css/jquery.contextMenu.css',
            )],
        }

    def render_textarea(self, name, value, attrs=None):
        return super(LiteratureTableWidget, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        language = get_language().split('-')[0]

        context = {
            'name': name,
            'language': language,
            'data': value,
            'STATIC_URL': settings.STATIC_URL,
        }
        return mark_safe(render_to_string(
            'cms/plugins/widgets/literature.html', context))

    def render(self, name, value, attrs=None):


        return self.render_textarea(name, value, attrs) + \
            self.render_additions(name, value, attrs)




