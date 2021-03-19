import json


class Event(dict):
    def __init__(self, event_string):
        e = json.loads(event_string.decode('utf-8'))
        super().__init__(e)

