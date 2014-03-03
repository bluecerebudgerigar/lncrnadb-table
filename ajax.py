from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from menus.menu_pool import menu_pool


@dajaxice_register
def sayhello(request, test):
    nodes = menu_pool.get_nodes(request)  
    #nodes = menu_pool.get_nodes(request)
    browse = [x for x in nodes if x.title == "Browse"]
    
    return simplejson.dumps({'message':'Hello World'})