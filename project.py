import numpy as np
import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

class project_framework(object):
    def __init__(self, data):
        self.data = data.copy()
        
    def clean(self):
        
        #Log transformation
        log_attributes = ['hoa (R$)', 'rent amount (R$)', 'property tax (R$)', 'fire insurance (R$)', 'total (R$)']
        for attr in log_attributes:
            self.data[attr] = self.data[attr] .apply(lambda x: np.log1p(x))

        #Fill the missing values
        self.data['floor'] = self.data['floor'].apply(lambda x: replace_with_nan(x, '-'))
        self.data['floor'] = self.data['floor'].astype(float)
        self.data['floor'].fillna(self.data['floor'].mean(), inplace = True)
        
        missing_attributes = ["property tax (R$)", "hoa (R$)"]
        for attr in missing_attributes:
            self.data[attr] = self.data[attr].apply(lambda x: replace_with_nan(x, 0))
        imp_mean = IterativeImputer(random_state=0)
        imp_mean.fit(self.data[missing_attributes])
        new_tax_hoa = imp_mean.transform(self.data[missing_attributes])
        self.data["property tax (R$)"] = new_tax_hoa[:, 0]
        self.data["hoa (R$)"] = new_tax_hoa[:, 1]
        
        #Drop the outliers
        outliers_attributes = ['hoa (R$)', 'property tax (R$)', 'total (R$)']
        
        for attr in outliers_attributes:
            mean = self.data[attr].mean()
            std = self.data[attr].std()
            self.data.drop(self.data[self.data[attr] - mean > 3 * std].index, inplace=True)
            self.data.drop(self.data[self.data[attr] - mean < -3 * std].index, inplace=True)
        
        self.data.drop(self.data[self.data['floor']==301].index, inplace=True)

        #Transfor categorical attribute
        self.data['animal'] = self.data['animal'].apply(lambda x: fillAnimalFurniture(x))
        self.data['furniture'] = self.data['furniture'].apply(lambda x: fillAnimalFurniture(x))
        
        onehot = pd.get_dummies(self.data['city'], drop_first = True)
        for colname in onehot:
            self.data[colname] = onehot[colname]


def replace_with_nan(x, old_val):
    return np.nan if x == old_val else x

def fill_with_num(x, new_val):
    return new_val if np.isnan(x) else x

def fillAnimalFurniture(x):
    if x == 'acept' or x == 'furnished':
        return 1
    else:
        return 0
