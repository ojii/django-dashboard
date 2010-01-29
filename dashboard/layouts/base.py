from django.template.loader import render_to_string

class BaseLayout(object):
    @property
    def template(self):
        raise NotImplementedError(
            "A layout has to define a template attribute or override the "
            "render method.")
        
    def render(self, obj):
        return render_to_string(self.template, {'layout': self, 'object': obj})
    
    
class ListLayout(BaseLayout):
    template = 'dashboard/layouts/list.html'
    
    def __init__(self, item_count, item_layout):
        self.item_count = item_count
        self.item_layout = item_layout
        
    def render(self, obj):
        return super(ListLayout, self).render(obj[:self.item_count])
    
    
class BinarySwitchLayout(BaseLayout):
    template = 'dashboard/layouts/binaryswitch.html'
    
    def __init__(self, true_text='Approve', false_text='Disapprove',
        argument='binary_switch_approve', description=lambda obj: unicode(obj)):
        self.true_text = true_text
        self.false_text = false_text
        self.argument = argument
        self.description = description