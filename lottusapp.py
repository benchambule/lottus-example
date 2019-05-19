import lottus.core
import json
import os
import lottus.helpers

with open('menus.json') as f:
    menus = json.load(f)

def get_lottus_app():
    lottus_app = lottus.core.Lottus(__name__, 'INITIAL', menus, InMemoryUSSDSessionBag())

    return lottus_app


class InMemoryUSSDSessionBag(lottus.core.USSDSessionBag):
    def __init__(self):
        self.__sessions = []

    def get_session(self, msisdn, session):
        return next((s for s in self.__sessions if s['session'] == session), None)

    def update_session(self, session):
        pass

    def save_session(self, session):
        pass

    def add_session(self, session):
        self.__sessions.append(session)