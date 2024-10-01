import time
import datetime
import logging
from django.shortcuts import redirect


logging.basicConfig(filename='request_logs.txt', level=logging.INFO)

class PostCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        if not request.user.is_authenticated and request.path != '/login/':
            return redirect('login')

        user_ip = self.get_client_ip(request)
        print(f'IP пользователя: {user_ip}')

        response = self.get_response(request)

        if request.user.is_authenticated and request.user.is_superuser:
            response.set_cookie('admin_user', 'True')

        execution_time = (time.time() - start_time) * 1000
        logging.info(f'{request.path} выполнен за {execution_time:.2f} мс пользователем {request.user}, IP {user_ip}')

        return response

    def process_exception(self, request, exception):
        error_time = datetime.datetime.now()
        user_info = request.user if request.user.is_authenticated else 'Anonymous'
        logging.error(f'Ошибка {exception} у пользователя {user_info} в {error_time}')
        return None

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
