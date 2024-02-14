import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    all_df = []

    types = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID':pd.Int64Dtype(),
                'store_and_fwd_flag':str,
                'PULocationID':pd.Int64Dtype(),
                'DOLocationID':pd.Int64Dtype(),
                'payment_type': pd.Int64Dtype(),
                'fare_amount': float,
                'extra':float,
                'mta_tax':float,
                'tip_amount':float,
                'tolls_amount':float,
                'improvement_surcharge':float,
                'total_amount':float,
                'congestion_surcharge':float
            }

    for i in range(12):
        month = '0'+str(i+1)
        month = month[-2:]

        response = requests.get(f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-{month}.parquet')
        df = pd.read_parquet(io.BytesIO(response.content))

        df['lpep_pickup_datetime'] = pd.to_datetime(df['lpep_pickup_datetime']).dt.tz_localize(None)
        df['lpep_dropoff_datetime'] = pd.to_datetime(df['lpep_dropoff_datetime'])

        df = df.astype(types)

        all_df.append(df)

    return pd.concat(all_df)