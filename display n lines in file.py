'''
        WAP to open file and display first n lines from beginning
'''



filename=input('Enter file name')
n=int(input('Enter file line number'))

data=[]
f=open(filename)
data.extend(f.readlines())

print(data[0:n])            #n because n is the end point and will
                                    #till n-1. n will not be printed
