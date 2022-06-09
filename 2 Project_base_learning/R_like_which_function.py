#https://alex.miller.im/posts/python-pandas-which-function-indices-similar-to-R/
import pandas as pd

def which(self):
    try:
        self = list(iter(self))
    except TypeError as e:
        raise Exception("""'which' method can only be applied to iterables.
        {}""".format(str(e)))
    indices = [i for i, x in enumerate(self) if bool(x) == True]
    return(indices)

#print(which(self))
# If you want to apply it as a class method to Pandas Series objects
pd.Series.which = which
#Just to give you a feel for how it works, I’ll load some toy data:

from io import StringIO
toy_data = StringIO("""A;B
    4.4;99
    4.5;200
    4.7;65
    3.2;140
""")
df = pd.read_csv(toy_data, sep=";")
print(df)


#With our toy dataframe, we can apply which to the columns as an outer function:

print(which(df.A > 4))
#[0, 1, 2]
#Or, if you’ve defined the class method, you can call .which() like any other Pandas method:

print((df.B == 200).which())
#[1]
#Just like in R, it works perfectly well for indexing:

print(df.loc[which(df.B < 100), ['A']])

'''
     A
0  4.4
2  4.7
'''
#Hopefully this function can ease some of the pains of switching between R and Pandas.