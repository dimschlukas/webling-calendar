from webling_calendar.event import Event
from icalendar import Calendar


class IcsReader:
    event_list: list[Event] = []
    calendar_name = ""

    def __init__(self, filepath):
        with open(filepath, "rb") as file:
            ecal = Calendar.from_ical(file.read())
            for component in ecal.walk():
                if component.name == "VEVENT":
                    title = component.get("summary")
                    description = component.get("description")
                    place = component.get("location")
                    begin = component.decoded("dtstart")
                    end = component.decoded("dtend")

                    self.event_list.append(
                        Event(title, begin, description, place, end)
                    )
                elif component.name == "VCALENDAR":
                    self.calendar_name = component.get("PRODID")
