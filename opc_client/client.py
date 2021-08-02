from opcua import Client
import time

#variable to hold server address
url = "opc.tcp://localhost:26543"
#url = "opc.tcp://Zeta-Pro:4840/"

#variable to simplify "Client" variable
client = Client(url)

#actual connect command
client.connect()
print("Client Connected")

while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)

    TIME = client.get_node("ns=2;i=4")
    TIME_value = TIME.get_value()
    print(TIME_value)

    time.sleep(1)