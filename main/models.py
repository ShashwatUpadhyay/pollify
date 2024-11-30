from django.db import models
from django.utils.text import slugify
import random

# Create your models here.
class Poll(models.Model):
    poll_name = models.TextField()
    creator= models.CharField(max_length=100)
    uuid = models.CharField(max_length=60)
    slug = models.CharField(max_length=70,null=True,blank=True)
    code = models.CharField(max_length=50)
    open = models.BooleanField(default=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.poll_name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.poll_name   
    
class Option(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    option = models.TextField()
    upload_time = models.DateTimeField(auto_now_add=True, null=True)

    
    
    def __str__(self):
        return f'{self.poll.poll_name}" "{self.option}'
    
class Response(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    Option = models.ForeignKey(Option , on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return f'{self.poll.poll_name}" - "{self.Option.option}'

    
    
    
    
    