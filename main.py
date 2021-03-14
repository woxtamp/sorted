def convert_file_to_list(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines


def write_to_file():
    files_dict = {'1.txt': convert_file_to_list('files/1.txt'), '2.txt': convert_file_to_list('files/2.txt'),
                  '3.txt': convert_file_to_list('files/3.txt')}
    elements_sorted = {k: files_dict[k] for k in sorted(files_dict, key=files_dict.get, reverse=True)}
    with open('files/file_final.txt', 'w', encoding='utf-8') as file:
        for item in list((elements_sorted.keys())):
            file.write(f'{item}\n')
            file.write(str(len(elements_sorted.setdefault(item))) + '\n')
            for str_dict in elements_sorted[item]:
                file.write(str_dict)
            file.write('\n')


write_to_file()
