from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
from zoneinfo import ZoneInfo


class Checker:
    def __init__(self) -> None:
        self.geolocator = Nominatim(user_agent="Checker")
        self.tf_obj = TimezoneFinder()

    def check_current_time(self, place: str) -> datetime:
        location = self.geolocator.geocode(place)
        lat, lng = location.latitude, location.longitude
        time_zone_name = self.tf_obj.timezone_at(lat=lat, lng=lng)
        current_time = datetime.now(tz=ZoneInfo(time_zone_name))
        return current_time.replace(microsecond=0)


def run_program() -> None:
    checker = Checker()
    place = input("Enter place: ")
    current_time = checker.check_current_time(place)
    print(f"Current time: {current_time}")


if __name__ == "__main__":
    run_program()
