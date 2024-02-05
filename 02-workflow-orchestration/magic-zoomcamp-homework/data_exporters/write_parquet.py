from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    df.to_parquet('green_taxi.parquet', engine='pyarrow', partition_cols = ['lpep_pickup_date'])