#coding=utf-8
import os
fileList = []
rootdir = "C:\Users\molido\Desktop\\test\\"
for root, subFolders, files in os.walk(rootdir):
    if '.svn' in subFolders: subFolders.remove('.svn') # 排除特定目录
print files
for file in files:
    if file.find(".txt") != -1:# 查找特定扩展名的文件
        file_dir_path = os.path.join(root,file)
        fileList.append(file_dir_path)
        print fileList