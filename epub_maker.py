import zipfile
import os
import re

def makezip(ab_path, name):
    zip_file = zipfile.ZipFile(f"./epubs/{name}.epub", "w")
    zip_file.write(ab_path+"mimetype")

    for (path, dir, files) in os.walk(ab_path+"OEBPS"):

        for file in files:
            file_path = f"{path}\{file}"
            #print(file_path)
            zip_file.write(file_path)

    for (path, dir, files) in os.walk(ab_path+"META-INF"):
        for file in files:
            file_path = f"{path}\{file}"
            #print(file_path)
            zip_file.write(file_path)

def findEpub(FolderNmae):
    ab_path = os.getcwd()
    for (path, dir, files) in os.walk(FolderNmae):
        for file in files:
            if file == "mimetype":
                name = re.sub('\\\\', '_', path)

                file_ab_path = f"{ab_path}/{path}/"
                makezip(file_ab_path, name)
                #print(name)
                #print(path, files)
    print(ab_path)
    

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#epub 폴더 있는 곳 이름 넣고 돌리면 됨
#epub가 제대로된 형식이라는 가정하에 잘 돌아감

createFolder("./epubs")
findEpub("./")
