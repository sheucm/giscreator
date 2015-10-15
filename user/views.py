from django.shortcuts import render
from django.http import HttpResponse
from user.models import Gis
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json

def gis_index(request):
    return render(request, 'index.html')

# Create your views here.
@csrf_exempt
def gis(request):
	if request.method == 'POST':
		lat = request.POST.get('lat','')
		lon = request.POST.get('lon','')
		item = request.POST.get('item','')

		if __is_float(lat) != True or __is_float(lon) != True or len(item) == 0:
			return HttpResponse(status=400)
		# Check duplicate of gis
		if len(Gis.objects.filter(item=item, lon=lon, lat=lat)) > 0:
			return HttpResponse(status=400)
		record = Gis(item=item, lat=lat, lon=lon)
		record.save()
		return HttpResponse(status=200)

	elif request.method == 'GET':
		gisObs = Gis.objects.all()
		response_data = list()
		for gisOb in gisObs:
			gis_data = model_to_dict(gisOb)
			response_data.append(gis_data)
		return HttpResponse(json.dumps(response_data), status=200, content_type="application/json")
	else:
		return	HttpResponse(status=400)


def __is_float(s):
	try:
		float(s)
		return True
	except ValueError:
		return False
