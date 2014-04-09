"""
Contains sample data to populate the templates.
"""

import datetime


TEXT_SNIPPET = """<p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut non libero consectetur adipiscing elit magna. Sed et quam lacus. Fusce condimentum eleifend enim a feugiat. Pellentesque viverra vehicula sem ut volutpat. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut non libero magna. Sed et quam lacus. Fusce condimentum eleifend enim a feugiat.</p>"""


class BlogPost(object):
    """ Model for a blog post. """
    description = TEXT_SNIPPET
    content = TEXT_SNIPPET * 4
    comments_count = 24
    tags = "Technology, Education, Media".split(',')

    def __init__(self, title, date, author, comments, type_, header):
        self.title = title
        self.date = date
        self.author = author
        self.comments = comments
        self.type = type_
        self.header = header


class BlogComment(object):
    """
    Model for a blog comment.

    A list of BlogComment objects can be assigned to the children property.
    """
    comment = "Donec id elit non mi portas sats eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna.."

    def __init__(self, name, avatar, time_delta, children=[]):
        self.name = name
        self.avatar = avatar
        self.time_delta = time_delta
        self.children = children


class InvoiceItem(object):
    """ Model for an item on the invoice. """
    def __init__(self, name, description, quantity, unit_cost):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.unit_cost = unit_cost

    @property
    def total(self):
        return self.quantity * self.unit_cost


class Invoice(object):
    """ Model for an Invoice. """
    discount = 14.8
    vat_percent = 6.0

    def __init__(self, items):
        self.items = items

    @property
    def sub_total(self):
        return float(sum([x.total for x in self.items]))

    @property
    def discounted_price(self):
        return self.sub_total * (100 - self.discount)/100

    @property
    def vat(self):
        return (self.vat_percent/100) * self.discounted_price

    @property
    def grand_total(self):
        return self.discounted_price + self.vat


class User(object):
    """ Model for a user. """
    def __init__(self, first_name, last_name, username, status, label_class, icon_class, icon):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.status = status
        self.label_class = label_class
        self.icon_class = icon_class
        self.icon = icon

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name


invoice_items = [
    InvoiceItem('Keyboard', 'At vero eos et accusamus etofficia mollitia', 252, 52),
    InvoiceItem('Displays', 'Verode eoset accusamus etofficia deserunt', 78, 128),
    InvoiceItem('Phones', 'Etquas molestias deexcepturi dasint', 16, 450),
    InvoiceItem('Software', 'Atofficia droeos etofficia taccusamus', 191, 24),
    InvoiceItem('Speakers', 'Dacusamus deserunt veroeoset vero eos', 65, 119),
    InvoiceItem('Hardware', 'Praesentium voluptatum deleniti atque', 1025, 63),
]

invoice = Invoice(invoice_items)

users = [
    User('Mark', 'Otto', '@mdo', 'Expiring', 'warning', 'trash', 'Share'),
    User('Jacob', 'Thornton', '@fat', 'Success', 'success', 'pencil', 'Submit'),
    User('Larry', 'the Bird', '@twitter', 'Error!', 'danger', 'share', 'Delete'),
    User('htmlstream', 'Web Design', '@htmlstream', 'Pending!', 'info', 'ok', 'Edit'),
]

comments = [
    BlogComment('Walter White', 'img/sliders/elastislide/2.jpg', '5 hours ago', children=[
        BlogComment('Walter Jr.', 'img/sliders/elastislide/3.jpg', '6 hours ago'),
        BlogComment('Holly', 'img/sliders/elastislide/6.jpg', '6 hours ago'),
    ]),
    BlogComment('Jesse Pinkman', 'img/sliders/elastislide/5.jpg', '17 hours ago'),
    BlogComment('Saul Goodman', 'img/sliders/elastislide/11.jpg', '2 days ago'),
    BlogComment('Skyler White', 'img/sliders/elastislide/9.jpg', '6 days ago'),
]

blog_posts = [
    # All these groups of blog posts just have different size of images and thus fit with different layouts

    # For Blog Large Page
    BlogPost('Unify is an incredibly beautiful and fully responsive Bootstrap 3 Template',
             datetime.datetime(2013, 04, 05), users[0], comments, 'IMAGE', 'img/posts/2.jpg'),
    BlogPost('Template comes with developer friendly and easy to customizable code',
             datetime.datetime(2013, 03, 16), users[0], comments, 'VIDEO', 'http://player.vimeo.com/video/47911018'),
    BlogPost('Unify Template works on all main web browsers, tablets and phones.',
             datetime.datetime(2013, 03, 10), users[0], comments, 'IMAGE_CAROUSEL', [
            {'url': 'img/posts/1.jpg', 'title': 'Facilisis odio, dapibus ac justo acilisis gestinas.'},
            {'url': 'img/posts/2.jpg', 'title': 'Cras justo odio, dapibus ac facilisis into egestas.'},
            {'url': 'img/posts/3.jpg', 'title': 'Justo cras odio apibus ac afilisis lingestas de.'},
        ]),
    # For Blog Medium Page
    BlogPost('Pellentesque Habitant Morbi Tristique',
             datetime.datetime(2013, 03, 05), users[1], comments, 'IMAGE', 'img/main/11.jpg'),
    BlogPost('Pellentesque Habitant Morbi Tristique',
             datetime.datetime(2013, 03, 05), users[1], comments, 'VIDEO', 'http://www.youtube.com/embed/ufsrgE0BYf0/'),
    BlogPost('Pellentesque Habitant Morbi Tristique',
             datetime.datetime(2013, 03, 05), users[1], comments, 'IMAGE', 'img/main/12.jpg'),
    BlogPost('Unify Template works on all main web browsers, tablets and phones.',
             datetime.datetime(2013, 03, 10), users[0], comments, 'IMAGE_CAROUSEL', [
            {'url': 'img/main/3.jpg', 'title': 'Facilisis odio, dapibus ac justo acilisis gestinas.'},
            {'url': 'img/main/13.jpg', 'title': 'Facilisis odawi, dapibus ac justo acilisis gestinas.'},
        ]),
    # For Blog Full Width Page
    BlogPost('Unify is an incredibly beautiful and fully responsive Bootstrap 3 Template',
             datetime.datetime(2013, 04, 05), users[0], comments, 'IMAGE', 'img/sliders/revolution/bg8.jpg'),
    BlogPost('Template comes with developer friendly and easy to customizable code',
             datetime.datetime(2013, 03, 16), users[0], comments, 'VIDEO', 'http://player.vimeo.com/video/47911018'),
    BlogPost('Unify Template works on all main web browsers, tablets and phones.',
             datetime.datetime(2013, 03, 10), users[0], comments, 'IMAGE_CAROUSEL', [
             {'url': 'img/sliders/revolution/bg2.jpg', 'title': 'Facilisis odio, dapibus ac justo acilisis gestinas.'},
             {'url': 'img/sliders/revolution/bg3.jpg', 'title': 'Cras justo odio, dapibus ac facilisis into egestas.'},
             {'url': 'img/sliders/revolution/bg4.jpg', 'title': 'Justo cras odio apibus ac afilisis lingestas de.'},
             ]),
]

# For use in `blog_left_sidebar.html` and `blog_right_sidebar.html`
blog_posts2 = [
    BlogPost('Sea Bordered Box', datetime.datetime(2013, 04, 05), users[0], comments, 'IMAGE', 'img/new/img1.jpg'),
    BlogPost('Grey Box', datetime.datetime(2013, 04, 05), users[0], comments, 'IMAGE', 'img/new/img1.jpg'),
    BlogPost('Yellow Bordered Box', datetime.datetime(2013, 04, 05), users[0], comments, 'IMAGE', 'img/new/img1.jpg'),
    BlogPost('Sea Box', datetime.datetime(2013, 04, 05), users[0], comments, 'IMAGE', 'img/new/img1.jpg'),
]

tags = [
    'Business', 'Music', 'Internet', 'Money', 'Google', 'TV Shows', 'Reddit',
    'Education', 'People', 'Math', 'Photos', 'Electronics', 'Apple', 'Canada',
]
