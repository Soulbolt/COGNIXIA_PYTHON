
# file = open('generic_text_file.txt', 'r')
# print(file.read())
# file.close()
#with open('generic_text_file.txt', 'r') as f:
    #print(f.readlines())
    #print(f.readline().strip())
    #print(f.readline().strip()) # strip() removes spaces
    # for line in f:
    #     print(line)
    #     f.seek(0) # infinite loop resetting read to first line
# rest of my program....

with open('generic_text_file.txt', 'a') as f:
    f.write("fifth line of text")