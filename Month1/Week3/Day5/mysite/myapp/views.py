# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'myapp/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'myapp/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse(
                        'polls:results', args=(question.id,)))
