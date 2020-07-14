from django.shortcuts import render, get_list_or_404, Http404
from django.http import HttpResponse
from django.template import loader
from .models import Feedback, Question
from .forms import FeedbackModelForm
# Create your views here.

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from .models import Feedback, Question


def index(request):
    all_feedbacks = Feedback.objects.all()
    template = loader.get_template('feedback/index.html')
    context = {
        'all_feedbacks': all_feedbacks
    }
    return HttpResponse(template.render(context, request))


def detail(request, feedback_id):
    try:
        feedback = Feedback.objects.get(id=feedback_id)
    except Feedback.DoesNotExist:
        raise Http404("Feedback doesnt exist")
    context = {
        'feedback': feedback
    }
    return render(request, 'feedback/feedback_details.html', context)


def feedback_create_view(request):
    form = FeedbackModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FeedbackModelForm()
    context = {
        'form': form
    }
    return render(request, "feedback/feedback_create.html", context)

