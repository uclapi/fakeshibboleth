from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fakeshibboleth.helpers import redirect_params

import os


def shibboleth(request):
    callback = request.GET["target"]

    context = {
        "callback": callback
    }
    return render(request, "core/shibboleth.html", context)

@csrf_exempt
def auto_shibboleth(request):
    callback = request.GET["target"]
    
    params={
        'eppn': os.environ.get("AUTO_EPPN"),
        'uclIntranetGroups': os.environ.get("AUTO_UCLINTRANETGROUPS"),
        'cn': os.environ.get("AUTO_CN"),
        'department': os.environ.get("AUTO_DEPARTMENT"),
        'givenName': os.environ.get("AUTO_GIVENNAME"),
        'displayName': os.environ.get("AUTO_DISPLAYNAME"),
        'employeeID': os.environ.get("AUTO_EMPLOYEEID"),
        'affiliation': os.environ.get("AUTO_AFFILIATION"),
        'mail': os.environ.get("AUTO_MAIL"),
        'sn': os.environ.get("AUTO_SN"),
        'unscoped_affiliation': os.environ.get("AUTO_UNSCOPED_AFFILIATION"),
        'convert-get-headers': "1"
    }

    return redirect_params(callback, params)
