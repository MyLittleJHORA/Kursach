import pandas as pd


def rename_columns(df, column_mapping):
        return df.rename(columns=column_mapping)


if __name__ == '__main__':
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    print("DataFrame начальная:")
    print(df)
    new_column_names = {'A': 'Column1', 'B': 'Column2'}
    df_renamed = rename_columns(df, new_column_names)
    print("DataFrame с переименованными столбцами:")
    print(df_renamed)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
