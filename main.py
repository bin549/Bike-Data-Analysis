import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # read file
    df = pd.read_excel('./excel/bike_data.xlsx', encoding='utf-8', sheet_name='Sheet1')
    print(type(df))
    # get column

    df['学校名称'].value_counts()

    ser = pd.Series(np.logspace(-2, 2, 30))
    n_25 = np.percentile(ser, q=[25, 95])[0]
    n_95 = np.percentile(ser, q=[25, 95])[1]
    df = pd.DataFrame(ser)
    df[df[0] < n_25] = n_25
    df[df[0] > n_95] = n_95
    print(df.transpose)

    df = pd.DataFrame(np.random.randn(100, 3), columns=["col1", "col2", "col3"])
    df.plot.bar(stacked=True)

    df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                        'weight': ['high', 'medium', 'low'] * 3,
                        'price': np.random.randint(0, 10, 9)})

    df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                        'kilo': ['high', 'low'] * 3,
                        'price': np.random.randint(0, 10, 6)})

    n_df = pd.merge(df1, df2, how='inner',
                    left_on=['fruit', 'weight'],
                    right_on=['pazham', 'kilo'],
                    suffixes=['_left', '_right'])

    print(n_df)

    p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

    sum((p - q) ** 2) ** .5

    state = np.random.RandomState(100)
    ser = pd.Series(state.normal(10, 5, 25))
    np.percentile(ser, q=[0, 25, 50, 75, 100])

    ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
    ser2 = pd.Series(np.arange(26))

    pd.DataFrame(pd.Series(ser1, ser2))

    mylist = list('abcedfghijklmnopqrstuvwxyz')
    myarr = np.arange(26)

    mydict = dict(zip(mylist, myarr))
    ser = pd.Series(mydict)
    print(ser)

    dictionary = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 5}
    pd.Series(dictionary)

    numpy_array = np.arange(1, 10)
    pd.Series(numpy_array)

    a_list = list("abcdefg")
    pd.Series(a_list)

    df = {'Apple': pd.Series(['35', '41'], index=['2017 Sale', '2018 Sale']),
          'Banana': pd.Series(['21', '34'], index=['2017 Sale', '2018 Sale'])}

    pd.DataFrame(df)

    countries = ['USA', 'France', 'China']
    my_data = [100, 200, 300]

    pd.Series(my_data, countries)

    array = np.array(my_data)

    pd.Series(array)

    my_dict = {'a': 50, 'b': 60, 'c': 70, 'd': 80}

    pd.Series(my_dict)

    my_dict_list = [{'a': 50, 'b': 60, 'c': 70, 'd': 80}, {'a': 80, 'b': 80, 'c': 70, 'd': 80}]
    df = pd.DataFrame(my_dict_list)

    df

    countries = ['USA', 'France', 'China']
    my_data = [100, 200, 300]
    series = pd.Series(my_data, countries)
    series['USA']

    series1 = pd.Series([1, 2, 3, 4], ['London', 'HongKong', 'Shanghai', 'Shenzhen'])
    series2 = pd.Series([0, 6, 7, 8], ['London', 'Shenzhen', 'NewYork', 'Delhi'])

    np.random.seed(100)
    dataframe = pd.DataFrame(data=np.random.randint(low=1, high=10, size=(5, 4)))
    print(dataframe)

    df = {'name': pd.Series(['Jon', 'Aaron', 'Tod'], index=['a', 'b', 'c']),
          'age': pd.Series(['39', '28', '17', '25'], index=['a', 'b', 'c', 'd']),
          'nationality': pd.Series(['US', 'China', 'US'], ['a', 'b', 'c'])}
    pd.DataFrame(df)

    data = {'name': ['Jon', 'Aaron', 'Tod'],
            'age': ['39', '28', '17'],
            'nationality': ['US', 'China', 'US']}
    my_df = pd.DataFrame(data,
                         index=['Lagos', 'Dubai', 'Mumbai'])
    my_df

    my_data = [{'name': 'a', 'age': 3}, {'name': 'b', 'age': 18}]

    temp_df = pd.DataFrame(my_data)

    temp_df

    my_df['name']

    type(my_df['name'])

    my_df[['name', 'age']]

    type(my_df[['name', 'age']])

    my_df

    my_df['year'] = pd.Series(['2016', '2017', '2018'],
                              ['Lagos', 'Dubai', 'Mumbai'])
    my_df

    my_df['age_year'] = my_df['age'] + my_df['year']
    my_df

    my_df.drop('age_year', axis=1)

    my_df.drop('Dubai', axis=0)

    my_df.drop(index='Lagos')

    my_df

    my_df.drop('Dubai', axis=0, inplace=True)
    my_df

    my_df.loc['Lagos']

    my_df.loc[['Lagos', 'Mumbai']]

    my_df.iloc[0]

    my_df.iloc[[0, 1]]

    my_df.loc['Lagos', 'name']

    


    # draw simple

    # sentence

    # draw it 111

    pass


if __name__ == '__main__':
    main()
