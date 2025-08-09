from django.shortcuts import render

def aboutMe(req):
   return render(req, 'about_me.html')
