file_name =  'new/ia.xlsx'
sheet =  0 # sheet name or sheet number or list of sheet numbers and names
categories = []
values = []

selectedValues=[]
selectedText=[]

valuesTable = []
# values.append([])



import pandas as pd
df = pd.read_excel(io=file_name, sheet_name=0)

dfVal = pd.read_excel(io=file_name, sheet_name=1)

for row in dfVal.index:
    # if col == 'Valor':
    #     # for row in col
    # if col == 'Valor.1':
    valuesTable.append((dfVal.iat[row,2],dfVal.iat[row,1]))
    
    
# categories.remove("Caso")
# print(dfVal.head)
# print(valuesTable)


possibleValues = ([value for (selection,value) in valuesTable if selection == 'Julho'])

print(possibleValues)
