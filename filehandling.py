with open("Info.txt",'r') as fp:
    # next(fp)          #skip the first line
    # lines = fp.readlines()[1:]    #skips first line
    
    # print(fp.read())    #read all at once
    
    # print(fp.read(10))    #read first characters
    
    # print(fp.readline()) #read one line at once
    
    # print(fp.readlines())   #return list of all lines in file
    
    # print(fp.readlines(500))   #return lines containing 500 bytes
    
    # print(fp.readable())    #True if file can be read
    
    # fp.truncate(30)   #Reduces the size of file to the specified bytes
    
    # print(fp.writable())    #Returns True if file can be written into (depends on the mode of operation) 
    
    # fp.write('This is a sample text to be written in the file.')    #writes the content in the file
    
    # fp.writelines(['hello','how\n','are','you\n'])  #write the list of strings into the file
    
    # print(fp.reconfigure())       #no idea
    
    '''
        a - append
        w - write/overwrite
        r - read
        a+ - read + append //file pointer points to the end of the file
        w+ - write + read //creates a new file everytime first
        r+ - read + write //different from a+ as it starts the file pointer from the beginning of the file
    '''
    