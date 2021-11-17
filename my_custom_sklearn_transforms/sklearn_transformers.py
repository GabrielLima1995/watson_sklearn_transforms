from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing  import LabelEncoder


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')


class putMean(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        data['EXISTING_SAVINGS'] = data['EXISTING_SAVINGS'].\
        replace('UNKNOWN',1365.38).astype('float')
        data['CHECKING_BALANCE'] = data['CHECKING_BALANCE'].\
        replace('NO_CHECKING',518.1573).astype('float')
        return data 

class Enconde(BaseEstimator, TransformerMixin):
    def __init__(self,columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do DataFrame 'X' de entrada
        data = X.copy()
        data[self.columns] = \
        data[self.columns].\
        apply(LabelEncoder().fit_transform) 

        return data


