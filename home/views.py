from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command

def migrate_view(request):
    try:
        call_command('migrate')
        return HttpResponse("✅ Migration tamamlandı.")
    except Exception as e:
        return HttpResponse(f"❌ Migration hatası: {str(e)}")

def homePage(req):
    return render(req, 'index.html')
