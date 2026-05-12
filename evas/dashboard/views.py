from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import *

# Create your views here.
def index(request):
    user_details = [user.get_data('clientno','gloryid','usamt') for user in Inventory.objects.all()]
    return render(request,'dashboard/index.html',context={'user_details' : user_details})

def detail(request, id : str = None):
    media_data = {media.mediano : media.value for media in Mediamap.objects.all()}
    if id is None:
        detailed_inventory = {}
    else:
        client_no , glory_id = id.removeprefix('c').split('g')
        _user = Inventory.objects.get(clientno = int(client_no), gloryid = glory_id)
        detailed_inventory = [user.get_data() for user in InventoryDtl.objects.filter(gloryid = _user.gloryid, clientno = _user.clientno)]
        for user in detailed_inventory:
            user['media_value'] = media_data[user['mediano']]
    return render(request,'dashboard/detail.html',context={'detailed_inventory' : detailed_inventory, 'mediaMap' : media_data, 'total_amount' : _user.cashamt})
