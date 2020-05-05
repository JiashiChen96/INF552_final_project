## INF 552 Final Project

Link: [Kaggle Contest](https://www.kaggle.com/rubenssjr/brasilian-houses-to-rent)

#### Data source

`houses_to_rent_v2.csv`

### Feature Engineer:

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