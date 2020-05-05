class project_framework(object):
    def __init__(self, data):
        self.data = data
    def clean(self):
        self.data['hoa (R$)'] = self.data['hoa (R$)'] .apply(lambda x: np.log1p(x))
        self.data['rent amount (R$)'] = self.data['rent amount (R$)'] .apply(lambda x: np.log1p(x))
        self.data['property tax (R$)'] = self.data['property tax (R$)'].apply(lambda x: np.log1p(x))
        self.data['fire insurance (R$)'] = self.data['fire insurance (R$)'].apply(lambda x: np.log1p(x))
        self.data['total (R$)'] = self.data['total (R$)'].apply(lambda x: np.log1p(x))
        count = 0
        total = 0
        for floor in self.data["floor"]:
            if floor != '-':
                if floor != "301":
                    total += int(floor)
                else:
                    total += 31
                count += 1
        mean = total / count
        self.data['floor'] = self.data['floor'].apply(lambda x: fillFloor(x, mean))
        self.data['animal'] = self.data['animal'].apply(lambda x: fillAnimalFurniture(x))
        self.data['furniture'] = self.data['furniture'].apply(lambda x: fillAnimalFurniture(x))
        
        onehot = pd.get_dummies(self.data['city'], drop_first = True)
        for colname in onehot:
            self.data[colname] = onehot[colname]
        self.data.drop(columns = ['city'], inplace = True)

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
