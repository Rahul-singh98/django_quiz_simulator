from django.db import models

# Create your models here.
class Question(models.Model):
	question = models.CharField(max_length=200)
	choice_1 = models.CharField(max_length=30)
	choice_2 = models.CharField(max_length=30)
	choice_3 = models.CharField(max_length=30)
	choice_4 = models.CharField(max_length=30)
	correct_ans = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	
