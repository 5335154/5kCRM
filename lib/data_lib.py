'''调用数据方法'''

def read_txt(file_name=r"D:\git_root\5kCRM\data\user.txt"):
    with open(file_name,"r+",encoding="utf-8") as f:
        lines = f.readlines()
        data_list = []
        print(lines)
        for line in lines:
            line = line.split()
            data_list.append(line)
        return data_list
# r = read_txt()
# print(r)