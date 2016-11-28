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
        #selected_choice = question.choice_set.get(choice_text=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Re-display the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        #selected_choice.votes += 1
        #selected_choice.save()
        selected_choice_set.update(votes=F('votes')+1)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the back button.
        #return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
