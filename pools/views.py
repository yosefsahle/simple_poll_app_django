from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Question, Choice
from .forms import PollForm, QuestionForm, ChoiceForm

def poll_list(request):
    polls = Poll.objects.all()
    return render(request, 'polls/poll_list.html', {'polls': polls})

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_detail.html', {'poll': poll})

def poll_vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        for question in poll.question_set.all():
            selected_choice = question.choice_set.get(pk=request.POST[str(question.id)])
            selected_choice.votes += 1
            selected_choice.save()
        return redirect('poll_detail', poll_id=poll.id)
    return render(request, 'polls/poll_vote.html', {'poll': poll})
