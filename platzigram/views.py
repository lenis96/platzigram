from django.http import HttpResponse
from datetime import datetime
import json

def helloWorld(request):
    return HttpResponse('Oh, hi Current server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sorted(request):
    # return HttpResponse(','.join(list(map(lambda x:str(x),sorted(list(map(lambda x:int(x),str(numbers).split(','))))))))
    numbers=[int(i) for i in request.GET['numbers'].split(',')]
    numbers.sort()
    data={
        'status':'ok',
        'numbers':numbers,
        'message':'numbers sorted successfully'
    }
    return HttpResponse(json.dumps(data),content_type="application/json")
def sayHi(request,name,age):
    if(age<12):
        message="Sorry {}, you are not allowd here.".format(name)
    else:
        message="Hellow, {} Welcome to Platzigram".format(name)
    return HttpResponse(message)

