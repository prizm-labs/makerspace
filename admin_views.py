from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('_admin_home.html')


# customize model before rendered
# https://flask-admin.readthedocs.org/en/latest/api/mod_contrib_sqla/#module-flask.ext.admin.contrib.sqla
# class ModelView(model, session, name=None, category=None, endpoint=None, url=None)

class ProjectView(ModelView):
    list_template = 'admin/project_list.html'
    #edit_template = 'my_edit_template.html'
    #create_template = 'create.html'

    column_display_all_relations = True


def add_admin_views(admin,models,db):
  admin.add_view(MyView(name='Hello'))

  admin.add_view(ProjectView(models.Project, db.session))
  admin.add_view(ModelView(models.Page, db.session))
  admin.add_view(ModelView(models.User, db.session))