from opcua import Server
from random import randint
import datetime
import time

#server variable
server = Server()

#servers ip address
url = "opc.tcp://localhost:26543"
server.set_endpoint(url)

#setting a namespace (project name)
name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

#creating the root node
node = server.get_objects_node()

#creating an object that will hold various variables
Param = node.add_object(addspace, "Parameters")
#creating varibles to hold information on the object
Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)
#setting writable so they are mutable
Temp.set_writable()
Press.set_writable()
Time.set_writable()

#starting server
server.start()
print("Server started at {}".format(url))

#loop to continually randomly generate values for the object variables
while True:

    Temperature = randint(10, 50)
    Pressure = randint(100, 999)
    TIME = datetime.datetime.now()

    print(Temperature, Pressure, TIME)

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)