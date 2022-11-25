import os,shutil

class scanner:
    def __init__(self):
        self.path ='testing'
        self.file_list = os.listdir(self.path)
        self.move_to = 'testing2'
        self.file_extention = '.txt'
        self.repeat = True
        self.copy = False
    def select(self):
        contains = S.filter()
        if len(contains) != 0:
            while self.repeat:
                self.file_list = os.listdir(self.path)
                contains = S.filter()
                S.printing(contains)
        else:
            print('there are no files here')
    def movement(self,file):
        local= self.path +'/'+file
        shutil.move(local,self.move_to)
        print('finished')
    def copying(self,file):
        local= self.path +'/'+file
        shutil.copy(local,self.move_to)
        print('finished')
    def filter(self):
        contains = []
        for i in range(len(self.file_list)):
            if self.file_extention in self.file_list[i]:
                contains.append(self.file_list[i])
        return contains
    def printing(self,contains):
        print('enter the index of the file to move')
        print('-----------------------------')
        if self.copy == True:
            print('Current Mode-Copy')
        else:
            print('Current Mode-Move')
        for i in range(len(contains)):
            print('{0}:{1}'.format(i,contains[i]))
        if self.copy == True:
            print('M:move mode')
        else:
            print('C:copy mode')
        print('E:exit')
        print('-----------------------------')
        file = input('')
        if file.lower() == 'e':
            self.repeat = False
            return
        elif file.lower() == 'm':
            self.copy = False
        elif file.lower() == 'c':
            self.copy= True
        else:
            try:
                if self.copy == False:
                    S.movement(contains[int(file)])
                else:
                    S.copying(contains[int(file)])
            except:
                print('sorry, something went wrong when attemping to move file number {0}'.format(file))
S = scanner()
S.select()
