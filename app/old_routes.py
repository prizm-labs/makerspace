from . import app
from flask import render_template

import forms
import sample_data

'''
@app.route('/')
def index():
    return render_template('index.html')
'''

@app.route('/page_home1')
def page_home1():
    return render_template('page_home1.html')


@app.route('/page_home2')
def page_home2():
    return render_template('page_home2.html')


@app.route('/page_home3')
def page_home3():
    return render_template('page_home3.html')


@app.route('/page_home4')
def page_home4():
    return render_template('page_home4.html')


@app.route('/page_home5')
def page_home5():
    return render_template('page_home5.html')


@app.route('/page_home6')
def page_home6():
    return render_template('page_home6.html')


@app.route('/page_home7')
def page_home7():
    return render_template('page_home7.html')


@app.route('/page_about')
def page_about():
    return render_template('page_about.html')


@app.route('/page_about1')
def page_about1():
    return render_template('page_about1.html')


@app.route('/page_services')
def page_services():
    return render_template('page_services.html')


@app.route('/page_services1')
def page_services1():
    return render_template('page_services1.html')


@app.route('/page_pricing')
def page_pricing():
    return render_template('page_pricing.html')


@app.route('/page_invoice')
def page_invoice():
    return render_template('page_invoice.html', invoice=sample_data.invoice)


@app.route('/page_meet_our_team')
def page_meet_our_team():
    return render_template('page_meet_our_team.html')


@app.route('/page_coming_soon')
def page_coming_soon():
    return render_template('page_coming_soon.html')


@app.route('/page_faq')
def page_faq():
    return render_template('page_faq.html')


@app.route('/page_funny_boxes')
def page_funny_boxes():
    return render_template('page_funny_boxes.html')


@app.route('/page_gallery')
def page_gallery():
    return render_template('page_gallery.html')


@app.route('/page_registration')
def page_registration():
    return render_template('page_registration.html', form=forms.RegisterForm())


@app.route('/page_registration1')
def page_registration1():
    return render_template('page_registration1.html', form=forms.RegisterForm())


@app.route('/page_login')
def page_login():
    return render_template('page_login.html', form=forms.LoginForm())


@app.route('/page_login1')
def page_login1():
    return render_template('page_login1.html', form=forms.LoginForm())


@app.route('/page_404_error')
def page_404_error():
    return render_template('page_404_error.html')


@app.route('/page_404_error1')
def page_404_error1():
    return render_template('page_404_error1.html')


@app.route('/page_clients')
def page_clients():
    return render_template('page_clients.html')


@app.route('/page_privacy')
def page_privacy():
    return render_template('page_privacy.html')


@app.route('/page_terms')
def page_terms():
    return render_template('page_terms.html')


@app.route('/page_2_columns_left')
def page_2_columns_left():
    return render_template('page_2_columns_left.html')


@app.route('/page_2_columns_right')
def page_2_columns_right():
    return render_template('page_2_columns_right.html')


@app.route('/page_3_columns')
def page_3_columns():
    return render_template('page_3_columns.html')


@app.route('/feature_grid')
def feature_grid():
    return render_template('feature_grid.html')


@app.route('/feature_boxes')
def feature_boxes():
    return render_template('feature_boxes.html')


@app.route('/feature_typography')
def feature_typography():
    return render_template('feature_typography.html')


@app.route('/feature_tagline_boxes')
def feature_tagline_boxes():
    return render_template('feature_tagline_boxes.html')


@app.route('/feature_buttons')
def feature_buttons():
    return render_template('feature_buttons.html')


@app.route('/feature_icons')
def feature_icons():
    return render_template('feature_icons.html')


@app.route('/feature_thumbnails')
def feature_thumbnails():
    return render_template('feature_thumbnails.html')


@app.route('/feature_components')
def feature_components():
    return render_template('feature_components.html')


@app.route('/feature_accordion_and_tabs')
def feature_accordion_and_tabs():
    return render_template('feature_accordion_and_tabs.html')


@app.route('/feature_navigations')
def feature_navigations():
    return render_template('feature_navigations.html')


@app.route('/feature_tables')
def feature_tables():
    return render_template('feature_tables.html', users=sample_data.users)


@app.route('/feature_forms')
def feature_forms():
    return render_template('feature_forms.html', form=forms.LoginForm())


@app.route('/feature_testimonials')
def feature_testimonials():
    return render_template('feature_testimonials.html')


@app.route('/portfolio_text_blocks')
def portfolio_text_blocks():
    return render_template('portfolio_text_blocks.html')


@app.route('/portfolio_2_column')
def portfolio_2_column():
    return render_template('portfolio_2_column.html')


@app.route('/portfolio_3_column')
def portfolio_3_column():
    return render_template('portfolio_3_column.html')


@app.route('/portfolio_4_column')
def portfolio_4_column():
    return render_template('portfolio_4_column.html')


@app.route('/portfolio_item')
def portfolio_item():
    return render_template('portfolio_item.html')


@app.route('/portfolio_item1')
def portfolio_item1():
    return render_template('portfolio_item1.html')


@app.route('/page_contact1')
def page_contact1():
    return render_template('page_contact1.html', form=forms.ContactForm())


@app.route('/page_contact2')
def page_contact2():
    return render_template('page_contact2.html', form=forms.ContactForm())


@app.route('/page_contact3')
def page_contact3():
    return render_template('page_contact3.html', form=forms.ContactForm())


@app.route('/blog_page')
def blog_page():
    return render_template('blog_page.html')


@app.route('/blog_large')
def blog_large():
    context_dict = {
        'blog_posts': sample_data.blog_posts[:3],
        'tags': sample_data.tags,
    }
    return render_template('blog_large.html', **context_dict)


@app.route('/blog_medium')
def blog_medium():
    context_dict = {
        'blog_posts': sample_data.blog_posts[3:7],
        'tags': sample_data.tags,
    }
    return render_template('blog_medium.html', **context_dict)


@app.route('/blog_full_width')
def blog_full_width():
    context_dict = {
        'blog_posts': sample_data.blog_posts[7:],
        'tags': sample_data.tags,
    }
    return render_template('blog_full_width.html', **context_dict)


@app.route('/blog_left_sidebar')
def blog_left_sidebar():
    context_dict = {
        'blog_posts': sample_data.blog_posts2,
    }
    return render_template('blog_left_sidebar.html', **context_dict)


@app.route('/blog_right_sidebar')
def blog_right_sidebar():
    context_dict = {
        'blog_posts': sample_data.blog_posts2,
    }
    return render_template('blog_right_sidebar.html', **context_dict)


@app.route('/blog_item_option1')
def blog_item_option1():
    context_dict = {
        'blog_post': sample_data.blog_posts[0],
        'comments': sample_data.comments,
        'comment_form': forms.BlogCommentForm(),
    }
    return render_template('blog_item_option1.html', **context_dict)


@app.route('/blog_item_option2')
def blog_item_option2():
    context_dict = {
        'blog_post': sample_data.blog_posts[7],
        'comments': sample_data.comments,
        'comment_form': forms.BlogCommentForm(),
    }
    return render_template('blog_item_option2.html', **context_dict)
