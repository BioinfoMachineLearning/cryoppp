import pandas as pd
import requests
df = pd.read_excel('EMPIAR.xlsx')
df.head()

df['Authors'] = df['Authors'].fillna('N/A')
df['Size'] = df['Size'].fillna('N/A')
df['Resolution'] = df['Resolution'].fillna('N/A')
df1 =df.dropna(axis=0)
df1 = df1.reset_index()
df1 = df1.drop(columns=['index'])
df1.to_excel('Processed_EMPIAR_by RG.xlsx')
df1



df1 = pd.read_excel('Processed_EMPIAR_by RG.xlsx')
abc = list(df1['EMPIAR ID'])
# abc = ['EMPIAR-11135']
empiars = []
titles = []
emdbs = []
pdbs = []
sizes = []
for x in abc:
    response = requests.get("https://www.ebi.ac.uk/empiar/api/entry/" + x).json()
    a = response[x]
    empiars.append(x)
    titles.append(a['title'])
    try:
        emdbs.append(','.join(a['cross_references']))
    except:
        emdbs.append("N/A")
    try:
        pdbs.append(','.join(a['related_pdb_entries']))
    except:
        pdbs.append("N/A")
    sizes.append(a['dataset_size'])
    
df3 =  pd.DataFrame(
    {'EMPIAR-ID': empiars,
     'Title': titles,
     'EMDB': emdbs,
     'PDB':pdbs,
     'Size':sizes
    })
df3.to_excel('EMPAIR_EMDB_PDB.xlsx')
df3
