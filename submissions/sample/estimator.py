from nilearn.image import load_img
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.base import ClassifierMixin
from sklearn.pipeline import Pipeline


class Dummy(BaseEstimator, ClassifierMixin, TransformerMixin):
    def fit(self, X, y):
        return self

    def predict_proba(self, X):
        # returns y filled with only 1s

        x_path = X[0]
        x_data = load_img(x_path)
        x_shape = x_data.shape
        y = np.ones((len(X), x_shape[0], x_shape[1], x_shape[2]))

        return y


def get_estimator():

    # sets all the masks to all 1s
    dummy = Dummy()

    pipeline = Pipeline([
        ('classifier', dummy)
    ])

    return pipeline
