from dataclasses import dataclass
from webling_calendar.event import Event


@dataclass
class Calendarevent:
    properties: Event
    parents: list[int]

    def get_dict(self):
        return {
                "properties": self.properties.get_dict(),
                "parents": self.parents
                }
