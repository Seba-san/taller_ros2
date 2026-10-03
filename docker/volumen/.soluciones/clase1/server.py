import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
import struct

class FloatToIntServer(Node):
    def __init__(self):
        super().__init__('square_float_server')
        self.srv = self.create_service(AddTwoInts, 'calculate_square', self.square_callback)
        self.get_logger().info('Servidor listo (Ocultando floats dentro de int64)')

    def square_callback(self, request, response):
        # 1. DESEMPAQUETAR: Convertimos el int64 de request.a en float
        # 'q' es int64 (long long), 'd' es float64 (double)
        # Empaquetamos el int64 en bytes y luego los leemos como float
        numero_float = struct.unpack('d', struct.pack('q', request.a))[0]
        
        # 2. OPERAR
        cuadrado = numero_float ** 2.0
        self.get_logger().info(f'Recibido (como float): {numero_float} -> Cuadrado: {cuadrado}')
        
        # 3. EMPAQUETAR: Convertimos el resultado float en int64 para la respuesta
        # Empaquetamos el float en bytes y los leemos como int64
        resultado_int = struct.unpack('q', struct.pack('d', cuadrado))[0]
        
        response.sum = resultado_int
        return response

def main(args=None):
    rclpy.init(args=args)
    node = FloatToIntServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()