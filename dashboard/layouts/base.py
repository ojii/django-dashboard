from django.template.loader import render_to_string

class BaseLayout(object):
    uniqueid = 0
    def __init__(self, **kwargs):
        for key, arg in kwargs.items():
            setattr(self, key, arg)
        self.uniqueid = BaseLayout.uniqueid
        BaseLayout.uniqueid += 1
            
    @property
    def template(self):
        raise NotImplementedError(
            "A layout has to define a template attribute or override the "
            "render method.")
    
    @safe_deco
    def render(self, obj):
        return render_to_string(self.template, {'layout': self, 'object': obj})
    
    
class PlainLayout(BaseLayout):
    def render(self, obj):
        return obj