# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:00:05 2022

@author: MOHAMMED ELAMINE
"""
import os

data_dir='../data/HAAD./'

dir_path = data_dir+'bert-pair/'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

with open(dir_path+"test_NLI_M.csv","w",encoding="utf-8") as g:
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
                if "المزايا" in category:
                    g.write(id+"\t"+polarity[category.index("المزايا")]+"\t"+"المزايا"+"\t"+text+"\n")
               
                if "الحبكة" in category:
                    g.write(id+"\t"+polarity[category.index("الحبكة")]+"\t"+"الحبكة"+"\t"+text+"\n")
                
                if "المشاعر" in category:
                    g.write(id+"\t"+polarity[category.index("المشاعر")]+"\t"+"المشاعر"+"\t"+text+"\n")
                
                if "الاسلوب" in category:
                    g.write(id+"\t"+polarity[category.index("الاسلوب")]+"\t"+"الاسلوب"+"\t"+text+"\n")
                
                if "السياق" in category:
                    g.write(id+"\t"+polarity[category.index("السياق")]+"\t"+"السياق"+"\t"+text+"\n")
      
                if "السلبيات" in category:
                    g.write(id+"\t"+polarity[category.index("السلبيات")]+"\t"+"السلبيات"+"\t"+text+"\n")

                if "المؤلف" in category:
                   g.write(id+"\t"+polarity[category.index("المؤلف")]+"\t"+"المؤلف"+"\t"+text+"\n")
                
                if "التقييم" in category:
                   g.write(id+"\t"+polarity[category.index("التقييم")]+"\t"+"التقييم"+"\t"+text+"\n")
                
                if "الاماكن" in category:
                    g.write(id+"\t"+polarity[category.index("الاماكن")]+"\t"+"الاماكن"+"\t"+text+"\n")
                
                if "الطائفية" in category:
                  g.write(id+"\t"+polarity[category.index("الطائفية")]+"\t"+"الطائفية"+"\t"+text+"\n")
                
                if "الخاتمة" in category:
                 g.write(id+"\t"+polarity[category.index("الخاتمة")]+"\t"+"الخاتمة"+"\t"+text+"\n")
              
                if "اللغات" in category:
                 g.write(id+"\t"+polarity[category.index("اللغات")]+"\t"+"اللغات"+"\t"+text+"\n")
               
                if "الهوامش" in category:
                 g.write(id+"\t"+polarity[category.index("الهوامش")]+"\t"+"الهوامش"+"\t"+text+"\n")
                
                if "الوقت" in category:
                 g.write(id+"\t"+polarity[category.index("الوقت")]+"\t"+"الوقت"+"\t"+text+"\n")
               
                if "الاموال" in category:
                 g.write(id+"\t"+polarity[category.index("الاموال")]+"\t"+"الاموال"+"\t"+text+"\n")
                
                if "اسلوب" in category:
                 g.write(id+"\t"+polarity[category.index("اسلوب")]+"\t"+"اسلوب"+"\t"+text+"\n")
               
                if "مشاعر" in category:
                 g.write(id+"\t"+polarity[category.index("مشاعر")]+"\t"+"مشاعر"+"\t"+text+"\n")
                
            else:
                s = f.readline().strip()


with open(dir_path+"train_NLI_M.csv","w",encoding="utf-8") as g:
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
                if "المزايا" in category:
                    g.write(id+"\t"+polarity[category.index("المزايا")]+"\t"+"المزايا"+"\t"+text+"\n")
                
                if "الحبكة" in category:
                    g.write(id+"\t"+polarity[category.index("الحبكة")]+"\t"+"الحبكة"+"\t"+text+"\n")
                
                if "المشاعر" in category:
                    g.write(id+"\t"+polarity[category.index("المشاعر")]+"\t"+"المشاعر"+"\t"+text+"\n")
                
                if "الاسلوب" in category:
                    g.write(id+"\t"+polarity[category.index("الاسلوب")]+"\t"+"الاسلوب"+"\t"+text+"\n")
                
                if "السياق" in category:
                    g.write(id+"\t"+polarity[category.index("السياق")]+"\t"+"السياق"+"\t"+text+"\n")
                
                if "السلبيات" in category:
                    g.write(id+"\t"+polarity[category.index("السلبيات")]+"\t"+"السلبيات"+"\t"+text+"\n")
                
                if "المؤلف" in category:
                   g.write(id+"\t"+polarity[category.index("المؤلف")]+"\t"+"المؤلف"+"\t"+text+"\n")
                
                if "التقييم" in category:
                   g.write(id+"\t"+polarity[category.index("التقييم")]+"\t"+"التقييم"+"\t"+text+"\n")
               
                if "الاماكن" in category:
                    g.write(id+"\t"+polarity[category.index("الاماكن")]+"\t"+"الاماكن"+"\t"+text+"\n")
                
                if "الطائفية" in category:
                  g.write(id+"\t"+polarity[category.index("الطائفية")]+"\t"+"الطائفية"+"\t"+text+"\n")
                
                if "الخاتمة" in category:
                 g.write(id+"\t"+polarity[category.index("الخاتمة")]+"\t"+"الخاتمة"+"\t"+text+"\n")
                
                if "اللغات" in category:
                 g.write(id+"\t"+polarity[category.index("اللغات")]+"\t"+"اللغات"+"\t"+text+"\n")
                                
                if "الهوامش" in category:
                 g.write(id+"\t"+polarity[category.index("الهوامش")]+"\t"+"الهوامش"+"\t"+text+"\n")
                
                if "الوقت" in category:
                 g.write(id+"\t"+polarity[category.index("الوقت")]+"\t"+"الوقت"+"\t"+text+"\n")
                
                if "الاموال" in category:
                 g.write(id+"\t"+polarity[category.index("الاموال")]+"\t"+"الاموال"+"\t"+text+"\n")
                
                if "اسلوب" in category:
                 g.write(id+"\t"+polarity[category.index("اسلوب")]+"\t"+"اسلوب"+"\t"+text+"\n")
                
                if "مشاعر" in category:
                 g.write(id+"\t"+polarity[category.index("مشاعر")]+"\t"+"مشاعر"+"\t"+text+"\n")
                



            else:
                s = f.readline().strip()


