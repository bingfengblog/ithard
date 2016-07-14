#coding:utf-8
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zcgw.settings')

import django
django.setup()

from hardware.models import City,Depart,User,Item

"""添加测试数据"""
def populate():
    city_name1 = add_city(name='厦门')
    city_name2 = add_city(name='漳州')
    city_name3 = add_city(name='泉州')
    item1 = add_item(name="笔记本电脑",price=4500,suplier=None)
    item2 = add_item(name="开发主机",price=5200,suplier=None)
    depart1 = add_depart(name="开发部")
    depart2 = add_depart(name="人事部")

    add_user(username="段智峰",
        depart=depart1,
        city=city_name1,
        pc=item1)


    # # Print out what we have added to the user.
    # for c in User.objects.all():
    #         print "- {0} - {1}".format(str(c))

def add_user(username,depart,city,pc ):
    p = User.objects.get_or_create(username=username, department=depart, city=city, pc=pc)[0]
    return p

def add_city(name):
    c = City.objects.get_or_create(cityname=name)[0]
    return c
def add_item(price,name,suplier):
    i = Item.objects.get_or_create(price=price,item_name=name,suplier=None)[0]
    return i
def add_depart(name):
    d = Depart.objects.get_or_create(departname=name)[0]
    return d


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
