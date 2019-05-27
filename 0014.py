import json
import pandas as pd
with open('0014.txt', 'r') as f:
    a = json.load(f)
df = pd.DataFrame.from_dict(a).T
writer = pd.ExcelWriter('0014.xlsx')
df.to_excel(writer, 'Sheet1')