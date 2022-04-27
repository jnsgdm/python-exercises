class Files_TXT:

    def __init__(self,content,file_name):
        self.content = content
        self.file_name = file_name
    
    def add_content(self):
        with open(str(self.file_name),'a') as file:
            file.write(str(self.content)+'\n')
    
    def print_file_content(self):
        with open(str(self.file_name),'r') as file:
            print(str(self.content)+'\n')

file_txt1 = Files_TXT('Etendendo POO','teste.txt')
file_txt1.add_content()
file_txt1.print_file_content()