import os
import shutil
import time

path = input("enter the path to delete")
days=5
seconds=time.time()-(days*24*60*60)

if os.path.exists(path):
    for root_folder,folders,files in os.walk(path):
        if seconds>=getfileorfolderage(root_folder):
            remove_folder(root_folder)
            break
        else:
            for folder in folders:
                folder_path=os.path.join(root_folder,folder)
                if seconds>=getfileorfolderage(folder_path):
                    remove_folder(folder_path)
            for file in files:
                file_path=os.path.join(root_folder,file)
                if seconds>=getfileorfolderage(file_path):
                    remove_file(file_path)        
    else:
        if seconds>=getfileorfolderage(path):    
            remove_file(path)

else:
    print("path is not found")


def remove_folder(path):
    if not shutil.rmtree(path):
        print("folder is removed succesfuly") 
    else:
        print("unable to delete folder")
def remove_file(path):
    if not os.remove(path):
        print("file is removed succesfully")
    else:
        print("unable to delete file")
def getfileorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime

if __name__ =='__main__':
    main()







