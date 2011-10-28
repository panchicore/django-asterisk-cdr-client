def common(request):
    return {'DB': request.session.get('DB', 'default')  }