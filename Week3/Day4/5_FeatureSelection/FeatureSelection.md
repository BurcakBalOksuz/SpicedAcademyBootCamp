# Feature Selection
Irrelevant or partially irrelevant features can negatively impact your model performance.
FS and data cleaning should be first and most important steps.
Automatically or manually select features which contribute most.

## De-select if... 
* Domain knowledge (you know what is important)
* Too many missing values in a feature or a constant feature (very low variance)
* Features dependent on each other (INdependent variable)
* Target not dependent on features (dependent variable)

## Methods
See also [here](https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/)
### 1. Filter methods    
* Apply methods to filter features    
    ```sklearn.feature_selection.SelectKBest```    
    Numerical Input - Numerical Output: `f_regression`     (Pearson Correlation)       
    Numerical Input - Categorical Output: `f_classif` (ANOVA) ([nice link](https://towardsdatascience.com/anova-for-feature-selection-in-machine-learning-d9305e228476))   
    Categorical Input - Categorical Output: `chi2` ([nice link](https://towardsdatascience.com/chi-square-test-for-feature-selection-in-machine-learning-206b1f0b8223))
### 2. Wrapper methods
* **Recursive Feature Elimination** (REF), rank features and select best
### 3. Embedded methods
* Automatic feature selection - e.g. Regularization    
    **LASSO** (L1 regularization)    
    (**RIDGE** (L2 regularization))   
    **ElasticNet** (L1 + L2 regularization)

## Get the index in a pythonic `for` loop
See [this link](https://dev.to/wangonya/when-to-use-python-s-enumerate-instead-of-range-in-loops-3e03)