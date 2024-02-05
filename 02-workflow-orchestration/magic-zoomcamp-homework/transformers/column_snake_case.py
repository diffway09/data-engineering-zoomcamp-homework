import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print("The existing values of 'VendorID' : ", pd.unique(data['VendorID']))
    before = data.columns.to_numpy()
    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True)
                    .str.lower()
    )

    after = data.columns.to_numpy()
    diff = len(set(before) - set(after))
    print(f'There are {diff} columns need to be renamed to snake case')

    return data

@test
def test_output(output, *args) -> None:
    assert (output.columns == 'vendor_id').any() , 'Column name vendor_id is undefined'