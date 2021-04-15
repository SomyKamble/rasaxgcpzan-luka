# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import datetime as dt
from typing import Any, Text, Dict, List
import requests
import sqlalchemy
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
#from .sql_file_rem import serve
import json
from .sqlact import activity_count

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_time_now"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"The time is {dt.datetime.now().strftime('%Y/%m/%d %I:%M:%S')}")

        return []

class ActionReciveName(Action):

    def name(self) -> Text:
        return "action_recive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text=tracker.latest_message.get('text')

        dispatcher.utter_message(text=f"I will remember your name {text}")

        return [SlotSet("name",text)]


class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name=tracker.get_slot("name")

        if not name:
            dispatcher.utter_message(text="I do not know your name")
        else:
            dispatcher.utter_message(text=f"Your Name is {name}")

        return []

        dispatcher.utter_message(text=f"I will remember your name {text}")

        return [SlotSet("name",text)]

class Askforname(Action):

    def name(self) -> Text:
        return "action_ask_last_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        first_name=tracker.get_slot("first_name")

        dispatcher.utter_message(text=f"So {first_name} whats your last name")

        return []


class remcycles(Action):

    def name(self) -> Text:
        return "action_get_rem_cycles"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        first_name=tracker.get_slot("first_name")
        last_name = tracker.get_slot("last_name")
        #remi = serve(first_name,last_name)

        dispatcher.utter_message(text=f"So {first_name} {last_name} rem cycle in hrs is {remi}")

        return []


class Temperature(Action):

    def name(self) -> Text:
        return "get_temp"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city=tracker.get_slot("city")
        print(city)
        city=str(city)
        APIKEY='2a671b02284f8be0fd8d1fbfee1bef91'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + APIKEY + "&q=" + city.capitalize()
        response = requests.get(complete_url)
        x = response.json()
        #print(response)
        if x["cod"] != "404":
            y = x["main"]
        #
        #     # store the value corresponding
        #     # to the "temp" key of y
            current_temperature = round((y["temp"]*0.10),2)

            # store the value corresponding
            # to the "pressure" key of y
            current_pressure = y["pressure"]

            dispatcher.utter_message(text=f"So {city} has {current_temperature} temperature \n {current_pressure} is prussure")
        else:
            dispatcher.utter_message(text="city not found")
        dispatcher.utter_message(text=f"the temperature of {city}")
        return []

class Activity(Action):

    def name(self) -> Text:
        return "get_act"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        act=tracker.get_slot("body")
        a = activity_count(str(act))
        if a is not None:
            print(act)
            a=activity_count(str(act))
            print(a.iloc[0])
            dispatcher.utter_message(text=f"Your Latest {act} details are \n {a.iloc[0]}")
        else:
            dispatcher.utter_message(text=f"{act}")

        return []

