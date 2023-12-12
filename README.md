# Simulação do uso do protocolo MQTT no EVE-ng

## Configurando o EVE-NG

## Adicionar a imagem do Ubuntu no EVE-ng

1. Para o projeto foi utilizado a imagem do ubuntu-18.04-server disponível em: `https://drive.google.com/drive/mobile/folders/1ogOU6WkanlQmkOiSkXk0lEg9cE4o-3zB?usp=sharing `
2. Crie uma pasta em `/opt/unetlab/addons/qemu`. A pasta deve seguir o padrão: `linux-versão`.
3. Dentro da pasta criada, adicione a imagem linux que será utilizada.

## Configurando o Cenário

1. Abra o EVE-ng e crie uma nova topologia.
2. Adicione três máquinas Linux:
- Broker MQTT
- Dispositivo Lâmpada
- Controlador

### Configurar Conexões

1. Conecte os dispositivos usando links Ethernet.
2. Certifique-se de que os dispositivos possam se comunicar entre si.

### Configurar a máquina Broker MQTT

1. Instale e configure um broker MQTT no dispositivo designado como broker. Utilize o Mosquitto.
   
   - Instalação:
     ```
     $ sudo apt-get update
     $ sudo apt-get install mosquitto
     ```

   - Verificação do Serviço Mosquitto:
     ```
     $ sudo systemctl status mosquitto
     ```

### Configurar a máquina da lâmpada

1. Carregue o código da lâmpada com as imagens no dispositivo designado como lâmpada.
2. Adicione o endereço ip do broker MQTT na linha indicada no código da lâmpada.
3. Ajuste o caminho para as imagens no código da lâmpada. 
4. Faça a instalação das seguintes dependências:

   - Pip:
     ```
     $ apt install python3-pip
     ```

   - Paho:
     ```
     $ pip3 install paho-mqtt
     ```

   - Tkinter:
     ```
     $ sudo apt-get install python3-tk
     ```
     
   - Zlib:
     ```
     $ sudo apt-get install zlib1g-dev
     ```
     
   - Jpeg:
     ```
     $ sudo apt-get install libjpeg-dev
     ```
     
   - Pillow:
     ```
     $ pip3 install Pillow
     ```

### Configurar a máquina do controlador

1. Instale o pacote do mosquitto clientes:
   ```
   $ sudo apt-get update
   ```
   ```
   $ sudo apt-get install mosquitto-clients
   ```
2. Carregue o script `controlador.sh` no dispositivo designado como Controlador. Este script será responsável por enviar comandos para ligar ou desligar a lâmpada via MQTT.
3. Torne-o executável:
   ```
   $ sudo chmod +x controlador.sh
   ```
     
## Executar e Testar

1. Execute o código Python da lâmpada no dispositivo Lâmpada:
   ```
   $ python3 lampada.py
   ```
   
2. Execute o script do Controlador para enviar comandos MQTT para ligar/desligar a lâmpada:
   ```
   $ ./controlador.sh ligar
   ```
      ```
   $ ./controlador.sh desligar
   ```
![Sem título 6_1080p](https://github.com/MG10exe/ProjetoMQTT/assets/61914401/7fc19eb6-ac11-4434-b084-437bb21411c5)
