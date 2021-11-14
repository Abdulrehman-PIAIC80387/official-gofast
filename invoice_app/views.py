from django.shortcuts import render
from .forms import InvoiceForm
from .models import *
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
	"title": title,
	}
	return render(request, "home.html",context)


def add_invoice(request):
	form = InvoiceForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/list_invoice')
	context = {
		"form": form,
		"title": "New Invoice",
	}
	return render(request, "entry.html", context)

		
    



def list_invoice(request):
	title = 'List of Invoices'
	queryset = Invoice.objects.all()
	context = {
		"title": title,
		"queryset": queryset,
	}
	return render(request, "list_invoice.html", context)    
	