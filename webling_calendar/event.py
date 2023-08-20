from dataclasses import dataclass
from typing import Optional
from datetime import datetime, timedelta


@dataclass
class Event:
    title: str
    begin: datetime
    description: Optional[str] = None
    place: Optional[str] = None
    end: Optional[datetime] = None
    duration: Optional[timedelta] = None
    is_all_day: bool = False

    def __post_init__(self):
        if (self.end is None and self.duration is None):
            raise Exception("Either end datetime or duration has to be set")
        elif (self.end is not None and self.duration is None):
            self.duration = timedelta(hours=2)
        elif (self.end is None and self.duration is not None):
            self.end = self.begin + self.duration

    def get_dict(self):
        dtf = "%Y-%m-%d %H:%M:%S"
        return {
                    "title": self.title,
                    "description": self.description,
                    "place": self.place,
                    "begin": self.begin.strftime(dtf),
                    "end": self.end.strftime(dtf),
                    "duration": int(self.duration.seconds / 60),
                    "isAllDay": self.is_all_day,
                }
