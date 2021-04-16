import pandas as pd
import numpy as np

df=pd.read_html("https://www.espn.com/mlb/player/_/id/33039/mookie-betts")
betts = df[3]
betts.to_html("test.txt",index=False)

df2 = pd.read_html("https://www.espn.com/mlb/player/_/id/34886/alex-bregman")
bregman = df2[3]
bregman.to_html("test2.txt",index=False)

df3 = pd.read_html("https://www.espn.com/mlb/player/_/id/33172/kris-bryant")
bryant = df3[3]
bryant.to_html("test3.txt",index=False)

df4 = pd.read_html("https://www.espn.com/mlb/player/_/id/32796/jacob-degrom")
degrom = df4[2]
degrom.to_html("test4.txt",index=False)

df5 = pd.read_html("https://www.espn.com/mlb/player/_/id/35983/fernando-tatis-jr")
tatis = df5[3]
tatis.to_html("test5.txt",index=False)

df6 = pd.read_html("https://www.espn.com/mlb/player/_/id/30836/mike-trout")
trout = df6[3]
trout.to_html("test6.txt",index=False)

df7 = pd.read_html("https://www.espn.com/mlb/player/_/id/32081/gerrit-cole")
cole = df7[3]
cole.to_html("test7.txt",index=False,classes="pitcher")

df8 = pd.read_html("https://www.espn.com/mlb/player/_/id/31283/christian-yelich")
yelich = df8[3]
yelich.to_html("test8.txt",index=False)

df9 = pd.read_html("https://www.espn.com/mlb/player/_/id/31261/nolan-arenado")
arenado = df9[3]
arenado.to_html("test9.txt",index=False)