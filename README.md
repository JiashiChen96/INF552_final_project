## INF 552 Final Project

Link: [Kaggle Contest](https://www.kaggle.com/rubenssjr/brasilian-houses-to-rent)

#### Data source

`houses_to_rent_v2.csv`

### Feature Engineer:

<img src="/Users/jiashichen/Study/Kaggle/brazilian_houses_to_rent/brasilian-houses-to-rent/img/original data.png" alt="original data" style="zoom:50%;" />

![boxplot](/Users/jiashichen/Study/Kaggle/brazilian_houses_to_rent/brasilian-houses-to-rent/img/original data box.png)

We can see from praphys above that these data are right skewed. In this case, we try to use log transformation to make the distribution less skewed.

![new data distribution](/Users/jiashichen/Study/Kaggle/brazilian_houses_to_rent/brasilian-houses-to-rent/img/new data distribution.png)

 Combined these with the boxplot, we think there are many outliers exist. In this way, we try to use 3 sigma method to get rid of outliers.

![](/Users/jiashichen/Study/Kaggle/brazilian_houses_to_rent/brasilian-houses-to-rent/img/std-dev-normal.jpg)





About the attribute 'floor', we will transform '-' and '301' to mean.

![](/Users/jiashichen/Study/Kaggle/brazilian_houses_to_rent/brasilian-houses-to-rent/img/multiple imputation.png)

I use *Multivariate imputation by chained equations* to fill the miss data *hoa* and *property tax*.

Step:

We have four variables hoa, property tax, rent amount and fire insurance so $Y_1, Y_2, Y_3, Y_4$

The number of inputed data set is 2. So we have $Y^{(h)} where \ h =1, 2...,10$

With the help of sklearn module, we apply *Bayesian Ridge Regression* to $Y^{(h)}$

Eventually, we compare these 10 esitimated value and return the best value.

- Clean data source
- Deal with null values(Drop it / fill it by ml algorithm)
- Deal with outliers(Use log / drop first and last quarter)
- Deal with label like animal ....

| Attribute           | Process               |
| ------------------- | --------------------- |
| City                | One-Hot Encoding      |
| Animal              | Integer Encoding      |
| furnished           | Integer Encoding      |
| Floor               | replace "-" with mean |
| hoa (R$)            | Apply *log*           |
| rent amount (R$)    | Apply *log*           |
| property tax (R$)   | Apply *log*           |
| fire insurance (R$) | Apply *log*           |
| Total               | Apply *log*           |



### Model

#### Attribute reduction

- PCA

#### Classification

- K-means(Use Silhouette Score to evaluate clusters)

#### Predict

K fold cross-validate

- Linear Regression
- Decision Tree



### Variable Name Conventions

$sth\_(attribute/process)$