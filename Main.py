# 선택한 폴더에 있는 파일들을 읽고 파일의 정보를 txt 파일로 저장하는 프로그램.
# 하위 폴더도 전부 읽어들인다.
import os
import time
import datetime
import shutil
from enum import Enum

FilstList = []

def AddFileInfo(path,name):
#해당 파일이 없으면 return
    if os.path.isfile(path) == False:
        #print(path + " 파일이 없습니다.")
        return 0
    
    ctime = time.ctime(os.path.getctime(path))
    ctime = time.strptime(ctime)
    rtime = time.strftime("%Y%m%d",ctime)
    FilstList.append([path,rtime,name])

    # 현재 가지고 있는 큰 파일 정보보다 용량이 클 경우 새로 저장
    
def search(dirname):    # 디렉토리 검색 
    try:
        fileNames = os.listdir(dirname) # 디렉토리에 있는 파일 목록들
        for filename in fileNames:
            full_filename = os.path.join(dirname, filename) # 경로와 파일 이름을 합쳐줌
            if os.path.isdir(full_filename):                # 폴더가 있을 경우
                search(full_filename)                       # 폴더 안으로 들어가기 위해 재귀
            else:   
                AddFileInfo(full_filename,filename)         # 파일일 경우 정보 저장
                
    except PermissionError:
        pass

def CreateNewFolder(path):
    index = 0
    for f in FilstList:
        if not os.path.isdir(path + "\\" + f[1]):
            os.makedirs(path + "\\" + f[1])
            
        CreateNewFile(f[0],path + "\\" + f[1] + "\\" + f[2])
        index += 1
        print(str(index) + " / "+ str(len(FilstList)))

def CreateNewFile(src,dst):
    shutil.copy2(src,dst)
def MoveNewFile(src,dst):
    shutil.move(src,dst) 



fpath = input("정리할 폴더의 경로를 입력해주세요 : ")
search(fpath)
rpath = input("새로 만들 폴더의 경로를 입력해주세요 : ")
rpath += "\\SortFolder"

CreateNewFolder(rpath)

print("완료되었습니다!")



