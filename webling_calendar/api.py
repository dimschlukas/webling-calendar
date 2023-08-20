import requests
import os
from dotenv import load_dotenv
from webling_calendar.calendarevent import Calendarevent
from webling_calendar.event import Event
from datetime import datetime, timedelta

load_dotenv()


class Api:  # pragma: no cover

    def __init__(self, api_key, endpoint):
        self.endpoint = endpoint
        self.headers = {'Content-Type': 'text/html',
                        'apikey': api_key}

    def get_calendar_ids(self):
        url = f'{self.endpoint}/calendar'
        r = requests.get(url, headers=self.headers)
        return r.json()['objects']

    def get_calenderevents_for_calendar_id(self, id):
        url = f'{self.endpoint}/calendar/{id}'
        r = requests.get(url, headers=self.headers)
        return r.json()['children']['calendarevent']

    def get_event_detail(self, id):
        url = f'{self.endpoint}/calendarevent/{id}'
        r = requests.get(url, headers=self.headers)
        return r.json()

    def create_new_calendarevent(self, calendarevent: Calendarevent):
        url = f'{self.endpoint}/calendarevent/'
        r = requests.post(url, headers=self.headers,
                          json=calendarevent.get_dict())
        print(r)
        print(r.json())

    def delete_calendar_event(self, id):
        url = f'{self.endpoint}/calendarevent/{id}'
        r = requests.delete(url, headers=self.headers)
        return r


if __name__ == '__main__':  # pragma: no cover
    api_key = os.getenv('WEBLING_API_KEY')
    endpoint = os.getenv('WEBLING_ENDPOINT')
    api = Api(api_key, endpoint)

    calendar_ids = api.get_calendar_ids()

    begin = datetime.now()
    duration = timedelta(minutes=120)

    event = Event(title='Test Event', description='Example description',
                  place='Judo und Aikido Club Wohlen', begin=begin,
                  duration=duration, is_all_day=False)
    calendarevent = Calendarevent(event, calendar_ids)
    # api.create_new_calendarevent(calendarevent)

    event_ids = api.get_calenderevents_for_calendar_id(calendar_ids[0])
    print(event_ids)
