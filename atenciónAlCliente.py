from collections import deque

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.solicitudes = 0

# Clase para implementar los nodos de la lista enlazada de clientes frecuentes
class NodoClienteFrecuente:
    def __init__(self, cliente):
        self.cliente = cliente
        self.siguiente = None

# Clase principal que gestiona el centro de atención
class CentroAtencion:
    def __init__(self):
        # Cola para almacenar solicitudes pendientes (FIFO: First In, First Out)
        # Utilizamos deque por su eficiencia en operaciones de inserción/eliminación en ambos extremos
        self.cola_solicitudes = deque()
        
        # Lista utilizada como pila para el historial (LIFO: Last In, First Out)
        # Las operaciones de push (append) y pop (pop) en el final de la lista son O(1)
        self.pila_historial = []
        
        # Arreglo/lista para almacenar todos los clientes registrados
        # Permite búsqueda por nombre y acceso aleatorio a los clientes
        self.clientes = []
        
        # Cabeza de la lista enlazada de clientes frecuentes
        # Inicialmente vacía (None)
        self.lista_frecuentes = None   
    
    # Método para registrar una nueva solicitud en la cola
    def registrar_solicitud(self, nombre, descripcion):
        cliente = self.obtener_cliente(nombre)
        cliente.solicitudes += 1
        self.cola_solicitudes.append((cliente, descripcion))
        if cliente.solicitudes > 5:
            self.agregar_cliente_frecuente(cliente)
        print(f"Solicitud registrada para {nombre}: {descripcion}")
    
    # Método para atender la solicitud más antigua de la cola
    def atender_solicitud(self):
        if not self.cola_solicitudes:
            print("No hay solicitudes pendientes.")
            return
        cliente, descripcion = self.cola_solicitudes.popleft()
        self.pila_historial.append((cliente, descripcion))
        print(f"Atendiendo solicitud de: {cliente.nombre} - {descripcion}")
    
    # Método para consultar el último caso atendido (tope de la pila)
    def consultar_historial(self):
        if not self.pila_historial:
            print("No hay historial de atenciones.")
            return
        cliente, descripcion = self.pila_historial[-1]
        print(f"Último caso atendido: {cliente.nombre} - {descripcion}")

    # Método para agregar un cliente a la lista enlazada de clientes frecuentes
    def agregar_cliente_frecuente(self, cliente):
        if self.es_cliente_frecuente(cliente):
            return
        nuevo_nodo = NodoClienteFrecuente(cliente)
        nuevo_nodo.siguiente = self.lista_frecuentes
        self.lista_frecuentes = nuevo_nodo
        print(f"Cliente frecuente agregado: {cliente.nombre}")
    
    # Método para verificar si un cliente ya está en la lista de frecuentes
    def es_cliente_frecuente(self, cliente):
        actual = self.lista_frecuentes
        while actual:
            if actual.cliente == cliente:
                return True
            actual = actual.siguiente
        return False
    
    # Método para obtener un cliente por su nombre o crear uno nuevo
    def obtener_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        nuevo_cliente = Cliente(nombre)
        self.clientes.append(nuevo_cliente)
        return nuevo_cliente

    # Método para listar todos los clientes registrados
    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        print("\n=== LISTADO DE CLIENTES ===")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i}. {cliente.nombre} - Solicitudes: {cliente.solicitudes}")

    # Método para listar los clientes frecuentes
    def listar_clientes_frecuentes(self):
        if not self.lista_frecuentes:
            print("No hay clientes frecuentes registrados.")
            return
        print("\n=== CLIENTES FRECUENTES ===")
        actual = self.lista_frecuentes
        contador = 1
        while actual:
            print(f"{contador}. {actual.cliente.nombre} - Solicitudes: {actual.cliente.solicitudes}")
            actual = actual.siguiente
            contador += 1

    # Método para listar las solicitudes pendientes en la cola
    def listar_solicitudes_pendientes(self):
        if not self.cola_solicitudes:
            print("No hay solicitudes pendientes.")
            return
        print("\n=== SOLICITUDES PENDIENTES ===")
        for i, (cliente, descripcion) in enumerate(self.cola_solicitudes, 1):
            print(f"{i}. {cliente.nombre} - {descripcion}")

def mostrar_menu():
    print("\n" + "="*40)
    print("SISTEMA DE ATENCIÓN AL CLIENTE")
    print("="*40)
    print("1. Registrar nueva solicitud")
    print("2. Atender próxima solicitud")
    print("3. Consultar último caso atendido")
    print("4. Listar clientes registrados")
    print("5. Listar clientes frecuentes")
    print("6. Ver solicitudes pendientes")
    print("0. Salir")
    print("="*40)
    return input("Seleccione una opción: ")

def ejecutar_sistema():
    centro = CentroAtencion()
        
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            descripcion = input("Ingrese la descripción de la solicitud: ")
            centro.registrar_solicitud(nombre, descripcion)
        
        elif opcion == "2":
            centro.atender_solicitud()
        
        elif opcion == "3":
            centro.consultar_historial()
        
        elif opcion == "4":
            centro.listar_clientes()
        
        elif opcion == "5":
            centro.listar_clientes_frecuentes()
        
        elif opcion == "6":
            centro.listar_solicitudes_pendientes()
        
        elif opcion == "0":
            print("Gracias por usar el Sistema de Atención al Cliente. ¡Hasta pronto!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el sistema
if __name__ == "__main__":
    ejecutar_sistema()