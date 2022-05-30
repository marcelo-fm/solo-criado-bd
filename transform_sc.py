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

def corrige_mz1(estoque_maximo, uso_estoque):
    uso_mz1 = uso_estoque.loc[uso_estoque['MZ'] == 1].copy()

    col_max = list(estoque_maximo.columns)
    col_uso = list(uso_estoque.columns)

    for i in range(14, len(col_uso)):
        uso_mz1[col_uso[i]] = (estoque_maximo[col_max[14]] - estoque_maximo[col_max[i]]) + uso_mz1[col_uso[i-1]]
        uso_estoque.replace(to_replace=list(uso_estoque[col_uso[i]][:1274]), value=list(uso_mz1[col_uso[i]]), inplace=True)
    
    return uso_estoque

def calcula_porcentagem(dataframe):
    coluna = list(dataframe.columns)
    uso_porcentagem = (dataframe[coluna[3:]]*100) / dataframe[coluna[3]]
    data_merged = pd.merge(left=dataframe[coluna[:3]], right=uso_porcentagem, how='outer', left_index=True, right_index=True)
    return data_merged

def calcula_uso(dataframe, is_percent=False): #arrumar
    """Receives a database containing 
    all dataframes, aggregates them, and
    calculate the use of Solo Criado."""
    if is_percent:
        prct = '%'
    else:
        prct = ''

    uso_estoque = dataframe.copy()
    dataframe = retira_ae(dataframe)
    uso_estoque = retira_ae(uso_estoque)

    colunas = list(uso_estoque.columns)
    # calcula o uso de estoque maximo.
    for i in range(4, len(colunas)):
        uso_estoque[colunas[i]] = (dataframe[colunas[3]] - dataframe[colunas[i]])
    
    # muda o nome
    for i in range(3, len(colunas)):
        if i < 12:
            colunas[i] = 'uso_estq' + prct + '_0' + str(i-2)
        else:
            colunas[i] = 'uso_estq' + prct + '_' + str(i-2)
    uso_estoque.columns = colunas
    # parece que a função corrige_mz1 não funciona dentro desta função, por isso comentei fora. Mas ainda quero descobrir o porquê
    # uso_estoque = corrige_mz1(dataframe, uso_estoque)

    if is_percent:
        uso_estoque = calcula_porcentagem(uso_estoque)
    else:
        None

    return uso_estoque

def cria_uso_estoque(estoque_maximo, is_percent=False):
    uso_estq = calcula_uso(estoque_maximo)
    uso_estq = corrige_mz1(estoque_maximo, uso_estq)

    return uso_estq