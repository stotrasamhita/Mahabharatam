#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
from lxml import objectify
import pandas as pd
from copy import copy
import json
import os
with open('SARIT-corpus/mahabharata-devanagari.xml', 'r') as f:
	file = f.read() 

# 'xml' is the parser used. For html files, which BeautifulSoup is typically used for, it would be 'html.parser'.
soup = bs(file, 'xml')
names = soup.find_all('div')

nParva = 1
store_dir ='extracted_data'
print(os.listdir('.'))
#exit()
if store_dir not in os.listdir('.'):
    os.mkdir(store_dir)
verses={}
for name in names:
    
    if name.get('xml:id',0):
        parva=name['xml:id']
        verses={}
        verses[parva]={}
        adhyayas = name.find_all('div')
        # print(parva)
        for adhyay in adhyayas:
            if adhyay.get('xml:id',0):
                adh = adhyay['xml:id']
                # print(adhyay)
                #exit()
                heads = adhyay.find_all('head')
                verses[parva][adh]={}
                if len(heads)>0:
                    verses[parva][adh]['head']=heads[0].text
                # print(adh,heads)
                # print(adhyay)
                ps1= adhyay.find_all('p')
                top=0
                verses[parva][adh]['before_verses']=''
                verses[parva][adh]['after_verses']=''
                top_ind=len(ps1)
                bottom_in=-1
                for i in range(len(ps1)):
                    if ps1[i].get('rend',0)=='topic':
                        verses[parva][adh]['topic']=ps1[i].text.replace("\n","").replace("\t","")
                        top_ind=i
                    
                    if ps1[i].get('rend',0)=='footnotes':
                        verses[parva][adh]['footnotes']=ps1[i].text.replace("\n","").replace("\t","")
                        bottom_ind=i

                for i in range(len(ps1)):
                    if i < top_ind:
                        verses[parva][adh]['before_verses']=verses[parva][adh]['before_verses']+ps1[i].text.replace("\n","").replace("\t","")
                    elif i>top_ind and i!=bottom_ind:
                        verses[parva][adh]['after_verses']=verses[parva][adh]['after_verses']+ps1[i].text.replace("\n","").replace("\t","")
                if len(ps1)>0:
                    verses[parva][adh]['topic']=ps1[0].text

                ps2= adhyay.find_all('p',attributes={'rend':'footnotes'})
                if len(ps2)>0:
                    verses[parva][adh]['footnotes']=ps2[0].text
            lgs=adhyay.find_all('lg')
            ls=[]
            for lg in lgs:
                l_dict={}
                l_dict['verse_no']=lg["xml:id"]
                l_dict['chandas']=lg.get("type",'')
                l_dict['verse_text']=lg.text.replace("\n",'').replace("\t","").split("।")
                ls.append(copy(l_dict))
                # print(l_dict)
            verses[parva][adh]['verses']=copy(ls)
        
        if len(verses[parva])>0 and '_' not in parva:
            output_file_name = '%s/%02d-%s.json' % (store_dir, nParva, parva)
            with open(output_file_name,'w') as f:
                json.dump(verses,f,indent=4,ensure_ascii=False)
                nParva += 1
