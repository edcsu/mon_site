from django.shortcuts import render, render_to_response

# Create your views here.
# name of function should be the name to be used in the url
# if this raquest is in the url, do....

def index(request):
    return render_to_response("firstapp/index.html")
 #appname/page
    # pass => if u dont want to do something