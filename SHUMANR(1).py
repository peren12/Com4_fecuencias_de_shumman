import serial
import time


class receptor(object):

    def __init__(self):
        self.PUERTO = 'COM4'
        self.TASA = '115200'
        self.ARCHIVO = 'DATOS.txt'
        self.DATA = []
        self.f = 0
        
    def conectar(self):
        print 'Bienvenido'

        try:
            tiva = serial.Serial(self.PUERTO, self.TASA)
        except:
            print 'Error de conexion'

        while(1):
            if(len(self.DATA) < 2):
                d = tiva.read()
                if (self.f == 1 and d != ''):
                    self.DATA.append(d)
                    #print d

                if ord(d) == 254:
                    self.f = 1

            else:
                self.f = 0
                n = ord(self.DATA[0])+256*ord(self.DATA[1])
                #print n
                self.DATA = []
                self.archivo(n)
                
    def archivo(self, n):
        datos = open(self.ARCHIVO, 'a')
        #datos.write(','.join(self.DATA)+',\n')
        #print self.DATA
        datos.write(str(n)+',\n')
        datos.close()

def run():
    try:
        r = receptor()
        r.conectar()
    except KeyboardInterrupt:
        try:
            tiva.close()
        except NameError:
            None
        try:
            datos.close()
        except NameError:
            None

            
        print '\nSalio\n'

run()
