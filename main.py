import csv
import pandas as pd
#csve file.csv (startx,starty) (endx,endy) operation
def load(df=None,file='data.csv',header=None):
    #try:
        df =  pd.read_csv(file,header=header)
        print(df)
        return df
    #except Exception as e:
        print("Invalid CSV file")
    #    print(e)


def slice(df,start,end):
    df = df.loc[start[0]:end[0],start[1]:end[1]]
    print(df)
    return df

def sortbyrow(df):
    out = []
    for index, row in df.iterrows():
        group = list(row)
        group.sort()
        out.append(group)
    return pd.DataFrame.from_records(out)

def saveas(df,file):
    print("saved")
    df.to_csv(file,header=None,index=False)
    return df

def peakrow(df,index):
    print(df.loc[index])
    return df

def peak(df,x,y):
    print(df[x][y])
    return df

def poke(df,x,y,str):
    df[x][y] = str
    return df

def search(df,str):
    for col in df:
        print(col,df[col].str.contains(str))
    return df


print("intialised")
while True:
    action = input(">")
    try:
        exec(action)
    except Exception as e:
        print(e)
