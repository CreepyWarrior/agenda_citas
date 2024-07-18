from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client['citas_medicas']
usuario_collection = db['usuario']
citas_collection = db['citas']

def menu():
    print("\nMenú:")
    print("[1] Agregar un usuario")
    print("[2] Actualizar un usuario")
    print("[3] Borrar usuario")
    print("[4] Agregar cita")
    print("[5] Cancelar cita")


def agregar_usuario(nombre,curp,correo):
    user = {"nombre": nombre, "curp": curp, "correo": correo}
    usuario_collection.insert_one(user)

def borrar_usuario(id):
    usuario_collection.delete_one ({"nombre": id})

def actualizar_usuario(id,nombre,curp,):
    usuario_collection.update_one({"nombre": id}, {"$set": {"nombre": nombre, "curp":curp}})


def agregar_cita(nombre,hora,fecha):
    cita = { "nombre":nombre, "hora":hora,"fecha":fecha}
    citas_collection.insert_one(cita)

def cancelar_cita(id):
    citas_collection.delete_one({"cita": id})


while True:
   menu()
   opc = input("Seleccione una opcion: ")
   if opc == '1':
        nombre = input("Ingrese el nombre del usuario: ")
        curp = input("Ingrese la curp del usuario: ")
        correo = input("Ingresar el correo del usuario: ")
        agregar_usuario(nombre,curp,correo)
        print("Se agregado el usuario")

   if opc =='2':
        id = input("Ingrese el nombre a actualizar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        curp = input('Ingrese la nueva curp:')
        actualizar_usuario(id, nombre, curp)
        print("usuario actualizado")

   if opc == '3':
        id = input("Ingresa el nombre del usuario a ser eliminado: ")    
        borrar_usuario(id)
        print("usuario eliminado")

   if opc == '4':
      
       nombre = input("Ingrese el nombre del usuario: ")
       hora = input("Ingresa la hora  de la cita: ")
       fecha =input("Ingrese la fecha de la cita: ")
       agregar_cita(nombre,hora,fecha)
       print("Se agregado el usuario")

   if opc == '5':
       id = input("Ingrese la cita a cancelar: ")
       cancelar_cita(id)
       print("cita cancelada")