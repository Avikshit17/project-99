import os
import shutil
allFiles=os.listdir("C:/Users/ACER/Downloads/Avikshit")
for eachFile in allFiles:
    root,ext=os.path.splitext(eachFile)
    if(ext==""):
        continue
    isExist=os.path.exists("C:/Users/ACER/Downloads/Avikshit/"+ext)
    print(isExist)
    if(isExist==False):
        os.mkdir("C:/Users/ACER/Downloads/Avikshit/"+ext)
        shutil.move("C:/Users/ACER/Downloads/Avikshit/"+eachFile,"C:/Users/ACER/Downloads/Avikshit/"+ext)
    else:
        shutil.move("C:/Users/ACER/Downloads/Avikshit/"+eachFile,"C:/Users/ACER/Downloads/Avikshit/"+ext)
