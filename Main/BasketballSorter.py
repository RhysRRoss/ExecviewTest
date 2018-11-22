from tkinter import filedialog
import pandas as pd
import json as js

out_dict = {}

csv_to_df = pd.DataFrame()

class BasketballSorter:

    def get_json(self):
        '''Calls all the required methods to format the csv into json'''
        players_df = self.get_csv()

        players_dict = players_df.set_index('Id').T.to_dict()

        out_dict['Players'] = []

        for key, item in players_dict.items():
            out_dict['Players'].append(item)
        print(js.dumps(out_dict))



    def get_csv(self):
        '''Returns a CSV file as a dataframe'''
        return pd.read_csv(filedialog.askopenfilename())


    def sort_players(self, pd_df):
        '''Sorts the data based on column PPG'''

        return pd_df


    def get_average(self, pd_df):
        '''Finds the average height of payers'''
        return average


    def top_three(self, pd_df):
        '''Gets the top three values from dataframe'''
        return pd_df


    def players_position_count(self, pd_df):
        '''Gets the occurence of values in position column'''
        return pd_df


    def get_average_height(self, pd_df):
        '''Gets the average value from the height column'''
        return pd_df


if __name__ == '__main__':
    BasketballSorter().get_json()
