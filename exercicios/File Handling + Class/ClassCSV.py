import csv

class Files_CSV:

    def __init__(self,file_name):
        self.file_name = file_name

    def add_datas(self,name_content,age_content,position):
        self.name_content = name_content
        self.age_content = age_content
        self.position = position

        open_file = open(str(self.file_name),'a',newline='',encoding='utf-8')
        add = csv.writer(open_file)

        for i in range(1): #lines
            add.writerow([i+self.position,str(self.name_content),self.age_content]) # id , nome , idade

#file_csv1 = Files_CSV('Jonas',19,1)
file_csv1 = Files_CSV('teste.csv')
file_csv1.add_datas('Jonas',19,1)