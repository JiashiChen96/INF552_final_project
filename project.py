import numpy as np
import pandas as pd

class project_framework(object):
    def __init__(self, data):
        self.data = data.copy()
    def clean_1(self):

        #Drop the outliers
        self.data.drop(self.data[self.data['hoa (R$)']==1117000].index, inplace=True)
        self.data.drop(self.data[self.data['property tax (R$)']==313700].index, inplace=True)
        self.data.drop(self.data[self.data['total (R$)']==1120000].index, inplace=True)
        self.data.drop(self.data[self.data['floor']=='301'].index, inplace=True)

        #Log transformation
        self.data['hoa (R$)'] = self.data['hoa (R$)'] .apply(lambda x: np.log1p(x))
        self.data['rent amount (R$)'] = self.data['rent amount (R$)'] .apply(lambda x: np.log1p(x))
        self.data['property tax (R$)'] = self.data['property tax (R$)'].apply(lambda x: np.log1p(x))
        self.data['fire insurance (R$)'] = self.data['fire insurance (R$)'].apply(lambda x: np.log1p(x))
        self.data['total (R$)'] = self.data['total (R$)'].apply(lambda x: np.log1p(x))

        #Fill the missing values
        self.data['floor'] = self.data['floor'].apply(lambda x: replace_with_nan(x, '-'))
        self.data['floor'] = self.data['floor'].astype(float)
        floor_mean = self.data['floor'].mean()
        self.data['floor'] = self.data['floor'].apply(lambda x: fill_with_num(x, floor_mean))

        # count = 0
        # total = 0
        # for floor in self.data["floor"]:
        #     if floor != '-':
        #         if floor != "301":
        #             total += int(floor)
        #         else:
        #             total += 31
        #         count += 1
        # mean = total / count
        # self.data['floor'] = self.data['floor'].apply(lambda x: fillFloor(x, mean))

        #Transfor categorical attribute
        self.data['animal'] = self.data['animal'].apply(lambda x: fillAnimalFurniture(x))
        self.data['furniture'] = self.data['furniture'].apply(lambda x: fillAnimalFurniture(x))
        
        onehot = pd.get_dummies(self.data['city'], drop_first = True)
        for colname in onehot:
            self.data[colname] = onehot[colname]
        # self.data.drop(columns = ['city'], inplace = True)

    def clean_2(slef):
        self.data.drop(columns = ['hoa (R$)'], inplace = True)

def replace_with_nan(x, old_val):
    return np.nan if x == old_val else x

def fill_with_num(x, new_val):
    return new_val if np.isnan(x) else x



def fillFloor(x, mean):
    if x.isnumeric():
        if x != "301":
            return float(x)
        else:
            return 31.0
    else:
        return mean

def fillAnimalFurniture(x):
    if x == 'acept' or x == 'furnished':
        return 1
    else:
        return 0
## pro = project_framework(data)
## pro.clean()
