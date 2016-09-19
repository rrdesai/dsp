#for my own sake, I rewrote the nessecary packages from ThinkStats2 to get some insight
#into how & why things are structured as they are.

import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

labels = '2002FemPreg.txt'
data = '2002FemPreg.dat.gz'

class FixedWidthVariables(object):

    def __init__(self, variables, index_base = 0):
        self.variables = variables
        self.colspecs = variables[['start','end']] - index_base
        self.colspecs = self.colspecs.astype(np.int).values.tolist()
        self.names = variables['name']

    def ReadFixedWidth(self, filename, **options):
        df = pd.read_fwf(filename, colspecs = self.colspecs, names = self.names, **options)

        return df


def StatData(dct_file, **options):
    types = dict(byte=int, int=int, long=int, float=int, double=float)

    var_info = []
    for line in open(dct_file, **options):
        row = re.search(r'_column\(([^)]*)\)', line)
        if row:
            start = int(row.group(1))
            t = line.split()
            vtype, name, fstring = t[1:4]
            name = name.lower()
            if vtype.startswith('str'):
                vtype = str
            else:
                vtype = types[vtype]
            long_desc = ' '.join(t[4:]).strip('"')
            var_info.append((start, vtype, name, fstring, long_desc))

    columns = ['start', 'type','name','fstring','desc']
    variables = pd.DataFrame(var_info, columns = columns)

    variables['end'] = variables.start.shift(-1)
    variables.loc[len(variables)-1, 'end'] = 0
    dct = FixedWidthVariables(variables, index_base = 1)
    return dct

def CleanData(df):
    df.agepreg /= 100.0
    df.loc[df.birthwgt_lb > 20, 'birthwgt_lb'] = np.nan
    replacement = [97, 98, 99]
    df.birthwgt_lb.replace(replacement, np.nan, inplace=True)
    df.birthwgt_oz.replace(replacement, np.nan, inplace=True)
    df.hpagelb.replace(replacement, np.nan, inplace=True)
    df.babysex.replace([7,9], np.nan, inplace=True)
    df.nbrnaliv.replace([9], np.nan, inplace=True)
    df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
    df.cmintvw = np.nan

def cohens_d(array_1, array_2):
    len1 = len(array_1)
    len2 = len(array_2)
    mean1 = array_1[~np.isnan(array_1)].mean()
    var1 = array_1[~np.isnan(array_1)].var()
    std1 = array_1[~np.isnan(array_1)].std()
    mean2 = array_2[~np.isnan(array_2)].mean()
    var2 = array_2[~np.isnan(array_2)].var()
    std2 = array_2[~np.isnan(array_2)].std()
    net_var = (len1*var1+len2*var2)/(len1+len2)
    mean_diff = mean1 - mean2
    print ' the mean difference is ', mean_diff
    d = mean_diff/math.sqrt(net_var)
    return d

dct = StatData(labels)


raw_data = dct.ReadFixedWidth(data, compression = 'gzip')
CleanData(raw_data)
live = raw_data[raw_data.outcome == 1]
first = live[live.birthord == 1]
rest = live[live.birthord != 1]

weight_diff = cohens_d(first.totalwgt_lb.as_matrix(), rest.totalwgt_lb.as_matrix())
gest_diff = cohens_d(first.prglngth.as_matrix(), rest.prglngth.as_matrix())

print "cohen's D for birth weight between first children and others is ", weight_diff
print "cohen's D for pregnancy length between first children and others is ", gest_diff

plt.hist(live.prglngth)
plt.title('Pregnancy Length for Live Births')
plt.xlabel('Weeks')
plt.ylabel('Frequency')
plt.show()


live_weights =  live.totalwgt_lb.as_matrix()
live_weights = live_weights[~np.isnan(live_weights)]
print live_weights
plt.hist(live_weights)
plt.title('Birth Weight for Live Births')
plt.xlabel('Weight (lbs)')
plt.ylabel('Frequency')
plt.show()
