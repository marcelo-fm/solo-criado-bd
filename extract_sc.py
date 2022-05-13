import pandas as pd
import os


def join_sheet(file):
    """Receives a excel file path and
    returns a dataframe with his sheets
    appended. Also fix third column name."""

    sheet_list = pd.ExcelFile(file).sheet_names
    df_list = []
    for sheet in sheet_list:
        df_list.append(pd.read_excel(io=file, sheet_name=sheet, header=1))
    
    listagem = pd.concat(objs=df_list, ignore_index=True)
    
    colunas = listagem.columns.to_list()
    colunas[-1] = 'estq_max_' + file[-7:-5]
    listagem.columns = colunas

    return listagem

def mzueuqrt(dataframe: list):
    """Receives a dataframe, adds
    the MZUEUQRT column in the [-1]
    position, and makes it the index."""

    new_columns = list(dataframe.columns)
    new_columns.insert(-1, 'MZUEUQRT')
    dataframe = dataframe.reindex(columns=new_columns)
    #Agora vem o calculo da columa MZUEUQRT
    
    dataframe['MZUEUQRT'] = (dataframe['MZ']*1000000) + (dataframe['UEU']*1000) + (dataframe['QRT'])

    return dataframe

def db_manager(path=any, database=[]):
    """Receives a path to Excel files and 
    a list containing dataframes, checks if 
    there is any file that is not in the database, 
    adds the missing files to database if there is any 
    and returns the updated database."""

    files = os.listdir(path)
    files.sort()
    
    if len(database) == len(files): #Não há nenhum dado novo a ser adicionado
        print("O banco de dados já está atualizado.")
        return database
    elif len(database) > len(files): #Há algum problema, pois o BD possui mais entradas do que a pasta de arquivos
        print("O banco de dados possui mais entradas do que a pasta de arquivos")
        return database
    elif len(database) < len(files): #Existem novas listagens que não foram adicionadas ao BD
        print("O banco de dados está desatualizado")
        for i in range(len(database), len(files)):
            listagem = mzueuqrt(join_sheet(path + "/" + files[i]))
            listagem = listagem.set_index('MZUEUQRT')
            database.append(listagem)
            print("Adicionando listagem", (i+1))

    return database
