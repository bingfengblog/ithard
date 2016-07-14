#coding:utf-8
from django.db import models
from django.utils import timezone

# Create your models here.
"""城市"""
class City(models.Model):
    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = u'城市'
    cityname = models.CharField(max_length=10,unique=True)
    def __unicode__(self):
        return self.cityname

"""部门"""
class Depart(models.Model):
    class Meta:
        verbose_name=u'部门'
        verbose_name_plural = u'部门'
    departname=models.CharField(u'部门',max_length=10)
    def __unicode__(self):
        return  self.departname


class User(models.Model):
    class Meta:
        verbose_name = u'员工姓名'
        verbose_name_plural = u'员工'
        ordering=['-username']
    department = models.ForeignKey(Depart,null=True,blank=True,verbose_name=u'部门')
    username = models.CharField(u'姓名',max_length=10,unique=True)
    city=models.ForeignKey(City,default=None,verbose_name=u'城市')
    nan='male'
    nv='female'
    male_choices = (
        (nan,u'男'),
        (nv,u'女'),
    )
    male = models.CharField(u'性别',max_length=10,choices=male_choices,default=nan)
    def __unicode__(self):
        return self.username
class Type(models.Model):
    class Meta:
        # verbose_name = "员工姓名"
        verbose_name_plural = u'设备型号'
    type_name=models.CharField(u'设备型号',max_length=10,default='',unique=True)
    price=models.IntegerField(u'价格',default=0)
    def __unicode__(self):
        return self.type_name
class Item(models.Model):
    class Meta:
        verbose_name = u'硬件'
        verbose_name_plural = u'电脑'
    item_name=models.CharField(u'设备编号',max_length=10,unique=True)
    depart = models.ForeignKey(Depart,default='',blank=True,null=True,verbose_name=u'部门')
    user = models.ForeignKey(User,default='',blank=True,null=True,verbose_name=u'使用人',related_name='items')
    city = models.ForeignKey(City,default=1,verbose_name=u'城市',related_name='items')
    type=models.ForeignKey(Type,default='',verbose_name=u'设备类型')
    describe = models.CharField(u'备注',default='',blank=True,max_length=20)
    buy_date = models.DateTimeField(u'采购时间',default=timezone.now)
    is_use = models.NullBooleanField(u'是否在用',default=False)
    suplier = models.CharField(u'供应商',max_length=10,blank=True,null=True)
    def __unicode__(self):
        return self.item_name





