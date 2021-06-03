from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import re


class MyMw(MiddlewareMixin):

    def process_request(self, request):
        print('MyMw process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMw process_views do ---')

    def process_response(self, request, response):
        print('MyMw process_response do ---')
        return response


class MyMw2(MiddlewareMixin):

    def process_request(self, request):
        print('MyMw2 process_request do ---')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMw2 process_views do ---')

    def process_response(self, request, response):
        print('MyMw2 process_response do ---')
        return response


class VisitLimit(MiddlewareMixin):
    visit_times = {}

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match('^/test', path_url):
            return
        times = self.visit_times.get(ip_address, 0)
        print('ip', ip_address, 'already be viewed', times)
        self.visit_times[ip_address] = times + 1
        if times < 5:
            return
        return HttpResponse('You have already viewed this page ' + str(times) + ' times')
