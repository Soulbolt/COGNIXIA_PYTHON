import os



#print(os.getcwd())
#os.mkdir("made_with_os")
#print(os.listdir(os.getcwd()))
#print()
#os.rmdir("made_with_os")
#print(os.stat("logic_comparisons.py"))

#os.mkdirs()
#os.chdir("..")
#print(os.getcwd())
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#     print()

#print(os.environ.get("HOME"))

path_to_calculator = os.path.join(os.getcwd(), "calculator.py")

#print(os.path.exists("new_test.py"))

#print(os.path.isfile("calculator.py"))

print(os.path.splittext(path_to_calculator))
path_less_suffix = os.path.splittext(path_to_calculator)[0]
print(os.path.splitext(path_less_suffixx))