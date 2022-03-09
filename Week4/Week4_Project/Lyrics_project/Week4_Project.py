# %%
import numpy as np
import re
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, recall_score, precision_score, ConfusionMatrixDisplay,f1_score
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt



# %%
np.random.seed(31415)

# %% [markdown]
# ## Definition of Function

# %%
def make_df_ready(name_csv):
    df=pd.read_csv(name_csv)
    df=df.drop("Unnamed: 0",axis=1)
    df=df.drop_duplicates(subset=["Lyrics"])
    df.reset_index(drop=True,inplace=True)
    return df

def prepare_final_df(name_csv_table):
    final_df=pd.DataFrame()
    for iter in range(len(name_csv_table)):
        final_df_temp=make_df_ready(name_csv_table[iter])
        final_df = pd.concat([final_df, final_df_temp], axis=0)
    return final_df
    
def printEvaluations (clf, X_test,y_test):        
    """Returns Confusion Matrix and relevant metrics for predictions of classifiers.
    Takes classification model and split data."""
    y_pred = clf.predict(X_test)   
    print(f'How does model {clf} score:')
    print(f'The accuracy of the model is: {round(accuracy_score(y_test, y_pred), 3)}')
    print(f'The precision of the model is: {round(precision_score(y_test, y_pred), 3)}')
    print(f'The recall of the model is: {round(recall_score(y_test, y_pred), 3)}')

    #print confusion matrix
    disp=ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test, cmap='Greens')
    disp.plot()
    plt.show()
    

# %%
name_csv_radiohead="final_lyrics_dataf.csv"
name_csv_coldplay="final_cold_lyrics_df.csv"
name_csv_table=[name_csv_radiohead,name_csv_coldplay]

# %%
result=prepare_final_df(name_csv_table)
result

# %% [markdown]
# ## Assigning 0 and 1 to columns

# %%
result["Artist"].replace("Radiohead",0,inplace=True)
result["Artist"].replace("Coldplay",1,inplace=True)
result

# %% [markdown]
# ## Defining of X and y

# %%
X=result["Lyrics"]
y=result["Artist"]
X.shape,y.shape


# %% [markdown]
# ## Split of Data

# %% [markdown]
# #Split of Test Data

# %%
X_train1,X_test1,y_train1,y_test1=train_test_split(X,y,random_state=42)

# %%
X_train1.shape,X_test1.shape,y_train1.shape,y_test1.shape

# %% [markdown]
# #Split the Remaining Test Data as Train and Test Data

# %%
X_train,X_test,y_train,y_test=train_test_split(X_train1,y_train1,random_state=42)

# %%
X_train.shape,X_test.shape,y_train.shape,y_test.shape

# %% [markdown]
# ## Sklearn CountVectorizer

# %%
# vectorizer = CountVectorizer(lowercase=True, stop_words='english', token_pattern='[A-Za-z]+', ngram_range=(1,1))
# X_cv = vectorizer.fit_transform(X_train)
# df_bow_sklearn = pd.DataFrame(X_cv.toarray(), columns=vectorizer.get_feature_names_out())
# df_bow_sklearn

# %% [markdown]
# ## Model

# %%
np.random.seed(31415)
text_clf=Pipeline([("vect",CountVectorizer()),("tfidf",TfidfTransformer()),("clf",RandomForestClassifier())])
text_clf.fit(X_train,y_train)
ypred=text_clf.predict(X_test)
accuracy_score(y_test, ypred)


# %%
ypred1=text_clf.predict(X_test1)
accuracy_score(y_test1, ypred1)

# %%
#y_test=y_test.to_numpy()
printEvaluations(text_clf,X_test,y_test)

# %%
printEvaluations(text_clf,X_test1,y_test1)

# # %% [markdown]
# # ## Grid Search

# # %%
# from sklearn.model_selection import RandomizedSearchCV


# # %%
# np.random.seed(31415)
# # Number of trees in random forest
# clf__n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# # Number of features to consider at every split
# clf__max_features = ['auto', 'sqrt']
# # Maximum number of levels in tree
# clf__max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
# clf__max_depth.append(None)
# # Minimum number of samples required to split a node
# clf__min_samples_split = [2, 5, 10]
# # Minimum number of samples required at each leaf node
# clf__min_samples_leaf = [1, 2, 4]

# # %%
# random_grid = {'clf__n_estimators': clf__n_estimators,
#                'clf__max_features': clf__max_features,
#                'clf__max_depth': clf__max_depth,
#                'clf__min_samples_split': clf__min_samples_split,
#                'clf__min_samples_leaf': clf__min_samples_leaf
#                }

# # %%
# np.random.seed(31415)
# rf_random = RandomizedSearchCV(estimator = text_clf, param_distributions = random_grid, n_iter = 1000, cv = 10, verbose=1, random_state=np.random.seed(31415), n_jobs = -1)
# # Fit the random search model
# rf_random.fit(X_train, y_train)

# # %%
# rf_random.best_params_

# # %%
# from sklearn.model_selection import GridSearchCV
# np.random.seed(31415)
# params_grid_search={'clf__n_estimators': [50,100,300,400,500],
#  'clf__min_samples_split': [3,4,5,6,7],
#  'clf__min_samples_leaf': [1,2,3,4],
#  'clf__max_depth': [80,90,100,110],
#  "clf__max_features": ["auto"]}
# Random_GS = GridSearchCV(estimator=text_clf,param_grid=params_grid_search, n_jobs=-1)
# Random_GS.fit(X_train,y_train)
# Random_GS.best_params_

# # %%
# ypred1=Random_GS.predict(X_test1)
# accuracy_score(y_test1,ypred1)

# # %%
# printEvaluations(Random_GS,X_test,y_test)

# # %%
# printEvaluations(Random_GS,X_test1,y_test1)


