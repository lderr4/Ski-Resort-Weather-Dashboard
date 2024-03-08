import pandas as pd
import pytz
from timezonefinder import TimezoneFinder
import datetime
import os

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def get_time_zone(row, **kwargs):
    tf = kwargs.get('tf')
    lat = row['latitude']
    lon = row['longitude']
    timezone = tf.timezone_at(lng=lon, lat=lat)
    return timezone

def get_local_time(dt, tz):
    l = dt.tz_localize('UTC').tz_convert(tz)
    return l


@transformer
def transform(df, *args, **kwargs):
    
    tf = TimezoneFinder()
    kwargs = {'tf': tf}
    df['time_zone'] = df[['latitude', 'longitude']].apply(get_time_zone, axis=1, **kwargs)
    df['date_local'] = df[['date', 'time_zone']].apply(lambda row: get_local_time(row['date'], row['time_zone']), axis=1)

    df['year_local'] = df['date_local'].apply(lambda x: x.year)
    df['month_local'] = df['date_local'].apply(lambda x: x.month)
    df['day_local'] = df['date_local'].apply(lambda x: x.day)
    df['hour_local'] = df['date_local'].apply(lambda x: x.hour)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
