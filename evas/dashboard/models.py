# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.forms.models import model_to_dict


class Inventory(models.Model):
    id = models.BigIntegerField(primary_key=True)

    clientno = models.IntegerField(db_column='CLIENTNO')
    gloryid = models.CharField(db_column='GLORYID', max_length=30)
    startcash = models.IntegerField(db_column='STARTCASH')
    usamt = models.DecimalField(db_column='USAMT', max_digits=14, decimal_places=0)
    cashamt = models.DecimalField(db_column='CASHAMT', max_digits=14, decimal_places=0)
    siteno = models.IntegerField(db_column='SITENO', null=True, blank=True)
    lasttrace = models.CharField(db_column='LASTTRACE', max_length=20, null=True, blank=True)
    traceversion = models.IntegerField(db_column='TRACEVERSION')
    
    def __str__(self):
        return f'Inventory of {self.clientno}'
    
    def get_data(self, *args : str):
        if args is None: model_to_dict(self)
        data = { arg : self.__dict__.get(arg,None) for arg in args}
        return data
    
    class Meta:
        managed = False
        db_table = '[EVASAPP].[INVENTORY_V]'


class InventoryDtl(models.Model):
    id = models.BigIntegerField(primary_key=True)

    clientno = models.IntegerField(db_column='CLIENTNO')
    gloryid = models.CharField(db_column='GLORYID', max_length=30)
    startcash = models.IntegerField(db_column='STARTCASH')
    looseflg = models.IntegerField(db_column='LOOSEFLG')
    mediano = models.IntegerField(db_column='MEDIANO')
    amount = models.DecimalField(db_column='AMOUNT', max_digits=18, decimal_places=0)
    siteno = models.IntegerField(db_column='SITENO', null=True, blank=True)
    traceversion = models.IntegerField(db_column='TRACEVERSION')
    lasttrace = models.CharField(db_column='LASTTRACE', max_length=20, null=True, blank=True)

    def __str__(self):
        return f'Detailed Inventory of {self.clientno}'
    
    def get_data(self, *args : str):
        if len(args) == 0: return model_to_dict(self)
        data = { arg : self.__dict__.get(arg) for arg in args}
        return data
    
    class Meta:
        managed = False
        db_table = '[EVASAPP].[INVENTORYDTL_V]'


class Mediamap(models.Model):
    mediano = models.IntegerField(db_column='MEDIANO', primary_key=True)  # Field name made lowercase.
    value = models.DecimalField(db_column='VALUE', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '[EVASAPP].[MEDIAMAP]'
