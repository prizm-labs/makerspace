
import os
from flask.ext.openid import OpenID
from config import basedir


from flask.ext import admin, login

from flask import render_template, request, jsonify, flash, redirect, session, url_for, g

from flask.ext.admin import Admin, expose, AdminIndexView, BaseView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import login_user, logout_user, current_user, login_required


from . import db
from . import app

import models
import forms


oid = OpenID(app, os.path.join(basedir, 'tmp'))

def init_admin():
    app_admin = Admin(app, 'Admin', index_view=MyAdminIndexView(), base_template='admin/master.html')
    add_admin_views(app_admin)
    return app_admin

def isUserAdmin():
    isAdmin = False
    if (current_user.is_authenticated() and current_user.role==models.ROLE_ADMIN):
        isAdmin = True
    return isAdmin

@app.before_request
def before_request():
    g.user = current_user


# https://github.com/mrjoes/flask-admin/blob/master/examples/auth/auth.py

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not isUserAdmin():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods = ['GET', 'POST'])
    @oid.loginhandler
    def login_view(self):

        form = forms.OpenIdLoginForm()

        if form.validate_on_submit():
            session['remember_me'] = form.remember_me.data
            return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])

        if isUserAdmin():
            return redirect(url_for('.index'))

        #link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        link = 'link to register'
        self._template_args['form'] = form
        self._template_args['link'] = link
        self._template_args['title'] = 'Sign In'
        self._template_args['providers'] = app.config['OPENID_PROVIDERS']

        return super(MyAdminIndexView, self).index()


    @oid.after_login
    def after_login(resp):
        if resp.email is None or resp.email == "":
            flash('Invalid login. Please try again.')
            return redirect(url_for('.login_view'))
        user = db.session.query(models.Maker).filter_by(email = resp.email).first()
        if user is None:
            nickname = resp.nickname
            if nickname is None or nickname == "":
                nickname = resp.email.split('@')[0]
            user = models.Maker(nickname = nickname, email = resp.email, role = models.ROLE_USER)
            db.session.add(user)
            db.session.commit()
        remember_me = False
        if 'remember_me' in session:
            remember_me = session['remember_me']
            session.pop('remember_me', None)
        login_user(user, remember = remember_me)

        return redirect(url_for('.index'))

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# customize model before rendered
# https://flask-admin.readthedocs.org/en/latest/api/mod_contrib_sqla/#module-flask.ext.admin.contrib.sqla
# class ModelView(model, session, name=None, category=None, endpoint=None, url=None)

class MyModelView(ModelView):
    def is_accessible(self):
        return isUserAdmin()

class ProjectView(MyModelView):
    list_template = 'admin/project_list.html'
    #edit_template = 'my_edit_template.html'
    #create_template = 'create.html'
    column_display_all_relations = True


def add_admin_views(admin):
  admin.add_view(ProjectView(models.Project, db.session))
  admin.add_view(MyModelView(models.Video, db.session))
  admin.add_view(MyModelView(models.Tag, db.session))
  admin.add_view(MyModelView(models.Meta, db.session))
  admin.add_view(MyModelView(models.Page, db.session))
  admin.add_view(MyModelView(models.Maker, db.session))
