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

        out_dict['AveragePPG'] = self.get_average(players_df, 'PPG')
        #out_dict['AveragePPG'].append(self.get_average(players_df, 'PPG'))

        self.top_selection(players_df, 'PPG', 3)

        self.players_position_count(players_df)

        return out_dict


    def sort_players(self, pd_df):
        '''Sorts the data based on column PPG'''
        return pd_df.sort_values('PPG', ascending=False)


    def get_average(self, pd_df, col):
        '''Finds the average value of specified pandas dataframe'''
        return round(pd_df[col].sum() / len(pd_df), 2)


    def top_selection(self, pd_df, col, count):
        '''Gets the top three values from dataframe'''
        in_df = pd_df.head(count)[['Name', 'PPG']]

        out_dict['Leaders'] = []

        for con in range(count):
            if (con == 0):
                out_dict['Leaders'].append({'Gold': in_df.iloc[con]['Name'], 'PPG': in_df.iloc[0]['PPG']})
            elif (con == 1):
                out_dict['Leaders'].append({'Silver': in_df.iloc[1]['Name'], 'PPG': in_df.iloc[1]['PPG']})
            elif (con == 2):
                out_dict['Leaders'].append({'Bronze': in_df.iloc[2]['Name'], 'PPG': in_df.iloc[2]['PPG']})
            else:
                out_dict['Leaders'].append({str(x): in_df.iloc[2]['Name'], 'PPG': in_df.iloc[2]['PPG']})
            con += 1

        return out_dict


    def players_position_count(self, pd_df):
        '''Gets the occurence of values in position column'''
        in_df = pd_df['Position'].value_counts()
        print (in_df)
        out_dict[''] = {
            'PG': in_df['PG'],
            'C': in_df['C'],
            'PF': in_df['PF'],
            'SG': in_df['SG'],
            'SF': in_df['SF'],
        }
        return out_dict


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

        if (test_dict[''] != ans_dict['']):
            result += 'player_postion_count fails, '

        if (test_dict['AverageHeight'] != ans_dict['AverageHeight']):
            result += 'average_height fails, '

        if(result != ''):
            return print(result)
        else:
            return print('All success!')


if __name__ == '__main__':
    BasketballSorter().test_outputs()
