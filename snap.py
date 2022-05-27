import pandas as pd
import time


def apply_complex_function(x): 
    return str(x).zfill(2)

def no_trailing_zero(value: str) :
    return value.rstrip("0")

def isHasParentCare(pid: str) :
    if(pid and pid.strip() !=""):
        return 1 #has
    else:
        return 0

def mapTypecripple(value: str) :
    if value == "ทางการเคลื่อนไหวหรือทางร่างกาย":
        return 1 
    elif value == "ทางการเห็น":
        return 2 
    elif value == "ทางการได้ยินหรือสื่อความหมาย":
        return 3 
    elif value == "ทางสติปัญญา":
        return 4 
    elif value == "ทางจิตใจหรือพฤติกรรม":
        return 5 
    elif value == "พิการซ้อน":
        return 6 
    elif value == "ทางออทิสติก":
         return 7 
    elif value == "ทางการเรียนรู้":
         return 8 
    else:
         return 9 #ไม่ระบุประเภทความพิการ


start = time.time()

# col
# 5 birth_date
# 6 age
# 8 sex
# 15 tumbon
# 16 tumbon_code
# 17 amphoe
# 18 amphoe_code
# 19 province
# 20 province_code
# 21 postcode
# 22 prename_curator
# 23 firstname_curator
# 24 lastname_curator
# 25 curator_pid
# 26 curator_relation_code
# 27 curator_relation_name
# 28 curator_other
# 43 deformname
# 44 card_issue_date
# 45 card_expire_date

#48 prename_cripple
#49 firstname_cripple
#50 lastname_cripple
#51 birthdate_cripple
#53 status_cripple

# 56 education
# 57 occupation
# 58 income_cripple
# 59 income_family
# 60 type_cripple
# 61 detail_cripple
# 62 lat
# 63 log

#64 tumbon_cripple
#65 amphoe_cripple
#66 province_cripple

colsIndex=[1,2,3,4,5,6,8,15,16,17,18,19,20,21,22,23,24,25,26,27,28,43,44,45,48,49,50,51,53,56,57,58,59,60,61,62,63,64,65,66]
#colsIndex=[1,2,3,4,5,6,8,15,16,17,18,19,20,21,22,23,24,25,26,27,28,43,44,45,48,49,50,51,53,56,57,58,59,60,61,62,63,64,65,66]
namesCol=['prename', 
 'firstname',
 'lastname', 
 'pid',
 'birth_date',#5
 'age',
 'sex',
 'tumbon',
 'tumbon_code',
 'amphoe',
 'amphoe_code',
 'province',
 'province_code',
 'postcode',
 'prename_curator',
 'firstname_curator',
 'lastname_curator',
 'curator_pid',
 'curator_relation_code',
 'curator_relation_name',
 'curator_other',
 'deformname',
 'card_issue_date',
 'card_expire_date',
 'prename_cripple',
 'firstname_cripple',
 'lastname_cripple',
 'birthdate_cripple',
 'status_cripple',
 'education',
 'occupation',
 'income_cripple',
 'income_family',
 'type_cripple',
 'detail_cripple',
 'lat',
 'long',
 'tumbon_cripple',
 'amphoe_cripple',
 'province_cripple',
 ]

df = pd.read_excel("cripple_db2.xlsx",  usecols=colsIndex, names=namesCol,dtype={3:str})
#df['MAIMAD_PERSON_CODE'] = df['MAIMAD_PERSON_CODE'].astype(str)
#df['pid'] = df['pid'].astype(str)
#print(penguins)
#print(df.head())
#print(df.info())
#print(df)
#data = df.head(10)

#df2 = df.drop(df[df['pid'].str.strip() !=""].index, inplace = True)
df.dropna()
#df = df[df.pid.notnull()]


df['fullname'] = df['prename'].map(str) + df['firstname'].map(str) + ' ' + df['lastname'].map(str)
df['curator_pid'] = df['curator_pid'].astype('str')
df['lat'] = df['lat'].astype('str')
df['long'] = df['long'].astype('str')
df['type_cripple'] = df['type_cripple'].astype('str')
df['province_id'] = df['province_code'].map(str)
df["amphoe_code"]= df["amphoe_code"].astype(str)
df["tumbon_code"]= df["tumbon_code"].astype(str)
df['district_id']= df['province_code'].map(str) + df['amphoe_code'].str.zfill(2)
df['district_code']=df.apply(lambda x: no_trailing_zero(x['tumbon_code']),axis=1)
df['district_code'].astype(str)
df['sub_district_id']=df['province_code'].map(str) + df['amphoe_code'].str.zfill(2)+df['district_code'].str.zfill(2)
df['cripple_category']=df.apply(lambda x: mapTypecripple(x['type_cripple'].strip()),axis=1)
df['is_has_parent_care']=df.apply(lambda x: isHasParentCare(x['curator_pid']),axis=1)


#f['ap_code'] = df['province_code'].map(str) + (df['amphoe_code'].astype(int)).zfill(2)
#df['tb_code'] = df['province_code'].map(str) + (df['amphoe_code'].astype(int)).zfill(2).map(str) + (df['tumbon_code'].astype(int)).normalize().map(str)
#f'{3.140:g}'




print(df.info())

print(df['deformname'].unique())

print(df['type_cripple'].unique())



#print(df)
#print(df.describe()) #หาค่าสถิติเบื้องต้นของทุกคอลัมน์ใน dataframe
df.to_csv("export_map_cripple.csv",encoding='utf-8-sig')



dfCat = pd.DataFrame(df['type_cripple'].unique())
dfCat.to_csv("cat_export.csv",encoding='utf-8-sig')

end = time.time()
print('\nExperiment Completed\nTotal Time: {:.2f} seconds'.format(end-start))


#df.nunique()

