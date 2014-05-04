from flask.ext.admin import Admin, BaseView, expose

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin_home.html')


def add_admin_views(admin):
  admin.add_view(MyView(name='Hello'))