from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Interview(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    running = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
class QA(models.Model):
    interview = models.ForeignKey(Interview,on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField(default=False)
    
    def __str__(self):
        return self.question

    
