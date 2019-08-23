import pandas as pd
import random

df=pd.read_csv("angry.csv")
df_top=(df.columns)[0]
print(df_top)
count=df[df_top].count()
print("total= ",count)
random_index = random.randrange(0, count, 1)
print(random_index)
song_name=df[df_top][random_index]
print(song_name)
