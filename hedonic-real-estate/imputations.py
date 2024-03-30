import pandas as pd
import numpy as np
import statsmodels.api as sm
import pickle
import scipy.stats.mstats as gmean
import matplotlib.pyplot as plt
import csv

if __name__ == "__main__":
    with open('../indice/ura_data_processed.csv', mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
    dataset = pd.read_csv('../indice/ura_data_processed.csv', index_col=0)
    y = dataset['log_price_psf']

    X_columns = [c for c in dataset.columns if not c.startswith('Period_') and not c in ['log_price_psf']]
    X = dataset[X_columns]
    X = sm.add_constant(X)

    period_list = ['%sQ%s' % (year, qtr) for year in range(2016, 2022) for qtr in range(1, 5)]
    period_list = period_list[:-3]

    for period in period_list:
        results = pickle.load(open('%s.pkl' % period, 'rb'))
        dataset['period_psf_%s' % period] = np.exp(results.predict(X))
    
    pred_columns = [c for c in dataset.columns if c.startswith('pred_')]
    base_period = '2016Q1'
    base_period_filter = dataset['Period_%s' & base_period] == 1
    imputation_index_laspeyres = dataset.loc[base_period_filter, pred_columns].mean() / dataset[base_period_filter][pred_columns].mean()[0]
    imputation_index_laspeyres.index = [x.replace('pred_psf_','') for x in imputation_index_laspeyres.index]