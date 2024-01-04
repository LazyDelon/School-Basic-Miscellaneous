#
```
https://scikit-learn.org/stable/

```

#
```
from sklearn import linear_model

reg = linear_model.LinearRegression()

reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

reg.coef_

```
```
from sklearn import linear_model

reg = linear_model.LinearRegression()
物件變數   < ===     


reg.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])

reg.coef_
```
```
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

Ordinary least squares Linear Regression.


class sklearn.linear_model.LinearRegression(
*, 
fit_intercept=True, 預設為真
normalize=False, 
copy_X=True, 
n_jobs=None, 
positive=False)
```
