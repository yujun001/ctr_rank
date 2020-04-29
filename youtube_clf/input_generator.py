from __future__ import absolute_import, division, print_function, unicode_literals
from sklearn.model_selection import train_test_split


def generate_dataset(dataframe, target_column):
    """ Given dataframe creates train, test and val datasets."""

    dataframe = dataframe.copy()

    target_attribute = dataframe.pop(target_column)
    train_ds, test_ds, train_lb, test_lb = train_test_split(dataframe, target_attribute, test_size=0.2)
    train_ds, val_ds, train_lb, val_lb = train_test_split(train_ds, train_lb, test_size=0.25)

    return (train_ds, train_lb), (val_ds, val_lb), (test_ds, test_lb)
