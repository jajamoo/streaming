import pandas as pd

local_file = '/sms_estimates_summary.csv'


def get_data(index_col='date'):

    data = pd.read_csv(
        local_file,
        index_col = 'report_date',
        usecols = ['label_id', 'release_id', 'sum_units', 'sum_royalty', 'report_date', 'territory_id'],
        parse_dates = ['report_date']
    )

    return data
