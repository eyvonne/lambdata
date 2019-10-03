# lambdata
A collection of DS Helper Functions

This package currently contains a class with two tools inside of it, genData and listCol. All changes that the class makes to the dataframe happen inplace They are detailed below.

## genData
The genData funciton is used to generate additional data based on the dataframe given. It uses the pandas sample method with replacement enabled.

## listCol
The listCol function takes in two arguments, a list and a name. The list is added to the dataframe and the column is named the given name. If the name is that of a column that already exists in the dataframe the column is replaced instead. 
