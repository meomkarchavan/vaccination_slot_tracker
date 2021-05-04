import requests
from endpoints import *

def get_states():
    resp=requests.get(get_states_url())
    return resp.json

def get_districts(state_id):
    resp=requests.get(get_districts_url(state_id=state_id))
    return resp.json

def get_vaccination_by_pin(query):
    resp=requests.get(get_vaccination_by_pin_url(),params=query)
    return resp.json

def get_vaccination_by_district(query):
    resp=requests.get(get_vaccination_by_district_url(),params=query)
    return resp.json

def get_vaccination_by_pin_7(query):
    resp=requests.get(get_vaccination_by_pin_7_url(),params=query)
    return resp.json

def get_vaccination_by_district_7(query):
    resp=requests.get(get_vaccination_by_district_7_url(),params=query)
    return resp.json