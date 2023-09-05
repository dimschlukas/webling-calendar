import requests
from webling_calendar.calendarevent import Calendarevent
from webling_calendar.models.calendar import Calendar


class Api:  # pragma: no cover
    def __init__(self, api_key, endpoint):
        self.endpoint = endpoint
        self.headers = {"Content-Type": "text/html", "apikey": api_key}

    def get_calendar_ids(self):
        url = f"{self.endpoint}/calendar"
        r = requests.get(url, headers=self.headers)
        return r.json()["objects"]

    def get_calendar_from_id(self, id):
        url = f"{self.endpoint}/calendar/{id}"
        r = requests.get(url, headers=self.headers)
        if not r.status_code == 200:
            return r.status_code
        props = r.json()["properties"]
        return Calendar(
            props["title"],
            props["color"],
            props["isPublic"],
            props["publicHash"],
            props["icsHash"],
        )

    def get_calenderevents_for_calendar_id(self, id):
        url = f"{self.endpoint}/calendar/{id}"
        r = requests.get(url, headers=self.headers)
        return r.json()["children"]["calendarevent"]

    def get_event_detail(self, id):
        url = f"{self.endpoint}/calendarevent/{id}"
        r = requests.get(url, headers=self.headers)
        return r.json()

    def create_new_calendarevent(self, calendarevent: Calendarevent):
        url = f"{self.endpoint}/calendarevent/"
        r = requests.post(
            url, headers=self.headers, json=calendarevent.get_dict()
        )
        if not r.status_code == 201:
            print(r)
            print(r.content)

    def delete_calendar_event(self, id):
        url = f"{self.endpoint}/calendarevent/{id}"
        r = requests.delete(url, headers=self.headers)
        return r
