"""
    <=============== Day 1 of the 2-Day Data Challenge! ===============>
    Today, we're going to be looking at how to deal with missing values.

"""
# First part: Importing Libraries
import pandas as pd


# Second part: Bringing the data to the project
Data_NFL = pd.read_csv("Datasets/NFL Play by Play 2009-2017 (v4).csv")


# Third part: Starting with the NFL dataset, the first thing that we need to do is to take a look at the file
print(Data_NFL.head(5))

"""
    This function (LookingData) will use the dataframe as argument, and will look in all columns 
    that have some missing data. And in the final, it will bring a dictionary with only the columns
    that have missing data and the total of it.
    
    OBS: missing_values[missing_values > 0]
     Acontece o filtro, que verifica a coluna se tem dados faltantes (se tiver retorna como True) 
     Isso resulta em uma nova Series que contém apenas as linhas onde o valor correspondente na Series booleana é True.
    
"""


def LookingData(dataframe):
    missing_values = dataframe.isnull().sum()                        # Search and sum the total of missing values
    columns_mv = missing_values[missing_values > 0].index.tolist()   # Will return a list of columns names that have missing value
    if len(columns_mv) > 0:
        return missing_values[columns_mv].to_dict()
    else:
        return "There are no missing values in your dataframe"


# Forth part: As we can see, there are some missing values, so we need to know how many and where they are
Missing_values_NFL = LookingData(Data_NFL)
# print(Missing_values_NFL)

# Fifth part: Now we need to remove all the rows or the columns that have missing data, if this project was important
# we should find why there are missing values in each column

# Data_NFL = Data_NFL.dropna()                      # After that we realize that all rows had at least one missing data
Data_NFL_02 = Data_NFL.dropna(axis=1)               # So we will remove the columns that have at least one missing data
# print(Data_NFL.head(5))
print(f"Columns in original Dataset: {Data_NFL.shape[1]} ")
print(f"Columns in original Dataset: {Data_NFL_02.shape[1]} ")

"""
    Data_NFL.shape[1] return a tuple with the dimension of dataset (columns,rows)
    
    <=========== Replacing Missing Data ===============>
        If we want, we can replace the missing data with two options
            . (1) Replacing the missing data with the value 0
            . (2) Replacing each missing data for each column with the media of that column
            . (3) Replacing the missing data for the value of the next value
            
    ==> (1) Replacing the missing data with the value 0
        Data_NFL.fillna(0)  
         
         
         
    ==> (2) Replacing each missing data for each column with the media of that column
        Data_NFL.fillna(Data_NFL.mean())
            
        data = {
            'coluna1': [1, 2, None, 4, None],
            'coluna2': [None, 5, 6, None, 8],
            'coluna3': [10, None, 12, 13, 14]
        }
        
        df = pd.DataFrame(data)
        
        # Preencha os dados vazios de cada coluna com a média da mesma coluna
        df = df.fillna(df.mean())
        
        print(df)
           
           
                
    =>> (3)
    
    fillna(method='bfill', axis=0): O método fillna é utilizado para preencher os valores ausentes (NaN) no DataFrame
    subset_nfl_data. Neste caso, estamos usando o parâmetro method='bfill', que significa "backward fill". Isso indica 
    que os valores ausentes serão preenchidos com os valores da próxima linha não nula (para frente) ao longo do eixo 0
    (ou seja, ao longo das linhas).

    fillna(0): Após preencher os valores ausentes com a estratégia de "backward fill", este segundo fillna é usado para 
    substituir quaisquer valores ausentes restantes com o valor 0. Isso garante que todos os valores ausentes que não 
    puderam ser preenchidos com o método "backward fill" serão agora preenchidos com o valor 0.
    
    Data_NFL.fillna(method = 'bfill', axis=0).fillna(0)
        
"""

