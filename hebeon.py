import numpy as np
import matplotlib.pyplot as
plt import pandas as pd
from google.colab import drive drive.mount("/content/drive") df=pd.read_csv('/content/drive/My Drive/Salary_Data.csv') X=
df.iloc[:,0:1].values y =
df.iloc[:, 1].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
from sklearn.linear_model import LinearRegression
30
     
   regressor = LinearRegression() regressor.fit(X_train, y_train, y_pred = regressor.predict(X_test) plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience') plt.ylabel('Salary')
plt.show()
plt.scatter(X_test, y_test, color = 'red') plt.plot(X_train, regressor.predict(X_train), color = 'blue') plt.title('Salary vs Experience (Test set)') plt.xlabel('Years of Experience') plt.ylabel('Salary')
plt.show()