f_name = input("Input File Name: ")
try :
    fhandle = open(fname+".txt")
except :
    print("Can't Open A File")
    quit()

numlist = list()

for word in fhandle:
    print(word)
