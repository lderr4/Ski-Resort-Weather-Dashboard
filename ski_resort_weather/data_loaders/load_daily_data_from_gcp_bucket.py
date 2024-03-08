from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
import pandas as pd
import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    """
    Template for loading data from a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    dt = datetime.datetime.now()
    date = dt.strftime('%Y_%m_%d')
    hour = list(range(0,24))


    bucket_name = 'raw_ski_resort_weather'
    weather_folder = f'current_weather/{date}'
    filename = 'current_weather'

    obj = 'current_weather/2024_03_07/'
    daily_data = []
    for h in hour:

        if h < 10:
            h = f'0{h}'
        else:
            h = str(h)

        datehour = f"{date}_{h}"
        filepath = f"{weather_folder}/{filename}_{datehour}.parquet"
        try:
            obj = GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).load(bucket_name, filepath)
            if obj.empty:
                print(print(f"{filepath} empty."))
                continue
            daily_data.append(obj)
            print(f"{filepath} loaded.")
        except:
            print(f"{filepath} failed to load.")
            continue
        
    return pd.concat(daily_data)
    
   


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
