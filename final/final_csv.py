import cv2
import os
import numpy as np
import pandas as pd

data=[]

csv = pd.read_csv('clear_data.csv')

for folder in os.listdir('augimg'):
    i=0
    for images in os.listdir(f'augimg/{folder}'):
        imgpath = f'augimg/{folder}/{images}'
        name = csv['Name'][i]
        s_n = csv['Scientific Name'][i]
        weight = csv['Weight(kg)'][i]
        height = csv['Height(cm)'][i]
        cs = csv['Conservation Status'][i]
        habi = csv['Commonly Found'][i]
        diet = csv['Food Habit'][i]
        age = csv['Average age'][i]
        
        data.append([imgpath,name,s_n,weight,height,cs,habi,diet,age])

data = pd.DataFrame(data,columns=['Image','Name','Scientific Name','Weight(KG)','Height(CM)','Conservation Status','Habitat','Diet','Age'])
data = data.sample(frac=1,random_state=42)

data.to_csv('create_script/final_data.csv',index=False)

