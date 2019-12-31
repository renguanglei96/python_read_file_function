def open_file_read(src_):
    decode_list = ["utf-8", 'gb18030', 'ISO-8859-2', 'gb2312', "gbk", "Error"]
    for k in decode_list:
        try:
            file = open(src_, "r", encoding=k)
            file_lines = file.readlines()
            file.close()
            break
        except UnicodeDecodeError:
            if k == "Error":
                file_lines = []
                print("No way can be used to read this file!")
            continue
    return file_lines, k
   
   # This method can be used to write files.
    lines_src, encoding_way = open_file_read('a.txt')
    f = open('a.txt', 'a+', encoding=encoding_way)
