import os
from traceback import print_exc, print_exception


def writer(file_path, data):
    
    if not os.path.isdir(dir_path := '/'.join(file_path.split('/')[:-1])):
        os.makedirs(dir_path)
    
    f = open(file_path, 'w')
    f.write(data)
    f.close()


def reader(file_path):
    
    try:
        f = open(file_path, 'r')
    except:
        return None
    else:
        data = f.read()
        f.close()
        return data


def create_file_list(path_list):
    result_path_list = []
    for each_path in path_list:
        try:
            if os.path.isdir(each_path):
                for root_path, dir_path, file_name_list in os.walk(each_path):
                    if not dir_path:
                        result_path_list += [root_path + '/' + f for f in file_name_list]
            elif os.path.isfile(each_path):
                result_path_list += [each_path]
        except:
            pass
    return result_path_list


if __name__ == "__main__":
    result = create_file_list(["/home/user"])
    print(result)
