#!/usr/bin/env python 

from bs4 import BeautifulSoup
import urllib2
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")
import re
import json, simplejson
#from HTMLParser import HTMLParser


##
##class URLFINDER:
##    ### convert list of pudmed id into 1. authour and year
##    ### and urls ###
##    def __init__(self):
##        self.aut_year = {}
##        self.urls = {}
##    


#
#class MLStripper(HTMLParser):                                               
#    def __init__(self):                                                     #Snippets from the web, should really write my own
#        self.reset()                                                        #
#        self.fed = []                                                       #
#    def handle_data(self, d):                                               #
#        self.fed.append(d)                                                  #
#    def get_data(self):                                                     #
#        return ''.join(self.fed)                                            #
#                                                                            #
#def strip_tags(html):                                                       #
#    s = MLStripper()                                                        #
#    s.feed(html)                                                            #

def convert_ref(text):
    aut_year = {}
    id_string = ",".join(text)
    url_pmd = "http://www.ncbi.nlm.nih.gov/pubmed/?term=%s&report=docsum&format=xml" % id_string
    url_response = urllib2.urlopen(url_pmd)
    url_response = url_response.read()
    url_response = BeautifulSoup(url_response)
    aut = url_response.find_all("p", {"class":"desc"})
    year = url_response.find_all("p",{"class":"details"})
    for x, y, z in zip(year, aut, text):
        dates = list(x.children)[1]
        dates = re.search("\d{4}",dates)
        first_aut = y.string
        first_aut =re.search("\w+",first_aut)
        entry = "<a href=\\\"http://www.ncbi.nlm.nih.gov/pubmed/%s\\\">(%s_%s)</a>" % (str(z), str(dates.group(0)), str(first_aut.group(0)))
        aut_year[z] = entry
    print "conversion completed"
    return aut_year
    
def convert_ref_literature(text):
    converted = [] ##list of list
    p = re.compile(r'(\[)|(\])|(<.*?>)')
    id_string = ",".join(text)
    url_pmd = "http://www.ncbi.nlm.nih.gov/pubmed/?term=%s&report=docsum&format=xml" % id_string
    url_response = urllib2.urlopen(url_pmd)
    url_response = url_response.read()
    url_response = BeautifulSoup(url_response)
    aut = url_response.find_all("p", {"class":"desc"})
    year = url_response.find_all("p",{"class":"details"})
    title = url_response.find_all("p",{"class":"title"})
    
    for w, x, y, z in zip(title, year, aut, text):
        entry =[]
        
        dates = list(x.children)[1]
        dates = re.search("\d{4}",dates)
        first_aut = y.string
        first_aut =re.search("\w+",first_aut)

        entry_title=p.sub('', str(w))
        pubmed_link =  "<a href=\\\"http://www.ncbi.nlm.nih.gov/pubmed/%s\\\">%s</a>" % (str(z), str(z))
        entry.append([pubmed_link, str(first_aut.group(0)),entry_title, str(dates.group(0))])
        converted.extend(entry)
    print "conversion completed"
    return converted

class sequence_converter(object):
    def __init__(self, json_data, seq_name):
        self.seq_name = seq_name
        self.data = json_data[1:]
        self.header = json_data.pop(0)
        self.return_array = [self.header]
    
    
        
    def convert_data_to_dict(self):
        
        self.original_dict = { key : value for key, value in enumerate(self.data)}
        
        
        accession_list = [str(x[1]).lower() for x in self.data if x[1] ]
        self.data_dict = {key : value for key, value in enumerate(accession_list)}
        
        self.reverse_dict = { value : key for key, value in enumerate(accession_list) }
        
        
    def find_unmatched_queries(self):
        unmatch = dict([ (x,y) for x,y in self.data_dict.iteritems() if re.match("<[^>]*>", y ) is None])
        print unmatch
        self.unmatch =  unmatch
        
        
    def unmatched_as_list(self):
        unmatch_keys = self.unmatch.keys()
        unmatch_keys = sorted(unmatch_keys)
        unmatch_list = []
        for keys in unmatch_keys:
            unmatch_list.append(self.data_dict[keys])
        
        unmatch_list = ",".join(unmatch_list)            
        self.unmatch_list = unmatch_list
         
        
    def read_get_beauty(self, url_terms):
        url_response = urllib2.urlopen(url_terms)                        
        url_response = url_response.read()                                    
        url_response = BeautifulSoup(url_response)                            
        self.url_response = url_response
        
        
    def find_multimapper(self):
        multi_mapper = []
        url_response =  self.url_response
        termset = url_response.find_all("termset")
        for x in termset:
            if  int(x.find("count").get_text())  > 1:
                multi_mapper.append(str(x.find("term").get_text()))


        multi_mapper = [ re.sub("\[.*\]|\"","",x) for x in multi_mapper]
        multi_mapper = [ x.lower() for x in multi_mapper ]       
        
        for x in multi_mapper:
            try:
                main_key = self.reverse_dict[x]
                print main_key
                del self.unmatch[main_key]
                self.original_dict[main_key] = ["Error Multi-mapper found ",x,"check id"]
                
            except ValueError:
                pass
            except KeyError:
                pass 
   
    
    def find_unfound(self):
        url_response = self.url_response
        unfound = url_response.find_all("phrasenotfound")
        if unfound is not None:
            unfound = [x.get_text() for x in unfound]
            unfound = [re.sub("\[.*\]","",x) for x in unfound]
            for x in unfound:
                try:
                    main_key = self.reverse_dict[x]
                    
                    del self.unmatch[main_key]
                    self.original_dict[main_key] = ["Error unfound terms ",x,"check id"]
                except ValueError:
                    pass
                except KeyError:
                    pass
                    
                    
    def accession_to_uid(self):
        url_response = self.url_response
        uid_list = [x.get_text() for x in url_response.find_all("id")]
        self.accession_uid_map = dict([ (str(uid), unmatch ) for unmatch, uid in zip(self.unmatch_list.split(','), uid_list)])
        self.uid_list = ",".join(uid_list)
                
        
        
                    
    def find_details(self):
        url_response = self.url_response
        url_response = url_response.find_all("gbseq")
        detail_dict = {}
        
        for x, y in zip(url_response, self.uid_list.split(',')):
            gbseq_primary = x.find("gbseq_primary")
            gbseq_organism = str(x.find("gbseq_organism").get_text())
            gbseq_sequence = str(x.find("gbseq_sequence").get_text())
            
            if gbseq_primary is None:
                gbseq_primary = x.find("gbseq_accession-version")
                gbseq_primary = ",".join(gbseq_primary)
            else:
                gbseq_primary = str(gbseq_primary.get_text())
                result = re.findall('\s([A-Za-z0-9\.]+)\s',gbseq_primary)
                gbseq_primary = ",".join(result)
                
            gbseq_primary = ["<a href=https://www.ncbi.nlm.nih.gov/nuccore/%s>%s</a>" % (x,x) for x in gbseq_primary.split(",")]
            gbseq_primary = ",".join(gbseq_primary)
            detail_dict[str(y)]= [str(gbseq_primary), str(gbseq_organism),  str(gbseq_sequence)]
        
        
        self.detail_dict = detail_dict 
        
        
    def reverse_match_details(self):
        detail_dict = self.detail_dict ## uid is key
        accession_uid_map = self.accession_uid_map ## uid is key, search term is value
        reverse_dict = self.reverse_dict ##search term is key, value is the entry no  
        for uid, details in detail_dict.iteritems():
            search_term  = accession_uid_map[uid]
            entry_no = reverse_dict[search_term] + 1
            
            sequence_name = "%s_%s_%s" % (self.seq_name, details[1], entry_no)
            sequence_name = sequence_name.lower()
            sequence_name = re.sub("\s","",sequence_name)
            details.insert(0, sequence_name)
            
            self.original_dict[entry_no] = details
    
    def build_return_array(self):
        entry_list = self.original_dict.keys()
        entry_list = sorted(entry_list)
        for entry_no in entry_list:
             self.return_array.append(self.original_dict[entry_no])
    
  #  
  #  def fix_sequence_name(self):
  #      for entry_no, details in self.data_dict.iteritems():
  #           sequence_name = "%s_%s_%s" % (self.seq_name, details[1], entry_no)
  #           sequence_name.lower()
  #           print details 
  #           
  #           sequence_name = re.sub("\s","",sequence_name)
  #           print "this is equence name %s" % sequence_name
  #           self.return_array.append(details)

            
def convert_function_sequence(json_data, pagename):
    
    
    seq_convertor = sequence_converter(json_data, pagename)            
    
    seq_convertor.convert_data_to_dict()
    print "this is %s" % seq_convertor.data
    
    
    seq_convertor.find_unmatched_queries()
    seq_convertor.unmatched_as_list()
    
  
    
    esearch_header = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=nucleotide&term="
    esearch_url = "%s%s" % (esearch_header, seq_convertor.unmatch_list)
    
    try :
        seq_convertor.read_get_beauty(esearch_url)
    except urllib2.HTTPError:
        print "Error in HTTP"
        return seq_convertor.json_data
    
    
    
    seq_convertor.find_multimapper()
    seq_convertor.find_unfound()
    seq_convertor.unmatched_as_list()
    
    print seq_convertor.unmatch_list
    print seq_convertor.unmatch
    print seq_convertor.data_dict

    if len(seq_convertor.unmatch_list) > 0:
        try :
            seq_convertor.read_get_beauty(esearch_url)
        except urllib2.HTTPError:
            print "Error in HTTP"
            return seq_convertor.json_data
    

        seq_convertor.accession_to_uid()
        efetch_header = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id="
        efetch_url = "%s%s&retmode=xml" % (efetch_header, seq_convertor.uid_list)
        try:
            seq_convertor.read_get_beauty(efetch_url)
        except urllib2.HTTPError:
            print "Error in HTTP"
            return seq_convertor.json_data
          
            
        seq_convertor.find_details()
        seq_convertor.reverse_match_details()
        seq_convertor.build_return_array()
    #   seq_convertor.fix_sequence_name()
        
    
        return seq_convertor.return_array   



    else:
        return json_data