import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    df = pd.DataFrame(data)

    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date

    return df

