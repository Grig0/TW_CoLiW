import facebook
import urllib
from urllib import request
import json

# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = '506276502849459'
FACEBOOK_APP_SECRET = '0eab8f2933a00ef259eaa712d5716b5b'

oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
request_params = urllib.parse.urlencode(oauth_args)

req = urllib.request.Request('https://graph.facebook.com/oauth/access_token?', request_params.encode('ascii'))
data = urllib.request.urlopen(req).read().decode("utf-8")
data = json.loads(data)
print(data)
print(data.get('access_token'))