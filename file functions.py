'''
seek function leaves n characters forward
eg:
first parameter- offset value
second parameter- beg, cur, end (by default it is )
seek goes to the specified position
'''
txt=open('hello.txt','rb')

txt.seek(2,0)  #from the beginning, seek two characters---- goes to the second character
print(txt.tell())           #cursor position
print(txt.read())           #the answer

txt.seek(-5,2)  #from end, go 5 characters back
                        #tell()--tell where we are(always in positive)
print(txt.tell())           #cursor position
print(txt.read())        #if you use only read(), you can move only from the start of file
