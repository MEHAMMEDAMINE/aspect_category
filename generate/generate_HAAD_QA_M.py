# -*- coding: utf-8 -*-


import os
import random
from random import sample
random.seed(10)
data_dir='../data/HAAD./'

dir_path = data_dir+'bert-pair/'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
d=['الحبكة', 'المشاعر', 'الاسلوب', 'السياق', 'السلبيات', 'المؤلف', 'التقييم', 'الاماكن', 'الطائفية', 'الخاتمة', 'اللغات', 'الهوامش', 'الوقت', 'الاموال', 'المزايا']
with open(dir_path+"test_QA_M.csv","w",encoding="utf-8") as g:
    with open(data_dir+"HAAD_Test_GOLD.xml","r",encoding="utf-8") as f:
        s=f.readline().strip()
        while s:
            category=[]
            polarity=[]
            if "<sentence id" in s:
                left=s.find("id")
                right=s.find(">")
                id=s[left+4:right-1]
                while not "</sentence>" in s:
                    if "<text>" in s:
                        left=s.find("<text>")
                        right=s.find("</text>")
                        text=s[left+6:right]
                    if "aspectCategory" in s:
                        left=s.find("category=")
                        right=s.find("polarity=")
                        category.append(s[left+10:right-2])
                        left=s.find("polarity=")
                        right=s.find("/>")
                        polarity.append(s[left+10:right-1])
                    s=f.readline().strip()
                a=[item for item in d if item not in category]
                
                ss=sample(a,3)
                for i in d:
                    if i in category:
                        g.write(id+"\t"+polarity[category.index(i)]+"\t"+"ما رأيك في "+i+" ؟"+"\t"+text+"\n")
                for l in ss:
                        g.write(id + "\t" + "none" + "\t"  +"ما رأيك في "+l+" ؟"+ "\t" + text + "\n")

               
                
                
            else:
                s = f.readline().strip()


with open(dir_path+"train_QA_M.csv","w",encoding="utf-8") as g:
    with open(data_dir+"HAAD_Train.xml","r",encoding="utf-8") as f:
        s=f.readline().strip()
        while s:
            category=[]
            polarity=[]
            if "<sentence id" in s:
                left=s.find("id")
                right=s.find(">")
                id=s[left+4:right-1]
                while not "</sentence>" in s:
                    if "<text>" in s:
                        left=s.find("<text>")
                        right=s.find("</text>")
                        text=s[left+6:right]
                    if "aspectCategory" in s:
                        left=s.find("category=")
                        right=s.find("polarity=")
                        category.append(s[left+10:right-2])
                        left=s.find("polarity=")
                        right=s.find("/>")
                        polarity.append(s[left+10:right-1])
                    s=f.readline().strip()
                a=[item for item in d if item not in category]
                
                ss=sample(a,3)
                for i in d:
                    if i in category:
                       g.write(id+"\t"+polarity[category.index(i)]+"\t"+"ما رأيك في "+i+" ؟"+"\t"+text+"\n")
                for l in ss:
                       g.write(id + "\t" + "none" + "\t"  +"ما رأيك في "+l+" ؟"+ "\t" + text + "\n")


                



            else:
                s = f.readline().strip()


