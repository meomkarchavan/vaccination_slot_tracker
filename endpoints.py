import urllib.parse

BASE_URL = 'https://cdn-api.co-vin.in/api'
GET_STATES = '/v2/appointment/sessions/public/calendarByDistrict'
GET_DISTRICTS = '/v2/admin/location/districts/%s'
GET_VACCINATION_BY_PIN='​/v2​/appointment​/sessions​/public​/findByPin'
GET_VACCINATION_BY_DISTRICT='/v2/appointment/sessions/public/findByDistrict'
GET_VACCINATION_BY_PIN_7='​/v2/appointment/sessions/public/calendarByPin'
GET_VACCINATION_BY_DISTRICT_7='/v2/appointment/sessions/public/calendarByDistrict'


def get_states_url():
    return BASE_URL+GET_STATES

def get_districts_url(state_id):
    return BASE_URL+GET_DISTRICTS % urllib.parse.quote_plus(state_id)

def get_vaccination_by_pin_url():
    return BASE_URL+GET_VACCINATION_BY_PIN

def get_vaccination_by_district_url():
    return BASE_URL+GET_VACCINATION_BY_DISTRICT

def get_vaccination_by_pin_7_url():
    return BASE_URL+GET_VACCINATION_BY_PIN_7

def get_vaccination_by_district_7_url():
    return BASE_URL+GET_VACCINATION_BY_DISTRICT_7