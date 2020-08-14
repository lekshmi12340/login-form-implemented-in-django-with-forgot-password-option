from django.db import models
class user(models.Model):
    name=models.CharField(max_length=50)
    loginid=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    emailaddress = models.CharField(max_length=20)
    phonenumber = models.IntegerField()

    class Meta:
        verbose_name_plural='user details'
    def __str__(self):
        return self.name
class resetpassword(models.Model):
    yourloginid = models.CharField(max_length=20)
    enterpassword=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    class Meta:
        verbose_name_plural='Password Reset'
    def __str__(self):
        return self.nameo

