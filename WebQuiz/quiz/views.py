from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
	questions = Question.objects.all()
	context = {"questions": questions , 
			}
	return render(request , "quiz/index.html" , context)

def ques(request , question_id):
	question = get_object_or_404(Question , pk=question_id)
	return render(request , 'quiz/ques.html' ,{'question':question})