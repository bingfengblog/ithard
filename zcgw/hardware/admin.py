#coding:utf-8
from django.contrib import admin
from hardware.models import City,Depart,User,Item,Type
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_filter = ('depart','city','type',)
    list_display = ('item_name','city','depart','get_type','get_price','user','buy_date','suplier','is_use','describe',)
    def get_type(self,obj):
        return obj.type.type_name
    get_type.short_description = '设备类型'
    def get_price(self, obj):
        return obj.type.price
    get_price.short_description = '价格'
    def get_city(self,obj):
        city_id=obj.user.city_id
        return City.objects.get(id=city_id).cityname
    get_city.short_description = '城市'
class UserAdmin(admin.ModelAdmin):
    list_display = ('city','department','username','male',)

class TypeAdmin(admin.ModelAdmin):
     list_display = ('type_name','price')
admin.site.register(City)
admin.site.register(Type,TypeAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Item,ItemAdmin)
admin.site.register(Depart)