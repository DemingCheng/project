import pandas as pd


train_data = pd.read_table("mytrain/datasets/medicine-38.txt", header = None)  
# print(train_data)
# print(train_data.shape)
train_data[0] = train_data[0].str.replace('Senior: "','')
train_data[0] = train_data[0].str.replace('" Caregiver: "','|')
# print(train_data[0][0])

# train_data['Senior'] = train_data[0].map(lambda x:x.split('|')[0])
# train_data['Caregiver'] = train_data[0].map(lambda x:x.split('|')[1])
train_data = train_data[['Senior', 'Caregiver']] = train_data[0].str.split('|', n = 1, expand=True)
# print(train_data)



