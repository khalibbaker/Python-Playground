#!/usr/bin/env python3

"""
Published by: Khalib Baker, President

This program pulls current weather from a location specified by the user. In order
to get current weather conditions, an API from OPEN WEATHER MAP weather is used.

Source: https://openweathermap.org/current
Source: https://openweathermap.org
"""

# Import Libraries
from weather import Weather, Unit

def getWeather():
    '''
    This function accepts a str 'city, state' or city and prints the 10-day forecastself.
    '''
    userLocation = input('Please enter a location in the US (city, st): ')
    weather = Weather(unit=Unit.FAHRENHEIT)
    location = weather.lookup_by_location(userLocation)

    forecasts = location.forecast
    dayCount = 1
    for forecast in forecasts:
        # Set variables
        text = forecast.text
        date = forecast.date
        highTemp = forecast.high
        lowTemp = forecast.low
        # Display
        print('-----------------------------------------------')
        print('\t\t\t\t\tDay:', dayCount, '\nDate:', date.replace(' ', '-'))
        print('It is going to be %s.' % (text.lower()))
        print('High:', highTemp, 'F')
        print('Low:', lowTemp, 'F')
        print('-----------------------------------------------')

        dayCount += 1

def exportWeather():
    '''
    This function will create a pandas dataframe and export the 10-day forecast
    to a CSV
    '''
    # Currently working on this function
    return None

# Main function
if __name__ == '__main__':
    # Display
    print('Welcome! Want a 10-day forecast?')

    # Execute
    getWeather()
