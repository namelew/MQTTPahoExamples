package main

import (
	"bufio"
	"log"
	"os"
	"os/signal"
	"syscall"

	mqtt "github.com/eclipse/paho.mqtt.golang"
	"github.com/namelew/MQTTPahoExamples/GoLang/subscriptions"
)

const CLIENTID string = "golang-test-client-01"
const TARGETID string = "golang-test-client-02"

const BROKERADRR string = "tcp://localhost:1883"
const QOS byte = byte(1)
const RETAINED bool = false

func main() {
	// redirecionando as saídas do cliente MQTT para o terminal
	mqtt.ERROR = log.New(os.Stdout, "[ERROR] ", 0)
	mqtt.CRITICAL = log.New(os.Stdout, "[CRIT] ", 0)
	mqtt.WARN = log.New(os.Stdout, "[WARN]  ", 0)
	mqtt.DEBUG = log.New(os.Stdout, "[DEBUG] ", 0)

	// criando cliente
	options := mqtt.NewClientOptions().
		SetClientID(CLIENTID).
		AddBroker(BROKERADRR)

	client := mqtt.NewClient(options)

	token := client.Connect()

	<-token.Done()

	if token.Error() != nil {
		log.Panic(token.Error().Error())
	}

	// realizando assinatura

	subscriptions.Subscribe(client, CLIENTID)

	// iniciando entrada com o usuário
	log.Println("Iniciando conversa...")

	c := make(chan os.Signal, 1)

	signal.Notify(c, os.Interrupt, syscall.SIGTERM)

	go func() {
		<-c
		log.Println("Finalizando exemplo...")
		client.Disconnect(10)
		os.Exit(0)
	}()

	r := bufio.NewReader(os.Stdin)

	log.Println("Envie uma mensagem digitando um texto e apertando ENTER")

	for {
		p, err := r.ReadSlice('\n')

		if err != nil {
			log.Println(err.Error())
			continue
		}

		token := client.Publish(TARGETID+"/entrada", QOS, RETAINED, p)

		<-token.Done()

		if token.Error() != nil {
			log.Println(token.Error().Error())
		}
	}
}
