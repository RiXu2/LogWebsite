import os
import shutil
import time
import csv

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, Http404
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_GET

from django.core.files import File
from upload_app.models import Content
import os


@cache_page(15)
def test_cache(request):
    t = time.time()
    return HttpResponse('t is %s' % (t))


def test_mw(request):
    print('---test Mw view in ----')
    return HttpResponse('---test--mw---')


def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('---test post is okay')


def test_page(request):
    page_num = request.GET.get('page', 1)
    # 模拟一下 后面改
    all_data = ['a', 'b', 'c', 'd', 'e']
    # Paginator(all data, data number per page)
    paginator = Paginator(all_data, 2)
    c_page = paginator.page(int(page_num))
    return render(request, 'test_page.html', locals())


def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="test.csv"'
    # 模拟一下 后面改
    all_data = ['a', 'b', 'c', 'd', 'e']
    writer = csv.writer(response)
    writer.writerow(all_data)
    return response


def make_page_csv(request):
    page_num = request.GET.get('page', 1)
    # 模拟一下 后面改
    all_data = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(all_data, 2)
    c_page = paginator.page(int(page_num))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="page-%s.csv"' % (page_num)
    writer = csv.writer(response)
    for b in c_page:
        writer.writerow([b])
    return response


def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == 'POST':
        title = request.POST['title']
        myfile = request.FILES['myfile']

        Content.objects.create(title=title, picture=myfile)
        return HttpResponseRedirect('/all_content')


root_dir = "/Users/liuxuri/Desktop/LogWebsite/logServer/tempsavesite/tempsave/tempsave/tempUpload"
move_dir = "/Users/liuxuri/Desktop/LogWebsite/logServer/tempsavesite/tempsave/tempsave/tempUpload/"
move_dest_dir = "/Users/liuxuri/Desktop/LogWebsite/logServer/tempsavesite/tempsave/media/file/"


def upload_local():
    if not os.listdir(root_dir):
        pass
    else:
        if os.path.isdir(root_dir):
            for p in os.listdir(root_dir):
                title = "local_UpFile"
                myfile = "file/"+p
                Content.objects.create(title=title, picture=myfile)
            for p in os.listdir(root_dir):
                shutil.move(move_dir + p, move_dest_dir + p)
        else:
            print('又有哪儿奇奇怪怪的错了')


def all_content(request):
    upload_local()
    all_content = Content.objects.filter(is_active=True)
    return render(request, 'all_content.html', locals())


def delete_content(request):
    content_id = request.GET.get('content_id')
    if not content_id:
        return HttpResponse('--请求异常')
    try:
        content = Content.objects.get(id=content_id, is_active=True)
    except Exception as e:
        print('--delete log error is %s' % (e))
        return HttpResponse('--The log id is error.')

    content.is_active = False
    content.save()
    return HttpResponseRedirect('/all_content')


def update_content(request, content_id):
    try:
        content = Content.objects.get(id=content_id, is_active=True)
    except Exception as e:
        print('--update log error is %s' % (e))
        return HttpResponse('--The log is not existed.')

    if request.method == 'GET':

        return render(request, 'update_content.html', locals())
    elif request.method == 'POST':
        title = request.POST['title']
        content.title = title
        content.save()
        return HttpResponseRedirect('/all_content')


def file_response_download(request, file_path):
    ext = os.path.basename(file_path).split('.')[-1].lower()
    # cannot be used to download py, db and sqlite3 files.
    if ext not in ['py', 'db', 'sqlite3']:
        response = FileResponse(open(file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        raise Http404
