'''
        WAP to open file and display first n lines from last
'''



filename=input('Enter file name')
n=int(input('Enter number of lines from last'))

data=[]
f=open(filename)
data.extend(f.readlines())

print(data[-1:-(n+1):-1])            #n because n is the end point and will
                                    #till n-1. n will not be printed
