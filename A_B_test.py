import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.utils import resample

def bootstrap(arr,n_boots):
    '''
    variables:
        arr = the data that we are random sampling from
        n_boots = the number of bootstraps we want to make
    
    returns:
        list of lists containing the number of bootstrap
        samples we wanted to make
    '''
    return [resample(arr) for _ in xrange(n_boots)]

def bootstrap_means(boots):
    '''
    variables:
        boots = our list of lists of the individual bootstraps
        
    returns:
        list of all of the means of the individual bootstraps
    '''
    return [np.mean(boot) for boot in boots]
    


#boots = bootstrap([0,1,2,3,4,5,6,7,8,9],100000)
#boot_means = bootstrap_means(boots)


#plt.hist(boot_means, bins = 20)
#plt.xlabel('Boot Means')
#plt.ylabel('Frequency')


df = pd.read_csv('data/Grades-Table 1.csv')
print df.head()
