import pickle

class Profesionales:

    def __init__(self,nombre,apellido,mail,profesion,sueldo,lugarderesidencia):

        self.nombre=nombre
        self.apellido=apellido
        self.mail=mail
        self.profesion=profesion
        self.sueldo=sueldo
        self.lugarderesidencia=lugarderesidencia
        print ("Se cargo un profesional de nombre: ",self.nombre)

    def __str__(self):
        return ("{} {} {} {} {} {}".format(self.nombre,self.apellido,self.mail,self.profesion,self.sueldo,self.lugarderesidencia))

class ListaProfesionales:

    profesionales=[]

    def __init__(self):
        listaprofesionales=open("listaprofesionales","ab+")
        listaprofesionales.seek(0)
        try:
            self.profesionales=pickle.load(listaprofesionales)
            print ("se cargaron {} profesionales".format(len(Profesionales)))
        except:
            print (" lista vacia")
        finally:
            listaprofesionales.close()
            del(listaprofesionales)

    def agregarPRofesionalFicheroExterno(self):
        listaprofesionales=open("listaprofesionales","wb")
        pickle.dump(self.profesionales,listaprofesionales)
        listaprofesionales.close()
        del(listaprofesionales)
    
    def mostrarInformacionFicheroExterno(self):
        print ("Mostrando informacion del fichero externo....")
        print("")
        for p in self.profesionales:
            print("")
            print(p)


    def guardoProfesional(self,p):
        
        self.profesionales.append(p)
        self.agregarPRofesionalFicheroExterno()

    def muestroProfesionales(self):
        for p in self.profesionales:
            print (p)

def cargandoProfesional():
    
    milista=ListaProfesionales()
    while(True):
        nombre=input("Ingresar nombre: ")
        if nombre ==(""):
            break
        else:
            apellido=input("Ingresar apellido: ")
            email=input("Ingrese su email: ")
            profesion=input("Ingrese su profesion: ")
            salario=input("Ingrese su salario: ")
            residencia=input("Igrese lugar de residencia: ")
            miprofesional=Profesionales(nombre,apellido,email,profesion,salario,residencia)
            milista.guardoProfesional(miprofesional)
           
    return milista

def buscoProfPorSalario():   
    listapro=open("listaprofesionales","rb")
    losprofe=pickle.load(listapro)
    listapro.close()
    print("\nEl programa buscara los profesionales que ganan menos del salario especificado")
    profesion=input("profesion que busca: ")
    salario=int(input("Salario que busca: "))
    #Print ("")
    print("\n{} que ganan menos de {}".format(profesion,salario))
    for c in losprofe :
        profesionales = (str(c).split(" "))
        if (profesionales[3]==profesion and int(profesionales[4])<salario):
            print(profesionales[2])
                    
def principal():
    print("\nElija que desea hacer:")
    print("Para cargar profesionale a la lista presione (1).")
    print("Para obtener los datos de todos los profesionales presione (2).")
    print("Para obtener el mail de que puedan querer cambiar de trabajo presione (3).")
    print("Para salir presione (4).")
    opcion=input("ingrese una opcion: ")
    while(True):
        if opcion=="1":
            cargandoProfesional()
            return principal()
        elif opcion=="2":
            listapro=open("listaprofesionales","rb")
            losprofe=pickle.load(listapro)
            listapro.close()
        #Print ("")
            print("\nLista de todos los profesionales")
            for c in losprofe :
                profesionales = (str(c).split(" "))
                print(profesionales)
            return principal()
            
        elif opcion=="3":
            buscoProfPorSalario()
            return principal()
            
        elif opcion == "4":
            print("\nPrograma terminado")
            break
        else:
            print("\nOpcion incorrecta!!")
            opcion=input("ingrese una opcion: ")

principal()













