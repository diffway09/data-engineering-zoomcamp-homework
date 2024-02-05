if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("Rows with zero trip distance:" ,data['trip_distance'].isin([0]).sum() )

    return data[data['trip_distance'] > 0]

@test
def test_output(output, *args) -> None:
    assert (output['trip_distance'] > 0).all() , 'Rows with zero trip distance existed'