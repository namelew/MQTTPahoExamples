import paho.mqtt.client as mqtt
import paho.mqtt.publish as pub

# Para simular um publicador externo, será utilizado um modulo da biblioteca que cria um cliente temporário
CLIENTID:str="python-test-client"

TOPIC:str="python-test-client/publication" # tópico de teste
QOS:int=2 # qualidade de serviço da assinatura

def on_message(client:mqtt.Client, userdata, msg:mqtt.MQTTMessage):
    if msg.topic == TOPIC:
        print(str(msg.payload))

client = mqtt.Client(client_id=CLIENTID, clean_session=False)

client.on_message = on_message

client.connect("localhost", 1883, 60)

client.subscribe(TOPIC, QOS)

pub.single(TOPIC, "essa eh uma mensagem de teste", 2)

try:
    client.loop_forever()
except KeyboardInterrupt:
    print()