from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_no = models.CharField(max_length=11)
    password = models.CharField(max_length=100)


    def register(self):
        return self.save()
    
    def isExist(self):
        if User.objects.filter(email=self.email):
            return True
        return False


    @staticmethod
    def loginByEmail(email):
        try:
            return User.objects.get(email=email)
        except:
            return False
