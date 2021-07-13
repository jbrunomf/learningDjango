from django.shortcuts import render, HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create your views here.


def index(request):
    context = {'latest_question_list': Question.objects.order_by('-pub_date')[:5]}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "Você está visualizando o resultado da questão %s."
    return HttpResponse(response % question_id)
