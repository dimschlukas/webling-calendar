from webling_calendar.ics_reader import IcsReader
from webling_calendar.event import Event
import os
import pytest
from datetime import datetime, timedelta


@pytest.fixture(autouse=True)
def run_around_tests(tmp_path):
    filepath = os.path.join(tmp_path, "icalendar.ics")
    with open(filepath, "x") as file:
        file.write(
            """BEGIN:VCALENDAR
VERSION:2.0
PRODID:test-calendar
BEGIN:VEVENT
SUMMARY:test-event
DTSTART:20230710T200000
DTEND:20230710T213000
DTSTAMP:20230709T181720
UID:14c40176-1e74-11ee-80dc-3c219ccd9961
DESCRIPTION:test-description
LOCATION:test-location
END:VEVENT
END:VCALENDAR"""
        )
    yield


def test_file_read(tmp_path):
    calendar_name = "test-calendar"
    title = "test-event"
    begin = datetime(2023, 7, 10, 20, 0)
    end = datetime(2023, 7, 10, 21, 30)
    description = "test-description"
    place = "test-location"

    filepath = os.path.join(tmp_path, "icalendar.ics")
    ics = IcsReader(filepath)
    assert ics.event_list[0] == Event(title, begin, description, place, end)
    assert ics.calendar_name == calendar_name
