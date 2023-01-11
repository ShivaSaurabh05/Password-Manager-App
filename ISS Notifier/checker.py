from sunrise_or_sunset import *
from iss_location import *
from notify import current_time

def is_iss_overhead():
    if (My_lat -5 <= Get_location_latitude() <= My_lat +5) and (My_lng - 5 <= Get_location_longitude() <= My_lng + 5):
        return True

def is_night():
    if current_time >= sunset_time() or current_time <= sunrise_time():
        return True
