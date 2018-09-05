from django.shortcuts import render

def home(request):
	return render(request,'home.html',{})


#def  base(request):
	#return render(request,'base.html',{})

def about(request):
	first_name = "john"
	last_name="legend"
	context = {'first_name' : first_name,'last_name' : last_name}
	return render(request,'about.html',context)