import pandas as pd
import os


def estoque_maximo(database):
    """Receives a database containing 
    all dataframes, and aggregates them."""

    estq_max = database[0]

    for i in range(1, len(database)):
        if i < 9: #Somente para não ter erro com a coluna da direita        \/
            estq_max = pd.merge(left=estq_max, right=database[i][('estq_max_0'+str(i+1))], how='outer', on='MZUEUQRT')
        else:
            estq_max = pd.merge(left=estq_max, right=database[i][('estq_max_'+str(i+1))], how='outer', on='MZUEUQRT')
    
    return estq_max

def retira_ae(dataframe):
    colunas = list(dataframe.columns)

    for i in range(3, len(colunas)):
        area_especial = list(dataframe.index[dataframe[colunas[i]] == 'AE'])
        dataframe.drop(labels=area_especial, axis=0, inplace=True)
    
    return dataframe

def retorna_ae(dataframe):
    colunas = list(dataframe.columns)

    for i in range(3, len(colunas)):
        area_especial = list(dataframe.index[dataframe[colunas[i]] != 'AE'])
        dataframe.drop(labels=area_especial, axis=0, inplace=True)
    
    return dataframe

def calcula_uso(dataframe, is_percent=False): #arrumar
    """Receives a database containing 
    all dataframes, aggregates them, and
    calculate the use of Solo Criado."""
    if is_percent:
        percent = (100 / dataframe[3])
        prct = '%'
    else:
        percent = 1
        prct = ''

    uso_estoque = dataframe.copy()
    uso_estoque = retira_ae(uso_estoque)

    colunas = list(uso_estoque.columns)

    for i in range(4, len(colunas)):
        uso_estoque[colunas[i]] = (dataframe[colunas[3]] - dataframe[colunas[i]]) * percent
    
    # muda o nome
    for i in range(3, len(colunas)):
        if i < 12:
            colunas[i] = 'uso_estq' + prct + '_0' + str(i-2)
        else:
            colunas[i] = 'uso_estq' + prct + '_' + str(i-2)
    uso_estoque.columns = colunas

    return uso_estoque