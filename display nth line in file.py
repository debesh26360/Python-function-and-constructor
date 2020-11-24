'''
        WAP to open file and display nth line from beginning of file 
'''

#can use indexing

filename=input('Enter file name')
n=int(input('Enter file line number'))

data=[]
f=open(filename)
data.extend(f.readlines())

print(data[n-1])
