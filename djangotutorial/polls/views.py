from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader

from polls.models import Question

# Create your views here.

def index (request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = { "latest_question_list": latest_question_list }
    # template = loader.get_template("polls/index.html")
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def detail (request, question_id):
    # try:
        # question = Question.objects.get(pk=question_id)
        # context = { "question": question }
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist you fool!")
    question = get_object_or_404(Question, pk=question_id)
    context = { "question": question }
    return render(request, "polls/detail.html", context)

def results (request, question_id):
    response = f"You are looking at the results of question {question_id}."
    return HttpResponse(response)

def vote (request, question_id):
    return HttpResponse(f"You are voting on question {question_id}.")

