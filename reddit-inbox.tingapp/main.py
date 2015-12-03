# coding: utf8
import tingbot
from tingbot import screen
from tingbot.graphics import Image
import requests
import pprint

options = {
    'feed_id': '', # Found in the url of your Reddit unread messages feed.
    'username': '' # Reddit username
}

messages = []

@tingbot.every(minutes=30)
def refresh_data():
    print 'refreshing...'

    r = requests.get('https://www.reddit.com/message/messages/.json', params={'feed': '%s' % options['feed_id'], 'user': '%s' % options['username']})
    r.raise_for_status()

    api_data = r.json()
    raw_messages = api_data['data']['children'];

    pprint.pprint(api_data)

    # Available data for development.
    # body - string
    # was_comment - boolean
    # created - timestamp
    # dest - string (message to)
    # author - string (message from)
    # created_utc - timestamp
    # body_html - string
    # replies - array
    # id - string
    # subject - string

    messages[:] = []
    for message in raw_messages:
        messages.append({
            'subject': message['data']['subject'],
            'dest': message['data']['dest'],
            'author': message['data']['author'],
            'created': message['data']['created'],
        })


def loop():
    screen.fill(color='black')

    screen.text (
        'Hello World',
        xy=(22,30),
        align='left',
        color='white',
        font_size=12,
    )

    screen.text (
        messages[0]['subject'],
        xy=(22,100),
        align='left',
        color='white',
        font_size=12,
    )

# run the app
tingbot.run(loop)
