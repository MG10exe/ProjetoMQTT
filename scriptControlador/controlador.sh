#!/bin/bash

broker_address="<endereço_do_broker>"    # Substituir <endereço_do_broker> pelo ip do broker
topic="/casa/quarto/lampada"

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
