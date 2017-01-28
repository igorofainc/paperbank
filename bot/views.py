from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.

def main(request):
    """
    Main endpoint for communications
    """
    print "Got message from messenger: %s" % request.POST # This should be logging
    token = request.POST.get('verify_token', '')
    print "The token is: %s" % token 
    return HttpResponse(token)

    if request.POST.get('verify_token', '') == 'Verification_string_will be here':
        print "Receiving data from facebook"
        data = {'challenge': request.POST['challenge']}
        return JsonResponse(data)

    return False
