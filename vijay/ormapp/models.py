from django.db import  models
from django.contrib import admin
class Bank_loan(models.Model):
   Name=models.CharField(max_length=10)
   Aadharno=models.IntegerField(primary_key="Aadharno")
   Accountno=models.IntegerField()
   Address=models.CharField(max_length=10)
   Email=models.EmailField()
class Bank_loanAdmin(admin.ModelAdmin):
   list_display=('Name','Aadharno','Accountno','Address','Email') 
   
 
