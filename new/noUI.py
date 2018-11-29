file_name =  'new/ia.xlsx'
sheet =  0 # sheet name or sheet number or list of sheet numbers and names
categories = []
values = []

selectedValues=[]
selectedText=[]

valuesTable = []

fields = 3

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
for value in values:
    print(value)
# print(values)
# print('tst')


# cells = sheet['A1': 'B6']

# for c1, c2 in cells:
#     print("{0:8} {1:8}".format(c1.value, c2.value))

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# import openpyxl
# book = openpyxl.load_workbook('./new/ia.xlsx')
# sheet = book.active

# cells = sheet['A1': 'B6']




# for c1, c2 in cells:
#     print("{0:8} {1:8}".format(c1.value, c2.value))

def GetValue(sel):
    # if sel.isdigit():
    #     return sel
    # else:

    possibleValues = ([value for (selection,value) in valuesTable if selection == sel])

    
    # print('selection:',sel,'value:',possibleValues[0])
    if len(possibleValues) ==0:
        return 'nope'
    elif possibleValues[0]=='?':
        return 0;

    else:
        print('possible:',possibleValues,'selection:',sel)
        return float(possibleValues[0])

def CatBox(self,vbox,cat):

    cat_store = Gtk.ListStore(str)
    # for cat in categories:
    cat_store.append([cat])

    cat_store = Gtk.ComboBox.new_with_model(cat_store)
    cat_store.connect("changed", self.on_cat_store_changed)
    renderer_text = Gtk.CellRendererText()
    cat_store.pack_start(renderer_text, True)
    cat_store.add_attribute(renderer_text, "text", 0)
    vbox.pack_start(cat_store, False, False, True)


def GetWeight(val):
    return 2
def GetMax(val):
    return 11
def GetMin(val):
    return 1
def Normalize(val):
    return abs(val)

def ValBox(self,vbox,cat):


    val_store = Gtk.ListStore(str)
    possibleValues = ([value for (category,value) in values if category == cat])

    for value in possibleValues:
        val_store.append([str(value)])

    val_store = Gtk.ComboBox.new_with_model(val_store)
    val_store.connect("changed", self.on_val_store_changed)
    renderer_text = Gtk.CellRendererText()
    val_store.pack_start(renderer_text, True)
    val_store.add_attribute(renderer_text, "text", 0)

    selectedValues.append(val_store)

    vbox.pack_start(val_store, False, False, True)

# def UpdateValues(cat):
#     # for value in values:
#     possibleValues = ([value for (category,value) in values if category == cat])
#     # print(possibleValues)
#     # ComboBoxWindow.config(values=possibleValues)





class ComboBoxWindow(Gtk.Window):
    


    def __init__(self):
        Gtk.Window.__init__(self, title="IA")

        self.set_border_width(10)


        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        hbox = Gtk.Box(spacing=6)
        self.add(vbox)


        label = Gtk.Label("Entrada do caso problema:")
        vbox.pack_start(label, True, True, 0)
        label = Gtk.Label("Atributos:")
        vbox.pack_start(label, True, True, 0)

        for cat in categories:
            if(categories.index(cat)>=fields):
                break

            CatBox(self,vbox,cat)
            ValBox(self,vbox,cat)
            
        vbox.add(hbox)



        button = Gtk.Button.new_with_mnemonic("_Fechar")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Continuar")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print("\"Next\" button was clicked")
        for combo in selectedValues:
            index = combo.get_active()
            model = combo.get_model()
            item = model[index]
            
            selectedText.append(item[0])
            print(item[0])
            print(GetValue(item[0]))

        rows = df.index
        for row in rows:
            totalWeight = 1
            temp = 0
            for item in selectedText:
                cat=selectedText.index(item)
                case=df.iat[row,cat+2]
                print('problem:',item,'case:',case)

                if GetValue(case) == 'nope':
                    print('nope')
                    break


                temp = 1- (abs(GetValue(item) - GetValue(case)))/GetMax(cat)-GetMin(cat)   #GetWeight(item)
                temp *= GetWeight(cat)
                temp=Normalize(temp)


                totalWeight+=GetWeight(cat)                
                # temp 
                # values.append(row
            # print(temp)
        
            calculated.append(temp/totalWeight)
        


        rows = df.index
        for row in rows:
            if(calculated[row]>0.01):
                # print(calculated.index(done),done)
                print(df.iat[row,0],df.iat[row,1],calculated[row])

        # for done in calculated:
        # print(len(calculated))
        calculated.clear()



        





    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

    
    def on_cat_store_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            cat = model[tree_iter][0]
            print("Selected: category =%s" % cat)

            # UpdateValues(cat)




    def on_val_store_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            cat = model[tree_iter][0]
            print("Selected: Value =%s" % cat)
            print(GetValue(cat))


            # for value in values:
            # print([value for (category,value) in values if category == cat])










win = ComboBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

# print(df.columns)

# print(df.head(5))  # print first 5 rows of the dataframe