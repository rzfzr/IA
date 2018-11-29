file_name =  'new/ia.xlsx'
sheet =  0 # sheet name or sheet number or list of sheet numbers and names
categories = []
values = []

selectedValues=[]
selectedText=[]

valuesTable = []

calculated = []
# values.append([])

import pandas as pd
df = pd.read_excel(io=file_name, sheet_name=0)

dfVal = pd.read_excel(io=file_name, sheet_name=1)


for row in dfVal.index:
    # if col == 'Valor':
    #     # for row in col
    # if col == 'Valor.1':
    valuesTable.append((dfVal.iat[row,2],dfVal.iat[row,1]))
# print(valuesTable)

# categories.remove("Caso")
# print(dfVal.head)




for col in df.columns:
    categories.append(col)
categories.remove("Caso")
categories.remove("DescDoenca")

# for cat in categories:
#     print(cat)

for cat in categories:
    # values.append[col]
    rows = df.index
    for row in rows:
            values.append((cat, df.iat[row,categories.index(cat)+2]))

values.pop(0)

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
      
values = (Remove(values)) 

# values = list(set(values))
# for value in values:
#     `print`(value)
# print(values)

print(df.iat[1,2])
