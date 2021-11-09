# 11-09-2021 Pandas
# **SERIES**
"""
 call libraries
"""
import numpy as np
import pandas as pd
from numpy.random import randn

## make series
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

### array series
print( pd.Series( data = my_data) )

### dictionary-like series
#### note that it is pd.Series(data,index)
print( pd.Series(data = my_data, index = labels) )
print( pd.Series(d) ) # gets the direct format from dictionary.

### Series with arrays
print( pd.Series(arr,labels) )

### Series holds functions also
print( pd.Series(data=[sum,print,len]) )

## Grabbing information from Series
ser1 = pd.Series([1,2,3,4],
['USA','Germany','USSR','Korea'])
print( ser1 )

ser2 = pd.Series([1,2,5,4],
['USA','Germany','Italy','Korea'])
print( ser2 )

ser1['USSR']
ser2['Italy']

ser3 = pd.Series(data=labels)

## operations between two series will try to match the indexes.
### USA will add with USA, USSR and Italy is unique in each series, so will return NaN.
print( ser1 + ser2 )

# **DATAFRAMES**
## make dataframes
np.random.seed(101)
df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print( df )

## print columns ex. W column
print( df['W'] )
print( type(df) ) # dataframe.
print( type(df['W']) ) # series, list from a dataframe.
print( df.W ) # this is not recommended as sometimes this can overwrite a specific df. function.
print( df[['W','Z']] ) # this will give out dataframe.

## create new column
df['new'] = df['W'] + df['Y']
print( df )

## remove columns
print( df.drop('new' , axis = 1) )# axis 0 is row, axis 1 is column.

## inplace= True will replace the old dataframe
print( df.drop('new' , axis = 1, inplace = True) )
print( df )

## dropping rows
print( df.drop('E') )

## numpy matrix reference.
print( df.shape ) # (5,4) comes out, so it's 5 rows 4 columns.

## print or select rows
"""
this is super important.
"""
print( df.loc['A'] ) # label, or location-based row
print( df.iloc[0] ) # index-based row

## printing the indexed values
print( df.loc['B','Y'] )
print( df.loc[ ['A','B'],['W','Y'] ] )
print( df.iloc[ :2,[0,2] ] )

## Conditional selection
print( df > 0 )
print( df[df > 0] )
print( df['W'] > 0 )

### Most important example, commonly used.
print( df[ df['W'] > 0 ])
print( df[ df['Z'] < 0 ])
resultdf = df[ df['W'] > 0 ]
print( resultdf['X'] )

## one line commands that should be used more often.
print( df[ df['W'] > 0 ]['X'] )
print( df[ df['W'] > 0 ][['X','Y']] )

### expanded version.
boolser = df['W'] > 0
result = df[boolser]
print(result)
mycols=['X','Y']
print( result[mycols] )

## Multiple conditions
'''
df[ ( df['W']>0 ) and (df['W']<2) ] # this spits out error
'''
print( df[ ( df['W']>0 ) & (df['W']<2) ] )  # & for and
print( df[ ( df['W']>0 ) | (df['Y']>1) ] )  # | for or

## make a rownames to a column[0]
### makes a numerical index as rownames.
print( df.reset_index() ) 

## index name change trick
newind = 'CA NY WY OR CO'.split()
print( newind )
df['States'] = newind
print( df )
print( df.set_index('States') ) #this will lose the old index info!

## multi-level index and hierarchy
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list( zip(outside,inside) )
hier_index = pd.MultiIndex.from_tuples( hier_index )

print( outside )
print( inside )
print( hier_index )

df = pd.DataFrame( randn(6,2), hier_index, ['A','B'] )
print(df)
print( df.loc['G1'] )
print( df.loc['G1'].loc[1])
print( df.index.names )
df.index.names = ['Groups','Num']
print( df )

## calling the hierarchy G2, 2, B
print( df.loc['G2'].loc[2]['B'] )

## cross-section example (ADVANCED)
print( df.xs('G1') )

### good for selecting items in Num = 1 in G1 and G2
print( df.xs(1,level='Num') )

## Missing data
### Please note Pandas will usually fill in the missing values with NaN or null by default.
d = {'A':[1,2,np.nan], 'B':[5,np.nan,np.nan], 'C':[1,2,3]}
df = pd.DataFrame(d)
print( df )
print( df.dropna() )
print( df.dropna(thresh=2) ) #thresh is >=2 NaNs in a row.

## replace NaN with some value
print( df.fillna(value='FILL VALUE') )

## Groupby Statements
"""
Groupby allows you to group together rows based off of a column and perform an aggregate function on them.
"""
### example: choose a column to group by and sum the values in column2 that have the same values in the groupby_column.

data = { 'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350] }

df = pd.DataFrame(data)
print(df)

### note that the non-numeric columns are ignored for math operations
byComp = df.groupby('Company') #groupby object
print( byComp.mean() ) 
print( byComp.std() )
print( byComp.sum() )
print( byComp.sum().loc['FB'] )

### in one line.
print( df.groupby('Company').sum().loc['FB'] )
print( df.groupby('Company').min() )

## describe in groupby
print( df.groupby('Company').describe() )
print( df.groupby('Company').describe().transpose )

### only FB
print( df.groupby('Company').describe().transpose()['FB'] )

"""
Merging joining and Concat using ipynb
"""