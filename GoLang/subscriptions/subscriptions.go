package subscriptions

import (
	mqtt "github.com/eclipse/paho.mqtt.golang"
	"github.com/labstack/gommon/log"
)

const QOS byte = byte(2)

func OnMessage(c mqtt.Client, m mqtt.Message) {
	// decompondo a mensagem em um JSON
	log.Printj(log.JSON{
		"messageID":  m.MessageID(),
		"topic":      m.Topic(),
		"qos":        m.Qos(),
		"retained":   m.Retained(),
		"duplicated": m.Duplicate(),
		"payload":    string(m.Payload()),
	})
}

func Subscribe(client mqtt.Client, base string) {
	// usando uma função personalizada para tratar as mensagens desse tópico
	token := client.Subscribe(base+"/entrada", QOS, OnMessage)

	<-token.Done()

	if token.Error() != nil {
		log.Error(token.Error())
	}
}
