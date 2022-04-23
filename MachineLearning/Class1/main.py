import zipfile
import os
"""----------------------------------------------------------------"""
# unzip file
def unzip_data(src_path,target_path):
    # 解压原始数据集，将src_path路径下的zip包解压至target_path目录下
    if(not os.path.isdir(target_path)):     
        z = zipfile.ZipFile(src_path, 'r')
        z.extractall(path=target_path)
        z.close()
unzip_data('data/data10954/cat_12_test.zip','data/data10954/car_12_test')
unzip_data('data/data10954/cat_12_train.zip','data/data10954/cat_12_train')
"""----------------------------------------------------------------"""
"""
通过给定目录，统计所有的不同子文件类型及占用内存
"""
size_dict = {}
type_dict = {}
def get_size_type(path):
    files = os.listdir(path)
    for filename in files:
        temp_path = os.path.join(path, filename)
        if os.path.isdir(temp_path):
            # 递归调用函数，实现深度文件名解析
            get_size_type(temp_path)     
        elif os.path.isfile(temp_path):
            # 获取文件后缀
            type_name=os.path.splitext(temp_path)[1]   
            #无后缀名的文件
            if not type_name:
                type_dict.setdefault("None", 0)
                type_dict["None"] += 1
                size_dict.setdefault("None", 0)
                size_dict["None"] += os.path.getsize(temp_path)
            # 有后缀的文件
            else:
                type_dict.setdefault(type_name, 0)
                type_dict[type_name] += 1
                size_dict.setdefault(type_name, 0)
                # 获取文件大小
                size_dict[type_name] += os.path.getsize(temp_path)  
path= "data/"
get_size_type(path)
for each_type in type_dict.keys():
    print ("%5s下共有【%5s】的文件【%5d】个,占用内存【%7.2f】MB" %     
            (path,each_type,type_dict[each_type],\
            size_dict[each_type]/(1024*1024)))
print("总文件数:  【%d】"%(sum(type_dict.values())))
print("总内存大小:【%.2f】GB"%(sum(size_dict.values())/(1024**3)))