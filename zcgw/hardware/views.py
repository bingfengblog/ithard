#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render_to_response
from froms import CityForm,ItemForm
from hardware.models import City,Item,User,Type
from django.db.models import Q
from rest_framework import viewsets,generics
from hardware.serializers import UserSerializer, ItemSerializer,CitySerializer
from rest_framework import filters

# Create your views here.
def index(request):
    citys = City.objects.all()
    return render(request,'hardware/index.html',{'citys':citys})

def showcity(request,city_id,type_id=0):
    context_dict = {}
    citys = City.objects.all()
    context_dict['type_id']=type_id
    context_dict['citys']=citys
    context_dict['city_id']=int(city_id)
    if city_id=='0':
        if type_id==0:
            context_dict['item']=Item.objects.filter().order_by("item_name")
            context_dict['else_num']=Item.objects.filter(type_id=6).count()
            context_dict['pc_num']=Item.objects.filter().count() - context_dict['else_num']
            context_dict['nouse_num']=Item.objects.filter(is_use=0).count()
        elif type_id=='4':
            context_dict['item']=Item.objects.filter(Q(type_id=6)|Q(type_id=4)|Q(type_id=5)).order_by("-depart")
        elif type_id == '7':
            context_dict['item']=Item.objects.filter(is_use=0)
        else:
            context_dict['item']=Item.objects.filter(type_id=type_id).order_by("item_name")

    else:
        if type_id==0:
            context_dict['item']=Item.objects.filter(city_id=city_id).order_by("-depart")
            context_dict['else_num']=Item.objects.filter(city_id=city_id,type_id=6).count()
            context_dict['pc_num']=Item.objects.filter(city_id=city_id).count() - context_dict['else_num']
            context_dict['nouse_num']=Item.objects.filter(is_use=0).count()
        elif type_id=='4':
            context_dict['item']=Item.objects.filter(Q(city_id=city_id),Q(type_id=6)|Q(type_id=4)|Q(type_id=5)).order_by("-depart")
        elif type_id == '7':
            context_dict['item']=Item.objects.filter(city_id=city_id,is_use=0)
        else:
            context_dict['item']=Item.objects.filter(city_id=city_id,type_id=type_id).order_by("-depart")
    return render(request,'hardware/showcity.html',context_dict)

class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑Item的 API endpoint
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # filter_backends = (filters.DjangoFilterBackend,)
# class CityListView(generics.ListAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer
#     filter_backends = (filters.DjangoFilterBackend,)


