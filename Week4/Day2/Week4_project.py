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
    
def printEvaluations (clf, X_train, X_test, y_test):        
    """Returns Confusion Matrix and relevant metrics for predictions of classifiers.
    Takes classification model and split data."""
    #clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)   
    #print(f'How does model {clf} score:')
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

# %%
result["Artist"].replace("Radiohead",0,inplace=True)
result["Artist"].replace("Coldplay",1,inplace=True)
result

# %%

# name_csv_radiohead="final_lyrics_dataf.csv"
# name_csv_coldplay="final_cold_lyrics_df.csv"
# name_csv_table=[name_csv_radiohead,name_csv_coldplay]
# data_radiohead=make_df_ready(name_csv_radiohead)
# data_radiohead
# data_coldplay=make_df_ready(name_csv_coldplay)
# data_coldplay
# result = pd.concat([data_radiohead, data_coldplay], axis=0)

# %%
X=result["Lyrics"]
y=result["Artist"]
X.shape,y.shape


# %% [markdown]
# Split

# %% [markdown]
# #Split of Test Data

# %%
X_train1,X_test1,y_train1,y_test1=train_test_split(X,y,random_state=42)

# %%
X_train1.shape,X_test1.shape,y_train1.shape,y_test1.shape

# %% [markdown]
# #Split of the Data which remains of the Test Data

# %%
X_train,X_test,y_train,y_test=train_test_split(X_train1,y_train1,random_state=42)

# %%
X_train.shape,X_test.shape,y_train.shape,y_test.shape

# %% [markdown]
# ## Sklearn CountVectorizer

# %%
vectorizer = CountVectorizer(lowercase=True, stop_words='english', token_pattern='[A-Za-z]+', ngram_range=(1,1))
X_cv = vectorizer.fit_transform(X_train)
df_bow_sklearn = pd.DataFrame(X_cv.toarray(), columns=vectorizer.get_feature_names_out())
df_bow_sklearn

# %% [markdown]
# ## Model

# %%
text_clf=Pipeline([("vect",CountVectorizer()),("tfidf",TfidfTransformer()),("clf",RandomForestClassifier(max_depth=20))])

#column_transformer=ColumnTransformer([
#   ("text_clf",text_clf,["Lyrics"])
#])

#column_transformer.fit(X_train)
text_clf.fit(X_train,y_train)
text_clf.score(X_train,y_train)


# %%
ypred=text_clf.predict(X_test)


# %%
accuracy_score(y_test, ypred)

# %%
ypred1=text_clf.predict(X_test1)

# %%
accuracy_score(y_test1, ypred1)

# %%
#y_test=y_test.to_numpy()
print('------Model Development Test-------')
printEvaluations(text_clf,X_train,X_test,y_test)

# %%
print('---------Actual Online Model Testing----------')
printEvaluations(text_clf,X_train,X_test1,y_test1)

# %%

# %%



