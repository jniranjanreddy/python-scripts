#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())
#print(df)