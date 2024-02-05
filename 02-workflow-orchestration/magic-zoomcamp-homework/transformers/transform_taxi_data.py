if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Rows with zero passsengers:" ,data['passenger_count'].isin([0]).sum() )

    print("Rows with zero trip distance:" ,data['trip_distance'].isin([0]).sum() )
    


    return data[data['passenger_count'] > 0, data['trip_distance'] > 0]


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
