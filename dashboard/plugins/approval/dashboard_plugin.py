from dashboard.plugin import BasePlugin
from dashboard.layouts import ListLayout, BinarySwitchLayout


class ApprovalPlugin(BasePlugin):
    """
    A plugin managing 'approval queues'. Useful for moderation.
    """
    
    # Each plugin requires a 'layout' attribute. This handles how a plugin is
    # rendered on a page. Writing plugins should involve as little HTML/CSS/JS
    # as possible, thus there are a couple of built-in layout classes.
    # A ListLayout simply displays a list (with a given length) of items. It
    # renders each item using the layout defined in item_layout.
    layout = ListLayout(
        # Amount of items to display
        item_count=5,
        # Layout to render the items with
        # A BinarySwitchLayout displays the name of an item as well as two
        # buttons you can press.
        item_layout=BinarySwitchLayout(
            # Text to display for the 'good' icon
            true_text='Approve',
            # Text to display for the 'bad' icon
            false_text='Delete',
            # Set the name of the POST argument to store the result in
            argument='approved'
        ),
    )
    
    def __init__(self, approve_attr_name='approved', approved_value=True,
            disapprove_attr_name='approved', disapprove_value=False,
            delete=True, description=lambda obj: unicode(obj)):
        self.approve_attr_name = approve_attr_name
        self.approved_value = approved_value
        self.disapprove_attr_name = disapprove_attr_name
        self.disapprove_value = disapprove_value
        self.delete = delete
        self.layout.item_layout.description = description
        
    def handle_post(self, object, post):
        """
        Handle a post request
        """
        if post[self.layout.item_layout.argument_name] == '1':
            setattr(object, self.approve_attr_name, self.approved_value)
        elif self.delete:
            object.delete()
        else:
            setattr(object, self.disapprove_attr_name, self.disapprove_value)
            
    def get_object(self, model):
        """
        Get the object for a model to render
        """
        return model.objects.exclude(**{self.approve_attr_name:self.approved_value})