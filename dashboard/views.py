from django.shortcuts import render_to_response
from django.template import RequestContext
from base import dashboard

def overview(request):
    """
    Render the overview of the dashboard.
    
    Here you'll see the installed apps, the content management and the site
    administration panels. You'll also get plugins filled with information about
    the installed apps (eg: RSS feeds, approval queue, recent actions...)
    """
    apps = dashboard.get_apps_for_user(request.user)
    plugins = dashboard.get_plugins_for_apps(*apps)
    return render_to_response('dashboard/overview.html',
        {'apps': registered_apps,
         'plugins': plugins}, context_instance=RequestContext(request))