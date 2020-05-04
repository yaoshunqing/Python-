# @Time : 2020/5/1 18:15 
# @Author : Yao
# @File : alice.py 
# @Software: PyCharm

file_names = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
def count_words(file_name):
    try:
        with open(file_name,'r+') as f_obj:
            contents = f_obj.read()
    except Exception as e:
        pass
        # msg = "Sorry, the file " +  file_name + " is not existing."
        # print(msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        #print(words)
        num_words = len(words)
        print("The file " + file_name + " has about " + str(num_words) + "words.")
for filename in file_names:
    count_words(filename)