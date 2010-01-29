"""
Api Draft:

-cms/
	-models.py
	-urls.py
	-views.py
	-dashboard.py (!)
"""

#===============================================================================
# dashboard.py:
#===============================================================================

from dashboard import register, ApplicationDashboard, ModelDashboard
from dashboard.plugins.news import NewsPlugin
from dashboard.plugins.approval import ApprovalPlugin
from cms.models import Page

class PageDashboard(ModelDashboard):
	# set the correct model
	model = Page
	
	plugins = (
		# Enables 'quick moderation' for cms pages.
		ApprovalPlugin(
			approve_attr_name='moderator_state',
			approved_value=10,
			disapprove_attr_name='moderator_state',
			disapprove_value=2,
			delete=False,
			display=lambda obj: '%s by %s'  % (obj.get_page_title(), obj.changed_by),
		),
	)
	
	def check_permission(self, user, object, plugin):
		# check the permission of a user for a plugin
		return True


class CMSDashboard(ApplicationDashboard):
	"""
	An ApplicationDashboard subclass handles the dashboard for a specific app.
	This would be for example django-cms or django-satchmo.
	"""
	# Quick action is displayed next to the app name on the main dashboard.
	# It usually is an 'add your-main-model'.
	quick_action = (add_page, _('Add Page'))
	# extra actions are the dropdown actions next to the 'add new ...'
	extra_actions = []
	# plug in any models in this app we would like to manage with the dashboard
	managed = [PageDashboard]
	
	plugins = (
		# Plugs the django-cms news feed into the dashboard.
		NewsPlugin(url='http://www.django-cms.org/blog/feed/', ttl=60),
		# Plugs the django-cms documetation into the dashboard
		DocumentationPlugin(docs=[('IRC Channel', 'irc://irc.freenode.net/#django-cms'),
								  ('Documentation', 'http://www.django-cms.org/en/documentation/')])
	)


register(CMSDashboard)