from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('Date published')
    def __str__(self):
        return self.question_text
    def was_pub_recently(self):
        return self.pub_date>timezone.now()-datetime.timedelta(days=1)

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    vote=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

