import sys
import csv
import pandas as pd
#df[x] index a collum
#df.loc[x] index a row
#df[x][y] index a coor
#csve file.csv (startx,starty) (endx,endy) operation
def init_df():
    try:
        starty = sys.argv[2]
        startx = sys.argv[3]#gonna need to reformat these
        endy = sys.argv[4]
        endx = sys.argv[5]
        df =  pd.read_csv(sys.argv[1],header=None)
        print(df)
        df = df.loc[startx:endx,starty:endy]
        return df
    except Exception as e:
        print("Invalid CSV file or slices")


def nothing(df):
    return df

def sortbyrow(df):
    out = []
    for index, row in df.iterrows():
        group = list(row)
        print(group)
        group.sort()
        out.append(group)
    return pd.DataFrame.from_records(out)


dispatcher = {"nothing":nothing,
            "sortbyrow":sortbyrow
            }

df = init_df()
print("reading in:")
print(df.to_string())
print("formated to:")
#try:
out_df = dispatcher[sys.argv[6]](df)
print(out_df)
print("saved to: out.csv")
out_df.to_csv("out.csv")
#except:
#    print("Invalid operation or error during operation")
