from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Host,Backup
from datetime import datetime, timezone
import re
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core import serializers
from rest_framework.decorators import api_view, permission_classes
from .serializers import HostSerializer

def index(request):
    all_hosts =  Host.objects.all()
    d = []
    for h in all_hosts:
        t = {}
        b = []
        t['id']       = h.id
        t['hostname'] = h.host
        t['vendor']   = h.vendor
        t['backups']  = Backup.objects.filter(host_id=h.id)
        d.append(t)
    # data = HostSerializer(all_hosts, many=True).data[:]
    return render(request, 'dashboard/home.html', {'hosts': d})

def details(request, id):
    if request.method == 'GET':
        data = Backup.objects.filter(host_id=id)
        return render(request, 'dashboard/details.html', { 'backups': data})


@csrf_exempt
@api_view(["POST"])
def status(request):
    if request.method != 'POST':
        return HttpResponse('Ony POST verb is supported.', content_type="text/plain")

    if not request.POST.get('host'):
        return HttpResponse('value for "host" is missing', content_type="text/plain")

    if not request.POST.get('vendor'):
        return HttpResponse('value for "vendor" is missing', content_type="text/plain")

    if not request.POST.get('state'):
        return HttpResponse('value for "state" is missing', content_type="text/plain")

    h = request.POST.get('host')
    v = request.POST.get('vendor')
    st =  request.POST.get('state')

    if re.search(r'started', st, re.IGNORECASE):
        try:
            host = Host.objects.get(host=h)
            newbackup = Backup(state='started', start_time=datetime.now(tz=timezone.utc), host_id=host)
            newbackup.save()

            return HttpResponse(newbackup.id, content_type="text/plain")

        except Host.DoesNotExist:
            host = Host(host=h, vendor=v)
            host.save()
            newbackup = Backup(state='started', start_time=datetime.now(tz=timezone.utc), host_id=host)
            newbackup.save()

            return HttpResponse(newbackup.id, content_type="text/plain")

    if re.search(r'finished', st, re.IGNORECASE):

        if not request.POST.get('filename'):
            return HttpResponse('value for "filename" is missing', content_type="text/plain")

        if not request.POST.get('location'):
            return HttpResponse('value for "location" is missing', content_type="text/plain")

        if not request.POST.get('backup_id'):
            return HttpResponse('value for "backup_id" is missing', content_type="text/plain")

        try:
            backup = Backup.objects.get(id=request.POST.get('backup_id'))
        except Host.DoesNotExist:
            return HttpResponse('Backup instance not found', content_type="text/plain")

        backup.state = 'finished'
        backup.finish_time = datetime.now(tz=timezone.utc)
        duration = backup.finish_time - backup.start_time
        backup.duration = divmod(duration.total_seconds(), 60)[0]
        backup.filename = request.POST.get('filename')
        backup.location = request.POST.get('location')
        backup.save()

        return HttpResponse('OK', content_type="text/plain")
