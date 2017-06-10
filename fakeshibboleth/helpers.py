from urllib.parse import urlencode
from django.shortcuts import redirect

def redirect_params(url, params=None):
    response = redirect(url)
    if params:
        query = urlencode(params)
        response['Location'] += '?' + query
    return response