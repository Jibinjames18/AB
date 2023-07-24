from django.db import models


# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Account(models.Model):
    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=250)
    phone_number=models.CharField(max_length=100)
    mail_id=models.EmailField()
    address=models.TextField()
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    account_type=models.CharField(max_length=250)
    materials_provide=models.ManyToManyField('Material')

    def __str__(self):
        return self.name

class Material(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name


