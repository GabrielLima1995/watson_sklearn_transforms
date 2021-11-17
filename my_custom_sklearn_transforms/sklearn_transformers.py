from sklearn.base import BaseEstimator, TransformerMixin


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
        replace('UNKNOWN',mean_value_esavings).astype('float')
        data['CHECKING_BALANCE'] = data['CHECKING_BALANCE'].\
        replace('NO_CHECKING',mean_value_cbalance).astype('float')
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
        apply(preprocessing.LabelEncoder().fit_transform) 

        return data


