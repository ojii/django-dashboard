class DashboardAppManager(object):
    def __init__(self):
        self.registered_apps = []
        self.ordered = True
        
    def register(self, app, dashboard):
        self.registered_apps.append(dashboard(app))
        self.ordered = False
        
    def get_registered_apps(self):
        if not self.ordered:
            self.registered_apps = sorted(self.registered_apps, key=lambda db: db.app_name)
        return self.registered_apps
    
    
manager = DashboardAppManager()