from django.http import HttpResponse, Http404
import datetime
def hello(request):
	return HttpResponse("Hello world")

def time(request):
	now = str(datetime.datetime.now())
	html = "<html><center><b>.%s.</b></center></html>" %now
	return HttpResponse(html)	

def newtime(request, offset):
		try:
			offset = int(offset)
		except:
			raise Http404()
		dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
		html = "<html><center><b> In %s hours, the time will be %s</b></center></html>" %(offset, dt)	
		return HttpResponse(html)