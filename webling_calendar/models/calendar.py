from dataclasses import dataclass


@dataclass
class Calendar:
    title: str
    color: str
    is_public: bool
    public_hash: str
    ics_hash: str

    def get_dict(self):
        return {
            "title": self.title,
            "color": self.color,
            "isPublic": self.is_public,
            "publicHash": self.public_hash,
            "icHash": self.ics_hash,
        }
