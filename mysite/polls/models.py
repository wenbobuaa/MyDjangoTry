from django.db import models

# Create your models here


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('max_length=200')


class Choice(models.Model):
    question_text = models.ForeignKey(Question)
    choice_text = modelsCharField(max_length=200)
    votes = modles.IntegerField(default=0)
