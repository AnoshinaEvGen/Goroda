# ключ ab15d101be244d1d96485ebc43787594

from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return "Город не найден"

key = 'ab15d101be244d1d96485ebc43787594'
city = "Moscow"
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')
