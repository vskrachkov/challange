import datetime

from django.db import connection


class StudentsMiddleware:

    def process_request(self, request):
        self.request_time = datetime.datetime.now()

    def process_template_response(self, request, response):
        if 'text/html' in response['Content-Type']:
            response.context_data['dd'] = self.request_time
            response.context_data['sql_count'] = len(connection.queries)
        else:
            pass
        return response
