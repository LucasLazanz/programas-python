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
        return ("nombre: {}\napellido: {}\nEMail:{}\nprofesion:{}\nsueldo: {}\nresidencia: {}\n".format(self.nombre,self.apellido,self.mail,self.profesion,self.sueldo,self.lugarderesidencia))

class ListaProfesionales:

    profesionales=[]

    def __init__(self):
        listaprofesionales=open("listaprofesionales","ab+")
        listaprofesionales.seek(0)
        try:
            self.profesionales=pickle.load(listaprofesionales)
            print ("\nse cargaron {} profesionales".format(len(Profesionales)))
        except:
            print (" ")
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

    def buscoProfPorSalario(self):
        profesionales=open("listaprofesionales","rb")
        losprofe=pickle.load(profesionales)
        profesionales.close()
        del (profesionales)
        print("\nEl programa buscara los profesionales que ganan menos del salario especificado")
        profesion=input("profesion que busca: ")
        salario=int(input("Salario que busca: "))
        print("\n{} que ganan menos de {}".format(profesion,salario))
        pro=[]
        for c in losprofe :
            profesional = (str(c).split("\n"))
        
            if (profesional[3].split(":")[1]==profesion and int(profesional[4].split(":")[1]) < salario ):
                print(profesional[2])
        
                
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
        if nombre.isalpha():
            apellido=input("Ingresar apellido: ")
            if apellido != "" and  apellido.isalpha():
                email=input("Ingrese su email: ")
                if email != "" and "@" in email:
                    profesion=input("Ingrese su profesion: ")
                    if profesion != "" and profesion.isalpha():
                        salario=input("Ingrese su salario: ")
                        if salario != "" and salario.isdigit():
                            residencia=input("Igrese lugar de residencia: ")
                            if residencia != "" and residencia.isalpha():
                                miprofesional=Profesionales(nombre,apellido,email,profesion,salario,residencia)
                                milista.guardoProfesional(miprofesional)
                            else:
                                print("ingrese lugar de residencia")
                        else:
                            print("Ingrese un salario correcto")
                    else:
                        print("Ingrese datos correctos")
                else:
                    print("Email incorrecto")
            else:
                print("Apellido incorrecto")
        
        elif nombre ==(""):
            break
        else:
            print("Ingrese un nombre")
            

    return milista

def principal():
    l=ListaProfesionales()
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
        
            l.mostrarInformacionFicheroExterno()
            
            return principal()

        elif opcion=="3":
            l.buscoProfPorSalario()
            return principal()

        elif opcion == "4":
            print("\nPrograma terminado")
            break
        else:
            print("\nOpcion incorrecta!!")
            opcion=input("ingrese una opcion: ")

principal()













