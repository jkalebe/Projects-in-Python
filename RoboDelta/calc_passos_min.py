file = open('logo_passos.txt', 'r')
vetor_file = file.read().splitlines()
file.close()

file = open('logo_passos.txt', 'r')
file_new = open('logo_passos_min.txt', 'w')


i=0
for linha in file:
    l = linha.split()
    #print(l)
    sinal1= -1 if '-' in l[0] else 1   
    sinal2= -1 if '-' in l[1] else 1
    sinal3= -1 if '-' in l[2] else 1

    if i != 0:
        m1 = abs(int(l[0])) - abs(int(vetor_file[i-1].split()[0]))
        m2 = abs(int(l[1])) - abs(int(vetor_file[i-1].split()[1]))
        m3 = abs(int(l[2])) - abs(int(vetor_file[i-1].split()[2]))
        
        m1 = abs(m1)*sinal1
        m2 = abs(m2)*sinal2
        m3 = abs(m3)*sinal3
        linha_new = f'{m1} {m2} {m3}\n'
        print(linha_new)
        file_new.write(linha_new)
    else:
        file_new.write(linha)
    
    i=i+1
    
    



    

file.close()
file_new.close()