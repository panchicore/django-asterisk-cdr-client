class CommonMiddleware:
    def process_request(self, request):
        request.database = request.session.get('DB', 'default')
  