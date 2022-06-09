__author__ = 'Administrator'
def function(a, b):
    print(a, b)

#apply(function, ("whither", "canada?"))
#apply(function, (1, 2 + 3))
function(*("whither", "canada?"))
function(*(1, 2 + 3))
function(**{"a": "crunchy", "b": "frog"})