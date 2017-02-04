import quandl
import pandas as pd
import pickle

api_key = open('../02-Building_dataset/quandlapikey.txt', 'r').read()

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        # df = quandl.get(query, authtoken=api_key, start_date="2015-09-30", end_date="2016-09-30")
        df = quandl.get(query, authtoken=api_key, start_date="1996-09-30", end_date="2016-09-30")
        # df's index is `Date`, columns is `Value`(all the same), so I rename `'Value'` to `abbv` in next line.
        df.rename(columns={'Value': str(abbv)}, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    main_df.to_pickle('fiddy_states.pickle')
    # with open('fiddy_states.pickle', 'wb') as pickle_out:
    #     pickle.dump(main_df, pickle_out)

def read_state_data():
    HPI_data = pd.read_pickle('fiddy_states.pickle')
    # with open('fiddy_states.pickle', 'rb') as pickle_in:
    #     HPI_data = pickle.load(pickle_in)
    return HPI_data

if __name__ == '__main__':
    # collect and store DataFrame() in .pickle with Binary
    grab_initial_state_data()

    # read binary data to DataFrame()
    print(read_state_data())
