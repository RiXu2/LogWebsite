from django.http import HttpResponse
from django.shortcuts import render


def test_static(request):
    return render(request, 'test_static.html')


def set_cookies(request):
    resp = HttpResponse('set cookies is ok')
    resp.set_cookie('uuname', 'lxr', 500)
    return resp


def get_cookies(request):
    value = request.COOKIES.get('uuname')
    return HttpResponse('value is %s'%(value))


def set_session(request):
    request.session['uname'] = 'cyp'
    return HttpResponse('set session is ok')


def get_session(request):
    value = request.session['uname']
    return HttpResponse('session value is %s'%(value))
