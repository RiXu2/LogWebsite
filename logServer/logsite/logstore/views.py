from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Log


# Create your views here.
def all_log(request):
    all_log = Log.objects.filter(is_active=True)
    return render(request, 'logstore/all_log.html', locals())


def update_log(request, log_id):

    try:
        log = Log.objects.get(id=log_id, is_active=True)
    except Exception as e:
        print('--update log error is %s'%(e))
        return HttpResponse('--The log is not existed.')

    if request.method == 'GET':

        return render(request, 'logstore/update_log.html', locals())
    elif request.method == 'POST':
        info = request.POST['info']
        log.info = info
        log.save()
        return HttpResponseRedirect('/logstore/all_log')


def delete_log(request):
    log_id = request.GET.get('log_id')
    if not log_id:
        return HttpResponse('--请求异常')
    try:
        log = Log.objects.get(id=log_id, is_active=True)
    except Exception as e:
        print('--delete log error is %s' % (e))
        return HttpResponse('--The log id is error.')

    log.is_active = False
    log.save()
    return HttpResponseRedirect('/logstore/all_log')
