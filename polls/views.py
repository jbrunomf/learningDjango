from django.shortcuts import render, HttpResponse
from .models import Question
# Create your views here.


def index(request):
    context = {'latest_question_list': Question.objects.order_by('-pub_date')[:5]}
    return render(request, template_name='polls/index.html', context=context)


def detail(request, question_id):
    return HttpResponse("Você está visualizando a questão %s.", question_id)


def results(request, question_id):
    response = "Você está visualizando o resultado da questão %s."
    return HttpResponse(response % question_id)

