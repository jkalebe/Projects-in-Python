
file = open('logo.txt', 'r')

for i in file:
    #print(i)
    l= i.split(' ')
    x=l[0]
    y=l[1]
    z=l[2]
    #print(f'{x}, {y}, {z}')
    print(l)
