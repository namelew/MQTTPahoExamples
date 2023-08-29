import paho.mqtt.client as mqtt

CLIENTID:str="python-test-client" # caso vazio, é aleatório
PROTOCOLVERSION:int=4 # versão do protocolo MQTT: 3 (MQTTv311), 4 (MQTTv3111), 5 (MQTTv5)
TRANSPORT_PROTOCOL:str="tcp" # protocolo para o transporte de dados: tcp, websockets

# Função que será chamada ao receber a confirmação de conexão com o servidor
def on_connect(client:mqtt.Client, userdata, flags, rc):
    print("----- Connect Args -----")
    print(f"Client: {client}") # self
    print(f"User Data: {userdata}") # cabeçalhos definidos pelo usuário
    print(f"Flags: {flags}") # dicionário com as flags de resposta
    print(f"Response Code: {rc}") # código da resposta enviada pelo servidor

    # Assinando todos os tópicos de controle do broker
    # Como essa assinatura foi feita em on_connect, ela será desfeita se a conexão for perdida
    client.subscribe("$SYS/#")

# Função para tratar desconexão
def on_disconnect(client, userdata, rc):
    print("----- Disconnect Args -----")
    print(f"Client: {client}") # self
    print(f"User Data: {userdata}") # cabeçalhos definidos pelo usuário
    print(f"Response Code: {rc}") # código da resposta enviada pelo servidor

# Handler padrão para todas as mensagens publicas nos tópicos assinados
def on_message(client:mqtt.Client, userdata, msg:mqtt.MQTTMessage):
    print("----- Args -----")
    print(f"Client: {client}") # self
    print(f"User Data: {userdata}") # cabeçalhos definidos pelo usuário
    print(f"Mensagem: \n\t Tópico: {msg.topic}\n\t Payload: {str(msg.payload)}") # mensagem recebida

# criando cliente
client = mqtt.Client(
    client_id=CLIENTID,
    clean_session=True,
    protocol=PROTOCOLVERSION,
    transport=TRANSPORT_PROTOCOL,
    reconnect_on_failure=True,
)

# adicionando funções de callback
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# conectando no broker
client.connect("localhost", 1883, 60)

client.disconnect()

# reiniciando o cliente e alterando a sessão para persistente
client.reinitialise(CLIENTID, False, None)

# adicionando funções de callback
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# conectando no broker
client.connect("localhost", 1883, 60)

# bloqueando a thread principal para esperar o tráfego de rede
client.loop_forever()