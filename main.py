# ключ ab15d101be244d1d96485ebc43787594

from opencage.geocoder import OpenCageGeocode
from pygments.lexers.sql import language_re


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language= "ru")
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Возникла ошибка: {e}"

key = 'ab15d101be244d1d96485ebc43787594'
city = "London"
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')
