import os,shutil

class scanner:
    def __init__(self):
        self.path ='testing'
        self.file_list = os.listdir(self.path)
        self.move_to = 'testing2'
        self.file_extention = '.txt'
    def select(self):
        contains = S.filter()
        print(contains)
        if len(contains) != 0:
            file_select = int(input('enter the index of the file you want to move? '))
            S.movement(contains[file_select])
        else:
            print('there are no files here')
    def movement(self,file):
        local= self.path +'/'+file
        shutil.move(local,self.move_to)
        print('finished')
    def filter(self):
        contains = []
        for i in range(len(self.file_list)):
            if self.file_extention in self.file_list[i]:
                contains.append(self.file_list[i])
        return contains

S = scanner()
S.select()
