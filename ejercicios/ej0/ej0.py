import rclpy
import rclpy.logging
from  rclpy.node  import Node
import rclpy.qos
from std_msgs.msg import String,Bool,Int16,Float32
import random



class EJ0(Node):
    def __init__(self):
        super().__init__('Desencriptador')
        self.f = open('archivo','r')
        self.escondido=self.f.readlines()
        #print(self.escondido)
        self.f.close()
        self.sub_4=self.create_subscription(msg_type=String,topic='paso_3',callback=self.paso_3,qos_profile=rclpy.qos.qos_profile_sensor_data)       
        self.sub_3=self.create_subscription(Float32,'paso_2',self.paso_2,qos_profile=rclpy.qos.qos_profile_sensor_data)
        self.sub_2=self.create_subscription(Int16,'paso_1',self.paso_1,qos_profile=rclpy.qos.qos_profile_sensor_data)
        self.sub_1=self.create_subscription(String,'tu_nombre_paso_0',self.paso_0,qos_profile=rclpy.qos.qos_profile_sensor_data)
        self.pub = self.create_publisher(String,'respuesta',qos_profile=rclpy.qos.qos_profile_sensor_data) 

        self.timer=self.create_timer(0.1,self.run)
        self.bandera=False
        self.msg=String()
        msg='Iniciando el ejercicio 0. Para comenzar debes publicar en el topic correcto tu nombre en minusculas.'
        self.get_logger().info(msg)
        self.msg.data=msg
                    
    def run(self):          
        if self.bandera:
            self.bandera=False                       
            self.pub.publish(self.msg)        

    def paso_3(self,data):
        idx=3
        self.bandera=True    
        self.process_(data,idx)

        if self.msg.data!='codigo incorrecto':
            self.msg.data='Ejercicio finalizado!. Recuerda que cuando te pregunten tu clave es: '+ self.msg.data       
        else:
            self.msg.data='codigo incorrecto'

    def paso_2(self,data):
        idx=2
        self.process_(data,idx)


    def paso_1(self,data):
        idx=1
        self.process_(data,idx)


    def paso_0(self,data):
        idx=0
        self.process_(data,idx)

    def process_(self,data,idx):
        self.bandera=True    
        cc=self.cifrar_descifrar(self.escondido[0])
        cc=cc[idx]
        cc="".join(" "+d for d in cc)
        #
        dd=data.data
        if type(dd)==float:
            dd=round(dd,2)
        if type(dd)!=str:
            dd=str(dd)
        #import pdb;pdb.set_trace()
        pos=cc.find(dd)
        if pos>-1:
            nn=len(dd)
            txt=cc[pos+nn:].split()
            self.msg.data=txt[0]            
        else:
            self.msg.data='codigo incorrecto'

    
    def cifrar_descifrar(self,texto):
        dd="".join(chr(ord(c) ^ 37) for c in texto)
        ltc = dd.split('\n')
        listas = [linea.split() for linea in ltc]
        return listas
        
    

if __name__=='__main__':
    rclpy.init()
    ej=EJ0()
    rclpy.spin(ej)
    ej.destroy_node()
    rclpy.shutdown()
        
    
    