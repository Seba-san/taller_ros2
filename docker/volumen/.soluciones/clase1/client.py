import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import struct
import sys

class FloatToIntClient(Node):
    def __init__(self):
        super().__init__('square_float_client')
        self.cli = self.create_client(AddTwoInts, 'calculate_square')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando al servidor...')
        self.req = AddTwoInts.Request()

    def send_request(self, numero_float):
        # EMPAQUETAR: Convertimos el float en int64 para engañar a ROS 2
        numero_int = struct.unpack('q', struct.pack('d', numero_float))[0]
        
        self.req.a = numero_int
        self.req.b = 0 # No lo usamos
        
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        
        # DESEMPAQUETAR: Convertimos el int64 de la respuesta de vuelta a float
        resultado_int = self.future.result().sum
        resultado_float = struct.unpack('d', struct.pack('q', resultado_int))[0]
        
        return resultado_float

def main(args=None):
    # Validamos que el usuario haya escrito un argumento
    if len(sys.argv) < 2:
        print("Error: Falta el número.")
        print("Uso: python3 client.py <numero_o_expresion>")
        print("Ejemplo: python3 client.py 1/3")
        return

    # Tomamos lo que el usuario escribió después de "client.py"
    expresion = sys.argv[1]
    
    try:
        # eval() toma un texto como "1/3" o "5.5" y lo calcula matemáticamente.
        # Lo pasamos por float() para asegurarnos de que el resultado sea decimal.
        mi_numero = float(eval(expresion))
    except Exception as e:
        print(f"Error al entender el número o expresión matemática '{expresion}'.")
        print(f"Detalle del error: {e}")
        return

    # IMPORTANTE: Pasamos args=None a rclpy.init para que ROS 2 no se confunda
    # intentando leer "1/3" como si fuera un parámetro interno de ROS.
    rclpy.init(args=None)
    client = FloatToIntClient()
    
    print(f"Expresión ingresada: {expresion}")
    print(f"Valor convertido a float: {mi_numero}")
    print("Enviando al servidor...")
    
    # Llamamos al servicio
    resultado = client.send_request(mi_numero)
    
    print(f"¡El servidor devolvió el cuadrado!: {resultado}")
    
    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()