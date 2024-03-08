import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    current_weather_dtypes = {
        'pass': str,
        'resort': str,
        'vis': pd.Int64Dtype(),
        'temp': float,
        'feels_like': float,
        'temp_min': float,
        'temp_max': float,
        'weather': str,
        'weather_description': str,
        'cloud_percent': pd.Int64Dtype(),
        'wind_speed': float, 
        'latitude': float,
        'longitude': float,
        'rain_1h_mm': float,
        'snow_1h_mm': float,
        'rain_3h_mm': float,
        'snow_3h_mm': float
    }

    df['date'] = pd.to_datetime(df['date'], unit='s')
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour

    for col_name, dtype in current_weather_dtypes.items():
        df[col_name] = df[col_name].astype(dtype)

    return df


    


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
