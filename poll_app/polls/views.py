from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import F

from .models import Question, Choice

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return a full list of published questions."""
        return Question.objects.order_by('question_text')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice_set = question.choice_set.all().filter(choice_text=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Re-display the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice_set.update(votes=F('votes')+1)
        return HttpResponseRedirect(reverse('polls:detail', args=(question_id)))

def reset(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    c_set = question.choice_set.all()
    c_set.update(votes=0)
    return HttpResponseRedirect(reverse('polls:results', args=(question_id)))

def showResults(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    c_set = question.choice_set.all()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
