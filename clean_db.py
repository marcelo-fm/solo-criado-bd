import pandas as pd

def mzueuqrt(dataframe):
    """Receives a dataframe and adds
    the MZUEUQRT column in the [-1]
    position."""

    new_columns = list(dataframe.columns)
    new_columns.insert(-1, 'MZUEUQRT')
    dataframe = dataframe.reindex(columns=new_columns)
    #Agora vem o calculo da columa MZUEUQRT
    dataframe['MZUEUQRT'] = (dataframe['MZ']*1000000) + (dataframe['UEU']*1000) + (dataframe['QRT'])

    return dataframe