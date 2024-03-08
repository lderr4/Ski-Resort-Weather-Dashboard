import io
import pandas as pd
import requests
import os
from constants import resorts, cols_current
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    weather_data = {col: [] for col in cols_current}
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    
    for pass_name, name, (lat, lon) in resorts:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print(f'Error fetching weather data: \nresponse: {response}\nurl: {url}')
            continue
        process_current(data, weather_data, (pass_name, name, lat, lon))


    df = pd.DataFrame(weather_data)
    return df



def process_current(x, weather_data, resort_info):
    
    
    pass_name, name, lat, lon = resort_info
  
        
    # date
    date = x['dt']

    # visibility
    visibility = x['visibility']

    # temperature
    temp = x['main']['temp']
    feels_like = x['main']['feels_like']
    temp_min = x['main']['temp_min']
    temp_max = x['main']['temp_max']

    # snowfall / rainfall (previous 3 hours)
    if "rain" in x:
        if '1h' in x['rain']:
            rain_1h_mm = x['rain']['1h']
        else:
            rain_1h_mm = 0
        if '3h' in x['rain']:
            rain_3h_mm = x['rain']['3h']
        else:
            rain_3h_mm = 0
    else:
        rain_1h_mm, rain_3h_mm = 0,0
            

    if "snow" in x:
        if '1h' in x['snow']:
            snow_1h_mm = x['snow']['1h']
        else:
            snow_1h_mm = 0
        if '3h' in x['snow']: 
            snow_3h_mm = x['snow']['3h']
        else:
            snow_3h_mm = 0
    else:
        snow_1h_mm, snow_3h_mm = 0,0

    # weather
    weather = x['weather'][0]['main']
    desc = x['weather'][0]['description']

    cloud_percent = x['clouds']['all']
    wind_speed = x['wind']['speed']


    weather_data['pass'].append(pass_name)
    weather_data['resort'].append(name)
    weather_data['latitude'].append(lat)
    weather_data['longitude'].append(lon)
    weather_data['date'].append(date)
    weather_data['vis'].append(visibility)
    weather_data['temp'].append(temp)
    weather_data['feels_like'].append(feels_like) 
    weather_data['temp_min'].append(temp_min) 
    weather_data['temp_max'].append(temp_max) 
    weather_data['weather'].append(weather) 
    weather_data['weather_description'].append(desc) 
    weather_data['cloud_percent'].append(cloud_percent) 
    weather_data['wind_speed'].append(wind_speed) 
    
    weather_data['snow_1h_mm'].append(snow_1h_mm)
    weather_data['rain_1h_mm'].append(rain_1h_mm)
    weather_data['snow_3h_mm'].append(snow_3h_mm)
    weather_data['rain_3h_mm'].append(rain_3h_mm)
    
    
    return weather_data
    
    

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
