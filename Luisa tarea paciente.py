class Paciente:
    def __init__(self):
        self.__nombre = '' 
        self.__cedula = 0 
        self.__genero = '' 
        self.__servicio = '' 
              
    #metodos get    
    def verNombre(self):
        return self.__nombre 
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio 
    # metodos set
    def asignarNombre(self,n):
        self.__nombre = n 
    def asignarCedula(self,c):
        self.__cedula = c 
    def asignarGenero(self,g):
        self.__genero = g 
    def asignarServicio(self,s):
        self.__servicio = s 
        
class Sistema:    
    def __init__(self):
        self.__lista_pacientes = [] 
        
    def verificarPaciente(self,cedula):
        for p in self.__lista_pacientes:
            if cedula == p.verCedula():
                return True 
        return False
        
    def ingresarPaciente(self,pac):
        self.__lista_pacientes.append(pac)
        return True
    
    def verDatosPaciente(self, c):
        if self.verificarPaciente(c) == False:
            return None
        for p in self.__lista_pacientes:
            #retorne la cedula y la comparo con la ingresada por teclado
            if c == p.verCedula():
                return p #si encuentro el paciente lo retorno
            
    def verNumeroPacientes(self):
        print("En el sistema hay: " + str(len(self.__lista_pacientes)) + " pacientes") 

    def buscarPacientePorNombreOCedula(self, busqueda):
        pacientes_encontrados = []
        
        # Buscar por cédula (si la busqueda es un número entero)
        try:
            cedula = int(busqueda)
            for p in self.__lista_pacientes:
                if p.verCedula() == cedula:
                    pacientes_encontrados.append(p)
        except ValueError:
            # Si no se puede convertir a entero, es porque la busqueda es un nombre
            for p in self.__lista_pacientes:
                if p.verNombre().lower().startswith(busqueda.lower()):
                    pacientes_encontrados.append(p)
        
        return pacientes_encontrados

def main():
    sis = Sistema() 
    #probemos lo que llevamos programado
    while True:
        #TAREA HACER EL MENU
        opcion = int(input("\nIngrese \n0 para salir, \n1 para ingresar nuevo paciente, \n2 ver Paciente, \n3 Ver numero de pacientes, \n4 Ver datos de paciente mediente nombre o cedula \t--> ")) 
        
        if opcion == 1:
            #ingreso pacientes
            print("A continuacion se solicitaran los datos ...") 
            #1. Se solicitan los datos
            cedula = int(input("Ingrese la cedula: ")) 
            if sis.verificarPaciente(cedula):
                print("\n<< Ya existe un paciente con esa cedula >>".upper()) 
            else:    
                # 2. se crea un objeto Paciente
                pac = Paciente() 
                # como el paciente esta vacio debo ingresarle la informacion
                pac.asignarNombre(input("Ingrese el nombre: ")) 
                pac.asignarCedula(cedula) 
                pac.asignarGenero(input("Ingrese el genero: ")) 
                pac.asignarServicio(input("Ingrese servicio: ")) 
                #3. se almacena en la lista que esta dentro de la clase sistema
                r = sis.ingresarPaciente(pac)             
                if r:
                    print("Paciente ingresado") 
                else:
                    print("No ingresado") 
        elif opcion == 2:
            #1. solicito la cedula que quiero buscar
            c = int(input("Ingrese la cedula a buscar: ")) 
            #le pido al sistema que me devuelva en la variable p al paciente que tenga
            #la cedula c en la lista
            p = sis.verDatosPaciente(c) 
            #2. si encuentro al paciente imprimo los datos
            if p != None:
                print("Nombre: " + p.verNombre()) 
                print("Cedula: " + str(p.verCedula())) 
                print("Genero: " + p.verGenero()) 
                print("Servicio: " + p.verServicio()) 
            else:
                print("No existe un paciente con esa cedula") 

        elif opcion == 3:
            # Ver número de pacientes en el sistema
            if len(sis._Sistema__lista_pacientes) > 0:
                sis.verNumeroPacientes()  # Si hay pacientes, muestra la cantidad
            else:
                print("No hay pacientes en el sistema.")  # Si no hay pacientes
        elif opcion == 4:
            # Buscar paciente por cédula o nombre
            busqueda = input("Ingrese la cedula o el nombre del paciente a buscar: ")
            pacientes = sis.buscarPacientePorNombreOCedula(busqueda)
            
            if pacientes:
                for p in pacientes:
                    print("\nPaciente encontrado:")
                    print("Nombre: " + p.verNombre()) 
                    print("Cedula: " + str(p.verCedula())) 
                    print("Genero: " + p.verGenero()) 
                    print("Servicio: " + p.verServicio())
            else:
                print("No se encontró ningún paciente con esa cédula o nombre.")

        elif opcion == 0:
            # Salir del programa
            break
        else:
            # Mensaje para opciones inválidas
            print("Opción no válida. Por favor, ingrese una opción válida (0, 1, 2, 3).")


#aca el python descubre cual es la funcion principal
if __name__ == "__main__":
    main() 
        
        
        
        
        
        
        
        
