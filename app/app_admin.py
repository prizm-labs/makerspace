
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
    #app_admin = Admin(app)
    app_admin = Admin(app, 'Admin', index_view=MyAdminIndexView(), base_template='admin/master.html')
    # admin = admin.Admin(app, 'Auth', index_view=MyAdminIndexView(), base_template='my_master.html')
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

'''
class MyView(BaseView):
    def is_accessible(self):
        return login.current_user.is_authenticated()
'''

class MyAdminIndexView(AdminIndexView):
    #@login_required
    @expose('/')
    def index(self):
        if not isUserAdmin():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods = ['GET', 'POST'])
    @oid.loginhandler
    def login_view(self):
        '''
        print g.user
        if g.user is not None and g.user.is_authenticated():
            if g.user.role == models.ROLE_ADMIN:
                return redirect('/admin')
            else:
                return redirect('/')
                '''
        '''
        form = forms.OpenIdLoginForm()
        if form.validate_on_submit():
            session['remember_me'] = form.remember_me.data
            return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
        return render_template('_login.html', 
            title = 'Sign In',
            form = form,
            providers = app.config['OPENID_PROVIDERS'])
        '''
        # handle user login
        #form = LoginForm(request.form)
        form = forms.OpenIdLoginForm()

        if form.validate_on_submit():
            session['remember_me'] = form.remember_me.data
            return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
        ''''
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)
        '''
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
        user = db.session.query(models.User).filter_by(email = resp.email).first()
        if user is None:
            nickname = resp.nickname
            if nickname is None or nickname == "":
                nickname = resp.email.split('@')[0]
            user = models.User(nickname = nickname, email = resp.email, role = models.ROLE_USER)
            db.session.add(user)
            db.session.commit()
        remember_me = False
        if 'remember_me' in session:
            remember_me = session['remember_me']
            session.pop('remember_me', None)
        login_user(user, remember = remember_me)

        #return redirect(request.args.get('next') or url_for('index'))
        return redirect(url_for('.index'))

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
'''
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
'''

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
  #admin.add_view(MyView(name='Hello'))

  admin.add_view(ProjectView(models.Project, db.session))
  admin.add_view(MyModelView(models.Page, db.session))
  admin.add_view(MyModelView(models.User, db.session))

  ####
  #https://github.com/mrjoes/flask-admin/blob/master/examples/auth/auth.py
'''
import os
from flask import Flask, url_for, redirect, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators
from flask.ext import admin, login
from flask.ext.admin.contrib import sqla
from flask.ext.admin import helpers, expose


  # Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    login = fields.TextField(validators=[validators.required()])
    email = fields.TextField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated()


# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated():
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Auth', index_view=MyAdminIndexView(), base_template='my_master.html')

# Add view
admin.add_view(MyModelView(User, db.session))

'''