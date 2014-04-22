from aweber_api import AWeberAPI
from aweber_api.base import APIException

class AWeberInterface(object):

    def __init__(self):
        # replace XXX with your keys
        consumer_key = 'Ak7W3K2vE3pODdOyag0t5X79'
        consumer_secret = 'ekxdnHs8aPgHIlI6RBLk3BynpylWEHCzSr4042vP'
        self.access_token = 'Agv7HS28IZoTDI05Zt1LuLIt'
        self.access_secret = 's2NucR72EL8S9KKmlriAhNNCP04mG1tqOsCkII5O'

        self.application = AWeberAPI(consumer_key, consumer_secret)
        self.account = self.application.get_account(self.access_token, self.access_secret)

    def connect_to_AWeber_account(self):
        app_id = '7XXXXXX8'
        authorization_url = 'https://auth.aweber.com/1.0/oauth/authorize_app/%s' % app_id
        print 'Go to this url in your browser: %s' % authorization_url
        authorization_code = raw_input('Type code here: ')

        auth = AWeberAPI.parse_authorization_code(authorization_code)
        consumer_key, consumer_secret, access_key, access_secret = auth
        print auth
        return auth

    def find_list(self):
        lists = self.account.lists.find(name="makerspace")
        return lists[0]

    def find_subscriber(self):
        subscribers = self.account.findSubscribers(email="whtever@example.com")
        return subscribers[0]

    def add_subscriber(self, subscriber, _list):
        list_url = '/accounts/%s/lists/%s' % (self.account.id, _list.id)
        _list = self.account.load_from_url(list_url)

        success = False
        data = {}

        try:
            new_subscriber = _list.subscribers.create(**subscriber)
            print new_subscriber
            success = True
            data = {
                'email': new_subscriber.email
            }

        except APIException, exc:
            print exc
            report = exc.message.split(':')
            # WebServiceError: email: Subscriber already subscribed and has not confirmed.

            data = {
                'class': report[0].strip(),
                'category': report[1].strip(),
                'status': report[2].strip()
            }

        except Exception, exc:
            print exc

        response = {
            'success': success,
            'data': data
        }

        return response

