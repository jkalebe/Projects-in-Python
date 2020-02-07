file = open('logo_pontos.txt', 'r')
file_write = open('logo_passos.txt', 'w')

for linha in file:
    l = linha.split()
    
    if l[0] != '\n':
        
        m1=round(float(l[0])/(1/16))
        m2=round(float(l[1])/(1/16))
        m3=round(float(l[2])/(1/16))

        linha_write = f'{m1} {m2} {m3}\n'
        file_write.write(linha_write)
        print(linha_write)
       
file.close()
file_write.close()