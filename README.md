# ProjetoMQTT

# Configurando o EVE-NG

## Adicionar a imagem do Ubuntu no EVE-ng

1. Crie uma pasta em `/opt/unetlab/addons/qemu`. A pasta deve seguir o padrão: `linux-versão`.
2. Dentro da pasta criada, adicione a imagem do Linux Ubuntu.

## Configurando Cenário

1. Abra o EVE-ng e crie uma nova topologia.
2. Adicione três máquinas Linux:
- Broker MQTT
- Dispositivo Lâmpada
- Controlador

### Configurar Conexões

1. Conecte os dispositivos usando links Ethernet.
2. Certifique-se de que os dispositivos possam se comunicar entre si.

### Configurar o Broker MQTT

1. Instale e configure um broker MQTT no dispositivo designado como Broker MQTT. Utilize o Mosquitto.
   
   - Instalação:
     ```
     $ sudo apt-get update
     $ sudo apt-get install mosquitto
     ```

   - Verificação do Serviço Mosquitto:
     ```
     $ sudo systemctl status mosquitto
     ```

### Adicione o Código Python da Lâmpada

1. Crie um arquivo de texto e adicione o código Python da lâmpada no dispositivo designado como Lâmpada.
2. Certifique-se de que as dependências estão instaladas no dispositivo.

   - Pip:
     ```
     $ apt install python-pip
     ```

   - Paho:
     ```
     $ pip install paho-mqtt
     ```

   - Tkinter:
     ```
     $ sudo apt-get install python3-tk
     ```

   - Pillow:
     ```
     $ pip install Pillow
     ```

### Configurar o Controlador

1. Carregue um script no dispositivo designado como Controlador. Este script será responsável por enviar comandos para ligar ou desligar a lâmpada via MQTT.

## Executar e Testar

1. Inicie os dispositivos no EVE-ng.
2. Execute o broker MQTT.
3. Execute o código Python da lâmpada no dispositivo Lâmpada.
4. Execute o script do Controlador para enviar comandos MQTT para ligar/desligar a lâmpada.

