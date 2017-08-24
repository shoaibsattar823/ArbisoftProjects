"""In this program we are fetching weather data from web page and then
displaying the informations.
"""


import requests
import json


def main():
    print '***Please enter the latitude and longitude where you want to know\
the weather***\n'

    lat = input('Enter the latitude: ')  # 31.4839658
    longit = input('Enter the longitude: ')  # 74.1861179
    url = 'https://api.darksky.net/forecast/39ecfa77\
5ce65ce3e38df70e14b76394/{lat},{longit}'.format(lat=lat, longit=longit)

    page = requests.get(url)
    content = page.content
    content_dict = json.loads(content)
    info = content_dict['currently']

    print 'Weather for region located at: Latitude = %s, Longitude = %s\n'\
          % (content_dict['latitude'], content_dict['longitude'])

    print 'Time: %s\nSummary: %s\nTemperature: %s Humidity:\
            %s\nWind Speed: %s' % (
            info['time'], info['summary'], info['temperature'],
            info['humidity'], info['windSpeed'])


if __name__ == '__main__':
    main()
