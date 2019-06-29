from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, authenticate
from django.urls import reverse
from django.shortcuts import redirect, resolve_url, render_to_response, render
from django.template.response import TemplateResponse
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
import datetime
def index(request):
	try:
		if request.user.is_authenticated:
			time=datetime.datetime.now()
			return render(request, 'home', {'time': time})
		else:
			return redirect("sales/login/")
	except Exception as e:
		return redirect("sales/login/")

@csrf_protect
@never_cache
@login_required
def sales_dashboard(request):
	result="hi weafasfasfafsasflcome"
	try:
		print(result)
	except Exception as e:
		print(e)
	return render(request, "sales_dashboard.html", {'result': result})
    