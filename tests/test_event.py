from webling_calendar.event import Event
from datetime import datetime, timedelta
import pytest

# Mok calendarevent data
TITLE = 'Test event'
DESCRIPTION = 'Test description'
PLACE = 'Street, PLZ City'
BEGIN = datetime.now()
DURATION = timedelta(hours=2)
END = BEGIN + DURATION
IS_ALL_DAY = False

# Date format
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def test_default_constructor():
    event = Event(title=TITLE, description=DESCRIPTION, place=PLACE, begin=BEGIN, end=END, duration=DURATION, is_all_day=IS_ALL_DAY)

    assert event.get_dict() == {
                    "title": TITLE,
                    "description": DESCRIPTION,
                    "place": PLACE,
                    "begin": BEGIN.strftime(DATETIME_FORMAT),
                    "end": END.strftime(DATETIME_FORMAT),
                    "duration": int(DURATION.seconds / 60),
                    "isAllDay": IS_ALL_DAY,
                }

def test_without_end_datetime():
    event = Event(title=TITLE, description=DESCRIPTION, place=PLACE, begin=BEGIN, duration=DURATION, is_all_day=IS_ALL_DAY)
    assert event.get_dict() == {
                    "title": TITLE,
                    "description": DESCRIPTION,
                    "place": PLACE,
                    "begin": BEGIN.strftime(DATETIME_FORMAT),
                    "end": END.strftime(DATETIME_FORMAT),
                    "duration": int(DURATION.seconds / 60),
                    "isAllDay": IS_ALL_DAY,
                }

def test_without_duration():
    event = Event(title=TITLE, description=DESCRIPTION, place=PLACE, begin=BEGIN, end=END, is_all_day=IS_ALL_DAY)
    assert event.get_dict() == {
                    "title": TITLE,
                    "description": DESCRIPTION,
                    "place": PLACE,
                    "begin": BEGIN.strftime(DATETIME_FORMAT),
                    "end": END.strftime(DATETIME_FORMAT),
                    "duration": int(DURATION.seconds / 60),
                    "isAllDay": IS_ALL_DAY,
                }


def test_exception_if_duration_and_end_is_missing():
    with pytest.raises(Exception, match="Either end datetime or duration has to be set") as e_info:
        event = Event(title=TITLE, description=DESCRIPTION, place=PLACE, begin=BEGIN, is_all_day=IS_ALL_DAY)
