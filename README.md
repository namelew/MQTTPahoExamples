# MQTTPahoExamples
Um repositório para guardar códigos de testes das diferentes implementações da biblioteca paho mqtt
## Avisos
Para todos os casos, é necessário instalar um broker para utilizar a biblioteca. O Mosquitto foi escolhido para essa função e ser instalado via docker com o arquivo 'docker-compose.yaml' na raiz do projeto. Para instalar o Mosquitto:
* Docker
```
docker compose up -d broker
```
* Linux (Debian)
```
sudo apt-get install mosquitto -y
```
Ps: fique livre para utilizar qualquer broker que desejar.
## Biblioteca
O Paho MQTT é uma biblioteca mantida pela Eclipse que permite a criação de clientes para redes que utilizam o protocolo MQTT para comunicação. No momento, está disponível para as linguagens abaixo:

* [Java](http://search.maven.org/#search%7Cga%7C1%7Ca%3A%22org.eclipse.paho.client.mqttv3%22)
* [Python](https://pypi.org/project/paho-mqtt/)
* [JavaScript](https://www.eclipse.org/downloads/download.php?file=/paho/releases/1.0.3/paho.javascript-1.0.3.zip)
* [GoLang](https://github.com/eclipse/paho.mqtt.golang/releases/tag/v1.1.0)
* [C](https://github.com/eclipse/paho.mqtt.c/releases/tag/v1.3.9)
* [C++](https://github.com/eclipse/paho.mqtt.cpp/releases/tag/v1.0.0)
* [Rust](https://github.com/eclipse/paho.mqtt.rust)
* [DotNet (C#)](https://www.nuget.org/packages/M2Mqtt/4.3.0)

Entretando, nem todas possuem todas as features disponíveis pela biblioteca. Para mais informações olhar [Eclipse Paho Project](https://eclipse.dev/paho/index.php)