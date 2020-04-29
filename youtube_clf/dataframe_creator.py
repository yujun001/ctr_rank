def create_seperate_columns(df, num_of_columns, column, nan_value='notags', splitor='|'):
    """ Split tags into num_of_columns
     columns by using '|' as separator."""

    new = df[column].str.split(splitor, expand=True)

    for i in range(0, num_of_columns):
        name = 'tag_' + str(i)
        df[name] = new[i]

    df.drop(columns=[column], inplace=True)
    df.fillna(nan_value, inplace=True)
    return df


def create_listed_columns(df, column):
    """ Creates a list of tags by separating
     by '|' and puts the list as column value."""

    df[column] = df[column].str.split(".")
    return df
