from ucimlrepo import fetch_ucirepo # fetch dataset
rt_iot2022 = fetch_ucirepo(id=942) # data (as pandas dataframes)
X = rt_iot2022.data.features
y = rt_iot2022.data.targets
# The next lines of code are only informative/diagnostic
#print(rt_iot2022.metadata) # this allows you to see the dataset metadata print(rt_iot2022.variables) # allows you to see the variables
#print(rt_iot2022.variables) # allows you to see the variables

#OneHotEncoder to preprocess X dataset
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

categorical_columns = X.select_dtypes(include = ['object']).columns

one_hot_encoder = OneHotEncoder(sparse_output= False).set_output(transform='pandas')

encoded_categorical = one_hot_encoder.fit_transform(X[categorical_columns])
#drop categotcal column from x data set
X.drop(columns = categorical_columns, inplace = True)

#concat the encoded column to x data set
X = pd.concat([X, encoded_categorical], axis= 1)

#Label encoder to preprocess y dataset
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y.values.ravel())
y_df_encoded = pd.DataFrame(y_encoded, columns=['Encoded_Target'])


#logistic regression
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#transforn x to scaler
scaler = StandardScaler()
X = scaler.fit_transform(X)

#divide train and test dataset 
X_train, X_test, y_train, y_test = train_test_split(X, y_df_encoded, test_size=0.2, random_state=42)

#no regularizastion

model_no_regularization = LogisticRegression(penalty=None, solver='saga', max_iter=1000, random_state=42)
model_no_regularization.fit(X_train, y_train)
accuracy_no_regularization = accuracy_score(y_test, model_no_regularization.predict(X_test))

#l2 ridge

model_l2_regularization = LogisticRegression(penalty='l2', solver='saga', max_iter=1000, random_state=42)
model_l2_regularization.fit(X_train, y_train)
accuracy_l2_regularization = accuracy_score(y_test, model_l2_regularization.predict(X_test))

#l1 lasso

model_l1_regularization = LogisticRegression(penalty='l1', solver='saga', max_iter=1000, random_state=42)
model_l1_regularization.fit(X_train, y_train)
accuracy_l1_regularization = accuracy_score(y_test, model_l1_regularization.predict(X_test))

#elastic net

model_elastic_net = LogisticRegression(penalty='elasticnet', l1_ratio=0.5, solver='saga', max_iter=1000, random_state=42)
model_elastic_net.fit(X_train, y_train)
accuracy_elastic_net = accuracy_score(y_test, model_elastic_net.predict(X_test))

#pca

from sklearn.decomposition import PCA

pca = PCA(n_components=0.99)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

model_pca = LogisticRegression( solver='saga', max_iter=1000, random_state=42)
model_pca.fit(X_train_pca, y_train)
accuracy_pca = accuracy_score(y_test, model_pca.predict(X_test_pca))

print("Accuracy of noregularization ", accuracy_no_regularization)
print("Accuracy of l2 ridge ", accuracy_l2_regularization)
print("Accuracy of l1 lasso ", accuracy_l1_regularization)
print("Accuracy of elasctic net ", accuracy_elastic_net)
print("Accuracy of pca ", accuracy_pca)
