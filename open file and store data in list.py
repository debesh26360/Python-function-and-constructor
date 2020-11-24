'''
        WAP to open file and store data in list
'''

data=[]

f=open('colors.txt')
#data.extend(f.read())      #extend considers each alphabet in colors.txt as an object
data.extend(f.readlines())

print(data)
