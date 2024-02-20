from django.db import models

# Create your models here.
class Exportdocs(models.Model):
    docid = models.AutoField(db_column='docId', primary_key=True)  # Field name made lowercase.
    invoiceno = models.CharField(db_column='invoiceNo', max_length=7)  # Field name made lowercase.
    shippingbillnumber = models.CharField(db_column='shippingBillNumber', max_length=20)  # Field name made lowercase.
    shippingbilldate = models.DateField(db_column='shippingBillDate')  # Field name made lowercase.
    exchangerate = models.DecimalField(db_column='exchangeRate', max_digits=6, decimal_places=2)  # Field name made lowercase.
    fobvalue_inr_field = models.DecimalField(db_column='fobValue(INR)', max_digits=12, decimal_places=2)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    fobvalueforex = models.DecimalField(db_column='fobValueForex', max_digits=12, decimal_places=2)  # Field name made lowercase.
    dutydrawback = models.DecimalField(db_column='dutyDrawBack', max_digits=8, decimal_places=2)  # Field name made lowercase.
    blnumber = models.CharField(db_column='blNumber', max_length=15)  # Field name made lowercase.
    bldate = models.DateField(db_column='blDate')  # Field name made lowercase.
    brcno = models.CharField(db_column='brcNo', max_length=25)  # Field name made lowercase.
    brcdate = models.DateField(db_column='brcDate')  # Field name made lowercase.
    brcamtinfx = models.DecimalField(db_column='brcAmtInFx', max_digits=8, decimal_places=2)  # Field name made lowercase.
    brccurrency = models.CharField(db_column='brcCurrency', max_length=12)  # Field name made lowercase.
    egmno = models.CharField(db_column='egmNo', max_length=15)  # Field name made lowercase.
    egmdate = models.DateField(db_column='egmDate')  # Field name made lowercase.
    phytono = models.CharField(db_column='phytoNo', max_length=20)  # Field name made lowercase.
    phytodate = models.DateField(db_column='phytoDate')  # Field name made lowercase.
    courierbooking = models.CharField(db_column='courierBooking', max_length=20)  # Field name made lowercase.
    courierbookingdate = models.DateField(db_column='courierBookingDate')  # Field name made lowercase.
    trackingno = models.CharField(db_column='trackingNo', max_length=20)  # Field name made lowercase.
    poddeliverydate = models.DateField(db_column='podDeliveryDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exportdocs'