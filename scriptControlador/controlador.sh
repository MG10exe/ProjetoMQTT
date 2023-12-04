#!/bin/bash

broker_address="<endereço_do_broker>"
topic="<nome_do_tópico>"

ligar() {
    mosquitto_pub -h $broker_address -t $topic -m "ligar"
}

desligar() {
    mosquitto_pub -h $broker_address -t $topic -m "desligar"
}

if [ "$1" == "ligar" ]; then
    ligar
elif [ "$1" == "desligar" ]; then
    desligar
else
    echo "Uso: $0 [ligar|desligar]"
fi