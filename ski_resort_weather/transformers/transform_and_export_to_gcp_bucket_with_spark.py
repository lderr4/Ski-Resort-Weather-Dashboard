import os
from pyspark.sql import SparkSession

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
print("asd;lkfjas;dlkfja;l")

@transformer
def transform(file_path,  *args, **kwargs):
    file_path = "shared_data/airport_weather_bulk.csv"
    gcp_creds = "/home/src/keys/data-engineering-zoom-413802-676a43f8dfc0.json"
    project_id = os.environ.get('GCP_PROJECT_ID')
    table_name = 'ski_resort_weather_dataset.airport_weather_dataset'
       
    spark_jars = ",".join([
        '/home/src/spark_files/gcs-connector-hadoop3-latest.jar',
        '/home/src/spark_files/spark-3.5-bigquery-0.37.0.jar'])

   


    spark = SparkSession.builder \
    .master("spark://spark-master:7077") \
    .appName(";lskdajf;lalksdjf;laskdjf") \
    .config("spark.executor.memory", "1g") \
    .config("spark.driver.memory", "4g") \
    .config("spark.sql.files.maxPartitionBytes", "128m") \
    .config("spark.jars", spark_jars) \
    .getOrCreate()

    spark._jsc.hadoopConfiguration().set("google.cloud.auth.service.account.json.keyfile",gcp_creds)
    spark._jsc.hadoopConfiguration().set('fs.gs.impl', 'com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem')
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    
    df = df.filter((df["Severity"] != "UNK") & (df["Severity"] != "Other"))
    output_path = "shared_data/spark_output"

    output_path = 'shared_data/spark_output'
    df.write.parquet(output_path, mode="overwrite")
    df.write.format('bigquery') \
      .mode('overwrite') \
      .option("temporaryGcsBucket",f"raw_ski_resort_weather") \
      .option("credentialsFile", gcp_creds) \
      .option("parentProject", project_id) \
      .option('table', table_name) \
      .option("createDisposition", "CREATE_IF_NEEDED") \
      .option("partitionField", "AirportCode") \
      .save()
    return output_path


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
