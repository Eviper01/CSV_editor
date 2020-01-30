import csv
import pandas as pd
#csve file.csv (startx,starty) (endx,endy) operation
def load(df,file,header=None):
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


df = None
print("intialised")
while True:
    action = input(">")
    df = exec(action)
