from django.shortcuts import render,redirect

from . import models
import random
# Create your views here.
def createOrJoinPoll(request):
    
    if request.method=='POST':
        code = request.POST.get('code')
        poll = None
        try:
            poll = models.Poll.objects.get(code=code)
        except Exception as e:
            print(e) 
        if poll:    
            s = poll.slug
            return redirect(f'/poll/{s}/')
        else:
            print('querry not found')
    return render(request,'index.html')

def givePoll(request, slug):
    poll = models.Poll.objects.get(slug=slug)
    options = models.Option.objects.all().filter(poll=poll)
    if request.method=='POST':
        selected_option = request.POST.get('option')
        if selected_option:
            try:
                option = models.Option.objects.get(option=selected_option)
                op = models.Response.objects.create(poll=poll, Option=option)
                op.save()
            except Exception as e:
                print(e)
            return redirect('create_join_poll')
    return render(request,'poll.html', {'poll':poll, 'options': options})


def poll_list(request):
    poll = models.Poll.objects.filter(open=True)
    data={
        'data' : poll
    }
    return render(request,'ongoingevent.html', data)

def createPollName(request):
    if request.method=='POST':
        poll_name = request.POST.get('poll_name')
        creator = request.POST.get('creator')
        try:
            poll = models.Poll.objects.create(poll_name=poll_name, creator = creator)
            poll.save()
            return redirect(f'/create-options/{poll.slug}/')
        except Exception as e:
            print(e)
            
    return render(request , 'enterpollname.html')

def addoptionsToPoll(request, slug):
    poll = models.Poll.objects.get(slug=slug)
    data = {
        'poll_name' : poll.poll_name
    }
    if request.method=='POST':
        options = request.POST.getlist('options[]') 
        alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        random_string = ''.join(random.choices(alphabet, k=4))
        
        for i  in options:
            if i != '':
                data = models.Option.objects.create(poll = poll, option = i)
                data.save()
        poll.open=True
        poll.code= random_string
        poll.save()
        return redirect('created', slug=slug )

    return render(request , 'createoptions.html', data)


def created(request, slug):
    poll = models.Poll.objects.get(slug=slug)
    data = {
        'code' : poll.code,
        'slug' : poll.slug,
        
    }
    return render(request, 'code.html', data)
