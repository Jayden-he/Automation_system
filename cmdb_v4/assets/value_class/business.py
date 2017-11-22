from django.shortcuts import render,HttpResponse,render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
# Create your views here.

@login_required
def auth_server_type_list(request):
	return render(request,'assets/server_type_list.html')	
	
	
	