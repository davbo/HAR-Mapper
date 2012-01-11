from models import HAR, Host
from django.shortcuts import get_object_or_404, render_to_response

def har_list(request):
    context = {'hars' : HAR.objects.all()}
    return render_to_response('har_list.html', context)

def har_map(request, id):
    har = get_object_or_404(HAR, id=id)
    context = {'har': har,
            'hosts': har.host_set.all(),
            }
    return render_to_response('har_map.html', context)
