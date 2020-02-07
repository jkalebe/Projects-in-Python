import time
import serial
 
ser = serial.Serial('/dev/ttyUSB0', 9600)
file = open('logo_passos_min.txt', 'r')
vetor_file = file.read().splitlines()
file.close()

i=0
print('Enviando Dados')
while True:
    #chave = input('Comandos: ')
    print(f'Enviando dado {i}')
    
    ser.write(b'A ')
    
    chave = vetor_file[i].split()[0]
    ser.write(str.encode(chave))
    #ser.flush()
    #time.sleep(0.5)

    ser.write(b' B ')
    
    chave = vetor_file[i].split()[1]
    ser.write(str.encode(chave))
    #ser.flush()
    #time.sleep(0.5)

    ser.write(b' C ')
    
    chave = vetor_file[i].split()[2]
    ser.write(str.encode(chave))
    ser.write(b' ')
    ser.flush()
    time.sleep(1)

    
    if i < len(vetor_file):
        i=i+1
    #linha = ser.read()
    #print(f'Retorno: {linha}')

#ser.write(b'5') #Prefixo b necessario se estiver utilizando Python 3.X
#ser.read()