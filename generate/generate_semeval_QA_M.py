import os

data_dir='../data/HAAD./'

dir_path = data_dir+'bert-pair/'
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

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
                if "المزايا" in category:
                    g.write(id+"\t"+polarity[category.index("المزايا")]+"\t"+"ما رأيك في المزايا ؟؟ا"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في المزايا ؟؟ا"+"\t"+text+"\n")
                if "الحبكة" in category:
                    g.write(id+"\t"+polarity[category.index("الحبكة")]+"\t"+"ما رأيك في الحبكة ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الحبكة ؟؟ا"+"\t"+text+"\n")
               
                if "المشاعر" in category:
                    g.write(id+"\t"+polarity[category.index("المشاعر")]+"\t"+"ما رأيك في المشاعر ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في المشاعر ؟؟ا"+"\t"+text+"\n")
                
                if "الاسلوب" in category:
                    g.write(id+"\t"+polarity[category.index("الاسلوب")]+"\t"+" ما رأيك في الاسلوب ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الاسلوب ؟؟ا"+"\t"+text+"\n")
                
                if "السياق" in category:
                    g.write(id+"\t"+polarity[category.index("السياق")]+"\t"+"ما رأيك في السياق ؟؟ "+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في السياق ؟؟ا"+"\t"+text+"\n")
      
                if "السلبيات" in category:
                    g.write(id+"\t"+polarity[category.index("السلبيات")]+"\t"+"ما رأيك في السلبيات ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في السلبيات ؟؟ا"+"\t"+text+"\n")

                if "المؤلف" in category:
                   g.write(id+"\t"+polarity[category.index("المؤلف")]+"\t"+"ما رأيك في المؤلف ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في المؤلف ؟؟ا"+"\t"+text+"\n")
                
                if "التقييم" in category:
                   g.write(id+"\t"+polarity[category.index("التقييم")]+"\t"+"ما رأيك في التقييم ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في التقييم ؟؟ا"+"\t"+text+"\n")
                
                if "الاماكن" in category:
                    g.write(id+"\t"+polarity[category.index("الاماكن")]+"\t"+"ما رأيك في الاماكن ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الاماكن ؟؟ا"+"\t"+text+"\n")
                
                if "الطائفية" in category:
                  g.write(id+"\t"+polarity[category.index("الطائفية")]+"\t"+"ما رأأيك في الطائفية ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الطائفية ؟؟ا"+"\t"+text+"\n")
                
                if "الخاتمة" in category:
                 g.write(id+"\t"+polarity[category.index("الخاتمة")]+"\t"+"ما رأيك في الخاتمة ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الخاتمة ؟؟ا"+"\t"+text+"\n")
              
                if "اللغات" in category:
                 g.write(id+"\t"+polarity[category.index("اللغات")]+"\t"+"ما رأيك في اللغات ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في اللغات ؟؟ا"+"\t"+text+"\n")
               
                if "الهوامش" in category:
                 g.write(id+"\t"+polarity[category.index("الهوامش")]+"\t"+"ما رأيك في الهوامش ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الهوامش ؟؟ا"+"\t"+text+"\n")
                
                if "الوقت" in category:
                 g.write(id+"\t"+polarity[category.index("الوقت")]+"\t"+"ما رأيك في الوقت؟؟ "+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الوقت ؟؟ا"+"\t"+text+"\n")
               
                if "الاموال" in category:
                 g.write(id+"\t"+polarity[category.index("الاموال")]+"\t"+"ما رأيك في الاموال ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الاموال ؟؟ا"+"\t"+text+"\n")
                
               
                
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
                if "المزايا" in category:
                    g.write(id+"\t"+polarity[category.index("المزايا")]+"\t"+"ما رأيك في المزايا ؟؟ا"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في المزايا ؟؟ا"+"\t"+text+"\n")
                if "الحبكة" in category:
                    g.write(id+"\t"+polarity[category.index("الحبكة")]+"\t"+"ما رأيك في الحبكة ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الحبكة ؟؟ا"+"\t"+text+"\n")
               
                if "المشاعر" in category:
                    g.write(id+"\t"+polarity[category.index("المشاعر")]+"\t"+"ما رأيك في المشاعر ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في المشاعر ؟؟ا"+"\t"+text+"\n")
                
                if "الاسلوب" in category:
                    g.write(id+"\t"+polarity[category.index("الاسلوب")]+"\t"+" ما رأيك في الاسلوب ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الاسلوب ؟؟ا"+"\t"+text+"\n")
                
                if "السياق" in category:
                    g.write(id+"\t"+polarity[category.index("السياق")]+"\t"+"ما رأيك في السياق ؟؟ "+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في السياق ؟؟ا"+"\t"+text+"\n")
      
                if "السلبيات" in category:
                    g.write(id+"\t"+polarity[category.index("السلبيات")]+"\t"+"ما رأيك في السلبيات ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في السلبيات ؟؟ا"+"\t"+text+"\n")

                if "المؤلف" in category:
                   g.write(id+"\t"+polarity[category.index("المؤلف")]+"\t"+"ما رأيك في المؤلف ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في المؤلف ؟؟ا"+"\t"+text+"\n")
                
                if "التقييم" in category:
                   g.write(id+"\t"+polarity[category.index("التقييم")]+"\t"+"ما رأيك في التقييم ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في التقييم ؟؟ا"+"\t"+text+"\n")
                
                if "الاماكن" in category:
                    g.write(id+"\t"+polarity[category.index("الاماكن")]+"\t"+"ما رأيك في الاماكن ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الاماكن ؟؟ا"+"\t"+text+"\n")
                
                if "الطائفية" in category:
                  g.write(id+"\t"+polarity[category.index("الطائفية")]+"\t"+"ما رأأيك في الطائفية ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الطائفية ؟؟ا"+"\t"+text+"\n")
                
                if "الخاتمة" in category:
                 g.write(id+"\t"+polarity[category.index("الخاتمة")]+"\t"+"ما رأيك في الخاتمة ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الخاتمة ؟؟ا"+"\t"+text+"\n")
              
                if "اللغات" in category:
                 g.write(id+"\t"+polarity[category.index("اللغات")]+"\t"+"ما رأيك في اللغات ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في اللغات ؟؟ا"+"\t"+text+"\n")
               
                if "الهوامش" in category:
                 g.write(id+"\t"+polarity[category.index("الهوامش")]+"\t"+"ما رأيك في الهوامش ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الهوامش ؟؟ا"+"\t"+text+"\n")
                
                if "الوقت" in category:
                 g.write(id+"\t"+polarity[category.index("الوقت")]+"\t"+"ما رأيك في الوقت؟؟ "+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الوقت ؟؟ا"+"\t"+text+"\n")
               
                if "الاموال" in category:
                 g.write(id+"\t"+polarity[category.index("الاموال")]+"\t"+"ما رأيك في الاموال ؟؟"+"\t"+text+"\n")
                else:
                    g.write(id+"\t"+none+"\t"+"ما رأيك في الاموال ؟؟ا"+"\t"+text+"\n")
            else:
                s = f.readline().strip()
