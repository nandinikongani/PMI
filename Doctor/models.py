from django.db import models

# Create your models here.


class doctorModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    specialization = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='doctorregister'



class doctorreportmodel(models.Model):
    name = models.CharField(max_length=50)
    bid = models.CharField(max_length=40, default="",editable=True,unique=True)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    ldh = models.CharField(max_length=40)
    ast = models.CharField(max_length=40)
    triglycerides = models.CharField(max_length=40)
    phlevel = models.CharField(max_length=40)
    pmi = models.CharField(max_length=40)


    def  __str__(self):
        return self.bid

    class Meta:
        db_table='doctorreport'


