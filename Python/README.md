# Paho MQTT Python
## Instalação
* Linux
```
python3 -m venv paho-mqtt
source paho-mqtt/bin/activate
pip3 install -r ./requirements.txt
```
* Windows
```
python -m venv paho-mqtt
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
.\paho-mqtt\Scripts\activate
pip install -r ./requirements.txt
```
## Exemplos
1. Conexão: opções de conexão e tratamento de erro
2. Publicação: funcionamento das publicações, flags e qualidades de serviço
3. Assinatura: assinatura de tópicos, qualidade de serviço e coringas