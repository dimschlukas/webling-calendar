from webling_calendar.calendarevent import Calendarevent
from webling_calendar.event import Event
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
API_KEY = os.getenv("WEBLING_API_KEY")
ENDPOINT = os.getenv("WEBLING_ENDPOINT")

# Mok calendarevent data
TITLE = "Test event"
DESCRIPTION = "Test description"
PLACE = "Street, PLZ City"
BEGIN = datetime.now()
DURATION = timedelta(hours=2)
END = BEGIN + DURATION
IS_ALL_DAY = False
EVENT = Event(
    title=TITLE,
    description=DESCRIPTION,
    place=PLACE,
    begin=BEGIN,
    end=END,
    duration=DURATION,
    is_all_day=IS_ALL_DAY,
)


def test_get_data():
    calendarevent = Calendarevent(EVENT, [1234])
    data = calendarevent.get_dict()

    assert data == {"properties": EVENT.get_dict(), "parents": [1234]}
