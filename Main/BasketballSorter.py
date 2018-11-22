from tkinter import filedialog
import pandas as pd
import json as js

out_dict = {}

csv_to_df = pd.DataFrame()

class BasketballSorter(object):

    def get_json(self):
        '''Calls all the required methods to format the csv into json'''
        players_df = pd.read_csv(filedialog.askopenfilename())

        players_df = self.sort_players(players_df)

        players_dict = players_df.to_dict('index')

        out_dict['Players'] = []
        for key, item in players_dict.items():
            out_dict['Players'].append(item)

        out_dict['AveragePPG'] = []
        out_dict['AveragePPG'].append(self.get_average(players_df, 'PPG'))

        out_dict['Leaders'] = []
        #out_dict['Leaders'].append(self.top_selection(players_df, 'PPG', 3))


        #print(js.dumps(out_dict))

        return out_dict


    def sort_players(self, pd_df):
        '''Sorts the data based on column PPG'''
        return pd_df.sort_values('PPG', ascending=False)


    def get_average(self, pd_df, col):
        '''Finds the average value of specified pandas dataframe'''
        return round(pd_df[col].sum() / len(pd_df), 2)


    def top_selection(self, pd_df, col, count):
        '''Gets the top three values from dataframe'''
        return pd_df.head(count)


    def players_position_count(self, pd_df):
        '''Gets the occurence of values in position column'''
        return pd_df


    def get_average_height(self, pd_df):
        '''Gets the average value from the height column'''
        return pd_df


    def test_outputs(self):
        result = ''

        input = open(filedialog.askopenfilename())
        ans_dict = js.load(input)
        input.close()

        test_dict = self.get_json()

        print(test_dict)
        print(ans_dict)

        if(test_dict['Players'] != ans_dict['Players']):
            result += 'sort_players fails, '

        if(test_dict['AveragePPG'] != ans_dict['AveragePPG']):
            result += 'get_average fails, '

        if(test_dict['Leaders'] != ans_dict['Leaders']):
            result += 'top_select fails, '

        if(result != ''):
            return print(result)
        else:
            return print('All success!')


if __name__ == '__main__':
    BasketballSorter().test_outputs()
