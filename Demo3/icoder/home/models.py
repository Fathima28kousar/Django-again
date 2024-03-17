from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add = True, blank = True)
    content = models.TextField(null = True)

    def __str__(self):
        return 'Message from ' + self.name + ' email is ' + self.email