import pandas as pd
data = {
    "First" :['John', 'Temi', 'Tiwa'],
    "Last" : ['Mosh', 'Lade', 'Tope'] ,
    "Email" : ['johnmosh@gmail.com', 'temilade@gmail.com', "tiwatope@gmail.com"]
    }
df = pd.DataFrame(data)
print(df)