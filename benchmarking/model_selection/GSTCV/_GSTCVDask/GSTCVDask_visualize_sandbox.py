# Author:
#         Bill Sousa
#
# License: BSD 3 clause
#



import numpy as np
import dask
import dask.array as da
import distributed
from dask_ml.datasets import make_classification as dask_make_classification
from dask_ml.linear_model import LogisticRegression as dask_LogisticRegression
from pybear_dask.model_selection.GSTCV._GSTCVDask.GSTCVDask import GSTCVDask



if __name__ == '__main__':

    X, y = dask_make_classification(
        n_samples=90, n_features=5, n_redundant=0,
        n_informative=5, n_classes=2, chunks=(10,5)
    )

    # X = X.compute()
    # y = y.compute()

    clf = dask_LogisticRegression(
        penalty='l2',
        dual=False,
        tol=1e-6,
        C=1.0,
        fit_intercept=True,
        intercept_scaling=1,
        class_weight=None,
        random_state=None,
        solver='lbfgs',
        max_iter=10000,
        multi_class='auto',
        verbose=0,
        warm_start=False,
        n_jobs=-1
    )

    param_grid = {'C': np.logspace(-5, -2, 4), 'solver': ['lbfgs', 'newton']}


    gstcv = GSTCVDask(
        clf,
        param_grid,
        thresholds=np.linspace(0,1,6),
        scoring='balanced_accuracy',
        n_jobs=-1,
        cv = 3,
        refit = True,
        error_score = 'raise',
        return_train_score = False,
        iid= True,
        scheduler = None,
        cache_cv = True
    )

    with distributed.Client(n_workers=None, threads_per_worker=1):
        gstcv.fit(X, y)

    dask.visualize(gstcv._estimator, filename='beartest', engine='graphviz')




































