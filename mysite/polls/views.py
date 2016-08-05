from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World! You're at polls index.")


def detail(request, question_id):
    return HttpResponse("You're at {id} question detail.".format(id=question_id))


def result(request, question_id):
    return HttpResponse("You're at {id} question results.".format(id=question_id))


def vote(request, question_id):
    return HttpResponse("You're at {id} question vote.".format(id=question_id))

