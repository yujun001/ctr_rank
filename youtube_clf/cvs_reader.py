from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd


def get_cvs_data(path):
    """ reads csv file from path
     and creates a pandas dataframe."""

    dataframe = pd.read_csv(path, error_bad_lines=False)
    return dataframe


def load_dataframe(csvpath, columns):
    """ Creates Dataframe with columns from
     values of given columns list and normalizes tags column."""

    csvdf = get_cvs_data(csvpath)
    df = pd.DataFrame(csvdf, columns=columns)

    for i, col in enumerate(df.columns):
        if col == 'tags':
            df.iloc[:, i] = (df.iloc[:, i]).str.replace('"', '')
    for i, col in enumerate(df.columns):
        if col == 'tags':
            df.iloc[:, i] = (df.iloc[:, i]).str.replace('#', '')

    return df
