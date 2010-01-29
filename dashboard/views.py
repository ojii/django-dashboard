from django.shortcuts import render_to_response
from django.template import RequestContext
from manager import manager

def overview(request):
    """
    Render the overview of the dashboard.
    
    Here you'll see the installed apps, the content management and the site
    administration panels. You'll also get plugins filled with information about
    the installed apps (eg: RSS feeds, approval queue, recent actions...)
    """
    registered_apps = manager.get_registered_apps()
    return render_to_response('dashboard/overview.html',
        {'apps': registered_apps}, context_instance=RequestContext(request))