from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('_admin_home.html')


def add_admin_views(admin,models,db):
  admin.add_view(MyView(name='Hello'))
  admin.add_view(ModelView(models.Project, db.session))
  admin.add_view(ModelView(models.Page, db.session))