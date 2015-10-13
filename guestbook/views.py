from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.template import RequestContext, loader
from django.utils import timezone
from .models import text



def index(request):
    latest_question_list = text.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    try:
        title=request.POST['nafn']
        texti1=request.POST['færsla']
    except(KeyError):
        pass
    else:
        f = text(question_text=texti1, pub_date=timezone.now(),title_text=title)
        f.save()
    return render(request, 'guestbook/index.html', context)



def detail(request, question_id):
    question = get_object_or_404(text, pk=question_id)
    return render(request, 'guestbook/detail.html', {'question': question})



"""
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""
