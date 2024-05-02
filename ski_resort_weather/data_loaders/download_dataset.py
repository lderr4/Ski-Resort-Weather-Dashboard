import os
import kaggle


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    dataset_name = "sobhanmoosavi/us-weather-events"
    dataset_target_dir = "shared_data"
    dataset_file_name_old = "WeatherEvents_Jan2016-Dec2022.csv"
    dataset_file_name_new = "airport_weather_bulk.csv"
    new_file_path = os.path.join(dataset_target_dir, dataset_file_name_new)
    old_file_path = os.path.join(dataset_target_dir, dataset_file_name_old)

    if os.path.exists(new_file_path):
        try:
            os.remove(new_file_path)
            print(f"{new_file_path} removed")
        
        except OSError as e:
            print(f"Error: {new_file_path} - {e.strerror}")
    else:
        print(f"{new_file_path} not found.")
    
    
    if os.path.exists(old_file_path):
        try:
            os.remove(old_file_path)
            print(f"{new_file_path} removed")
        
        except OSError as e:
            print(f"Error: {old_file_path} - {e.strerror}")
    else:
        print(f"{old_file_path} not found.")


    
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files(dataset_name, path=dataset_target_dir, unzip=True)
    
    
    new_file_path = os.path.join(dataset_target_dir, dataset_file_name_new)
    
    os.rename(old_file_path, new_file_path)
    print(f"Dataset Downloaded successfully at {new_file_path}")
    return new_file_path


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'