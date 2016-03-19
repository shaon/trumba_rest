import urllib
from flask import Flask
from flask_restful import Resource, Api
from icalendar import Calendar


app = Flask(__name__)
api = Api(app)


class HelloPark(Resource):

    def get(self, calendar_name):
        global_dict = {"events": []}

        target_url = "http://www.trumba.com/calendars/" + calendar_name + ".ics"
        txt = urllib.urlopen(target_url).read()
        cal = Calendar.from_ical(txt)
        events = global_dict["events"]
        for event in cal.walk('vevent'):
            keydict = {}
            for key in event.keys():
                if (key == 'DTSTART') or (key == 'DTEND') or (key == 'DTSTAMP'):
                    keydict[key.lower()] = event.get(key).dt.isoformat()
                else:
                    keydict[key.lower()] = event.get(key)
            events.append(keydict)
        return global_dict

api.add_resource(HelloPark, '/calendar/<string:calendar_name>')
