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

#Result
# ['changeserver.PNG', 'cms-common-11.1.76.jar', 'handlers$py.class', 'handlers.py', 'licenseexpired.PNG', 'licenserestricted.PNG', 'needlicenseremain.PNG', 'neednewlicense.PNG', 'oswalk.py', 'rules$py.class', 'rules.py', 'SNMP_Connection_Utils.py', 'test.py', 'test_input.txt', 'test_output.html', 'utils$py.class', 'utils.py', 'versioncontrol.PNG']
# ['C:\\Users\\molido\\Desktop\\test\\test_input.txt']