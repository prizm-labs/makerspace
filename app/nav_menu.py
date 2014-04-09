"""
Please use the following format to create header navigation menu.

Note: 'bc_title' for breadcrumb title is optional. By default the 'name' field
      is used for breadcrumb title, only use it when it needs to be customized
      to something different.

header_nav = [
    # without children
    {'name': 'Item Name', 'endpoint': 'endpoint_function_name', 'bc_title': 'Breadcrumb Title'},

    # with children
    {
        'name': 'Item Name',
        'children': [
            {'name': 'Child Name', 'endpoint': 'endpoint_function_name', 'bc_title': 'Breadcrumb Title'}
        ]
    }
]


Use the following format for sidebar navigation menu.

Note: 'label' and 'label_class' are optional, can be used to put assign label to the navigation item.

sidebar_nav = [
    {'name': 'Item Name', 'endpoint': 'endpoint_function_name'},
    {'name': 'Item Name', 'endpoint': 'endpoint_function_name', 'label': 'Label Title', 'label_class': 'badge-green'},
]

"""

header_nav = [
    {
        'name': 'Home',
        'children': [
            {'name': 'Option 1: Default Page', 'endpoint': 'index'},
            {'name': 'Option 2: Layer Slider', 'endpoint': 'page_home1'},
            {'name': 'Option 3: Revolution Slider', 'endpoint': 'page_home2'},
            {'name': 'Option 4: Amazing Content', 'endpoint': 'page_home3'},
            {'name': 'Option 5: Home Sidebar', 'endpoint': 'page_home4'},
            {'name': 'Option 6: Home Flatty', 'endpoint': 'page_home5'},
            {'name': 'Option 7: Home Magazine', 'endpoint': 'page_home6'},
            {'name': 'Option 8: Home Portfolio', 'endpoint': 'page_home7'},
        ]
    },
    {
        'name': 'Pages',
        'children': [
            {'name': 'About Us', 'endpoint': 'page_about'},
            {'name': 'About Us Option', 'endpoint': 'page_about1', 'bc_title': 'About Us'},
            {'name': 'Services', 'endpoint': 'page_services'},
            {'name': 'Services Option', 'endpoint': 'page_services1', 'bc_title': 'Services'},
            {'name': 'Pricing Tables', 'endpoint': 'page_pricing', 'bc_title': 'Pricing'},
            {'name': 'Invoice Page', 'endpoint': 'page_invoice', 'bc_title': 'Invoice'},
            {'name': 'Meet Our Team', 'endpoint': 'page_meet_our_team'},
            {'name': 'Coming Soon', 'endpoint': 'page_coming_soon'},
            {'name': 'FAQs Page', 'endpoint': 'page_faq', 'bc_title': 'FAQ'},
            {'name': 'Funny Boxes', 'endpoint': 'page_funny_boxes'},
            {'name': 'Gallery Page', 'endpoint': 'page_gallery', 'bc_title': 'Gallery'},
            {'name': 'Registration Page', 'endpoint': 'page_registration', 'bc_title': 'Registration'},
            {'name': 'Registration Option', 'endpoint': 'page_registration1'},
            {'name': 'Login Page', 'endpoint': 'page_login', 'bc_title': 'Login'},
            {'name': 'Login Option', 'endpoint': 'page_login1'},
            {'name': '404 Error', 'endpoint': 'page_404_error'},
            {'name': '404 Error Option', 'endpoint': 'page_404_error1'},
            {'name': 'Clients Page', 'endpoint': 'page_clients', 'bc_title': 'Our Clients'},
            {'name': 'Privacy Policy', 'endpoint': 'page_privacy'},
            {'name': 'Terms Of Service', 'endpoint': 'page_terms'},
            {'name': '2 Columns Page Left', 'endpoint': 'page_2_columns_left', 'bc_title': 'Left Column'},
            {'name': '2 Columns Page Right', 'endpoint': 'page_2_columns_right', 'bc_title': 'Right Column'},
            {'name': '3 Columns Page', 'endpoint': 'page_3_columns', 'bc_title': 'Three Columns'},
        ]
    },
    {
        'name': 'Features',
        'children': [
            {'name': 'Grid Layout', 'endpoint': 'feature_grid'},
            {'name': 'Content Boxes', 'endpoint': 'feature_boxes'},
            {'name': 'Typography', 'endpoint': 'feature_typography'},
            {'name': 'Tagline Boxes', 'endpoint': 'feature_tagline_boxes'},
            {'name': 'Buttons', 'endpoint': 'feature_buttons'},
            {'name': 'Icons', 'endpoint': 'feature_icons'},
            {'name': 'Thumbnails', 'endpoint': 'feature_thumbnails'},
            {'name': 'Components', 'endpoint': 'feature_components'},
            {'name': 'Accordion and Tabs', 'endpoint': 'feature_accordion_and_tabs'},
            {'name': 'Navigations', 'endpoint': 'feature_navigations'},
            {'name': 'Tables', 'endpoint': 'feature_tables'},
            {'name': 'Forms', 'endpoint': 'feature_forms'},
            {'name': 'Testimonials', 'endpoint': 'feature_testimonials'},
        ]
    },
    {
        'name': 'Portfolio',
        'children': [
            {'name': 'Portfolio Text Blocks', 'endpoint': 'portfolio_text_blocks'},
            {'name': 'Portfolio 2 Columns', 'endpoint': 'portfolio_2_column'},
            {'name': 'Portfolio 3 Columns', 'endpoint': 'portfolio_3_column'},
            {'name': 'Portfolio 4 Columns', 'endpoint': 'portfolio_4_column'},
            {'name': 'Portfolio Item Option 1', 'endpoint': 'portfolio_item'},
            {'name': 'Portfolio Item Option 2', 'endpoint': 'portfolio_item1'},
        ]
    },
    {
        'name': 'Blog',
        'children': [
            {'name': 'Blog Page', 'endpoint': 'blog_page'},
            {'name': 'Blog Large', 'endpoint': 'blog_large'},
            {'name': 'Blog Medium', 'endpoint': 'blog_medium'},
            {'name': 'Blog Full Width', 'endpoint': 'blog_full_width'},
            {'name': 'Blog Left Sidebar', 'endpoint': 'blog_left_sidebar'},
            {'name': 'Blog Right Sidebar', 'endpoint': 'blog_right_sidebar'},
            {'name': 'Blog Item Option 1', 'endpoint': 'blog_item_option1'},
            {'name': 'Blog Item Option 2', 'endpoint': 'blog_item_option2'},
        ]
    },
    {
        'name': 'Contacts',
        'children': [
            {'name': 'Contacts Default', 'endpoint': 'page_contact1', 'bc_title': 'Contact Us'},
            {'name': 'Contacts Option 1', 'endpoint': 'page_contact2', 'bc_title': 'Contact Us'},
            {'name': 'Contacts Option 2', 'endpoint': 'page_contact3', 'bc_title': 'Contact Us'},
        ]
    },
]


sidebar_nav = [
    {'name': 'Grid Layout', 'endpoint': 'feature_grid'},
    {'name': 'Content Boxes', 'endpoint': 'feature_boxes', 'label': 'New', 'label_class': 'badge-green'},
    {'name': 'Typography', 'endpoint': 'feature_typography'},
    {'name': 'Tagline Boxes', 'endpoint': 'feature_tagline_boxes', 'label': 'New', 'label_class': 'badge-red'},
    {'name': 'Buttons', 'endpoint': 'feature_buttons'},
    {'name': 'Icons', 'endpoint': 'feature_icons', 'label': 'New', 'label_class': ''},
    {'name': 'Thumbnails', 'endpoint': 'feature_thumbnails'},
    {'name': 'Components', 'endpoint': 'feature_components'},
    {'name': 'Accordion and Tabs', 'endpoint': 'feature_accordion_and_tabs', 'label': 'New', 'label_class': 'badge-blue'},
    {'name': 'Navigations', 'endpoint': 'feature_navigations'},
    {'name': 'Tables', 'endpoint': 'feature_tables'},
    {'name': 'Forms', 'endpoint': 'feature_forms'},
    {'name': 'Testimonials', 'endpoint': 'feature_testimonials', 'label': 'New', 'label_class': 'badge-sea'},
]
