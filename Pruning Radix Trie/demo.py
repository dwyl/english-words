file1 = open("words_alpha.txt","r")
file2 = open("some.txt","w")
for i,line in enumerate(file1):
    s = "\""
    if line[-1] == "\n":
        s += line[:-1]
        s += "\",\n"
    else:
        s += line
        s +="\""
    
    file2.write(s)
