from django.db import models


class bodydetails(models.Model):
        name = models.CharField(max_length=50)
        bid = models.CharField(max_length=40,default="", editable=True,unique=True)
        age   = models.CharField(max_length=40)
        gender = models.CharField(max_length=40)
        weight = models.CharField(max_length=50, default="", editable=True)
        blood  = models.CharField(max_length=40, default="", editable=True)
        evidence  = models.CharField(max_length=40, default="", editable=True)
        body = models.FileField(upload_to='files/pdfs/')

        def __str__(self):
            return self.bid

        class Meta:
            db_table = 'bodydetails'





















