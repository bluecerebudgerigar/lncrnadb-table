from django import forms
from django.forms.models import ModelForm
from widgets import AnnotationTableWidget, ExpressionTableWidget, SpeciesTableWidget, LiteratureTableWidget, NomenclatureTableWidget, SequencesTableWidget, AssociatedcompTableWidget
from models import Annotation, Expression, Species, Literature, Nomenclature, Sequences, Associatedcomp
from django.utils.translation import ugettext_lazy as _
import csv
from django.utils import simplejson
import re
from bs4test_mod import convert_ref, convert_ref_literature
import json, simplejson


class SequencesForm(ModelForm):
    table_data = forms.CharField(widget=SequencesTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
            
    
    class Meta:
        model = Sequences
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
        
        
        
class AssociatedcompForm(ModelForm):
    table_data = forms.CharField(widget=AssociatedcompTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
            
    
    class Meta:
        model = Associatedcomp
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
        
        



class NomenclatureForm(ModelForm):
    table_data = forms.CharField(widget=NomenclatureTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
            
    
    class Meta:
        model = Nomenclature
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
        


class AnnotationForm(ModelForm):
    table_data = forms.CharField(widget=AnnotationTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
            
    def clean_table_data(self):
        data = self.cleaned_data['table_data']
        PUBS = re.findall("PMID:(\d+)", data)
        if PUBS:
            PUBS = list(set(PUBS))
            PUBS_DIC = convert_ref(PUBS)
            for i in PUBS:
                href_tag = PUBS_DIC[i]
                pattern = "PMID:%s" % i
                data = data.replace(pattern, href_tag)
                 
        print data    
        return data
        
    
    class Meta:
        model = Annotation
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
        
        
class ExpressionForm(ModelForm):
    table_data = forms.CharField(widget=ExpressionTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
    
    class Meta:
        model = Expression
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )



    
class SpeciesForm(ModelForm):
    table_data = forms.CharField(widget=SpeciesTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
        
    
    class Meta:
        model = Species
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
            )
            
            
            
            
class LiteratureForm(ModelForm):
    table_data = forms.CharField(widget=LiteratureTableWidget)
    csv_upload = forms.FileField(label=_("upload .csv file"), help_text=_("upload a .csv file to fill the table up."), required=False)
    
    
    
    def clean_csv_upload(self):
        if self.cleaned_data['csv_upload']:
            csv_reader = csv.reader(self.cleaned_data['csv_upload'], dialect='excel')
            data = []
            for row in csv_reader:
                data.append(row)
            self.cleaned_data['table_data'] = simplejson.dumps(data)
            self.csv_uploaded = True
            
            
    
    def clean_table_data(self):    
        corrected = []
        correct_fields = []
        data = self.cleaned_data['table_data'] 
        #### '[[1,2,3],[2,3,4]]
    
        rclean =re.compile(r'\]|\[|\"')
        
        list_data = [rclean.sub('',x) for x in str(data).split("],[")] ## [[1,2,3],[2,3,4]] type list
        wrong_entries = []
        for i in xrange(len(list_data) -1,-1,-1):
            entry_fields = list_data[i].split(",")
            if "href" in entry_fields[0]:
                correct_fields.append(entry_fields)
            elif entry_fields[0] == "Pub Med ID":
                correct_fields.insert(0, entry_fields)

            else:
                wrong_entries.append(entry_fields[0])
                del list_data[i]
                

        corrected = convert_ref_literature(wrong_entries) ## return an list of list
        #
        correct_fields.extend(corrected)
        #correct_fields = [[i.replace("\\","") for i in x ] for x in correct_fields]
        print correct_fields
        correct_fields = [[i.replace("\\","") for i in x ] for x in correct_fields]
        data = simplejson.dumps(correct_fields)
        #print data  
        #data = data.replace("\\","")
       # data = unicode(correct_fields)
       # print data
        
        return data
            

        
    
    class Meta:
        model = Literature
        exclude = (
            'page',
            'position',
            'placeholder',
            'language',
            'plugin_type',
        )
        
        
