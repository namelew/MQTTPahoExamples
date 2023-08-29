import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as sub

# Para simular um assinante externo, será utilizado um modulo da biblioteca que cria um cliente temporário
CLIENTID:str="python-test-client"

TOPIC:str="python-test-client/publication" # tópico de teste
QOS:int=0 # qualidade de serviço da mensagem
RETAINED=True # flag de retenção
PROPERTIES:mqtt.Properties=None # UserProperties do MQTTv5

client = mqtt.Client(client_id=CLIENTID, clean_session=True)

client.connect("localhost", 1883, 60)

# publicando mensagem
client.publish(TOPIC, "esta é uma mensagem de teste", QOS, RETAINED, PROPERTIES)

client.disconnect()

result = sub.simple(TOPIC)

print(f"Tópico: {result.topic}\nMensagem: {str(result.payload)}\nTimestamp: {result.timestamp}")