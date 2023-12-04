import paho.mqtt.client as mqtt
import tkinter as tk
from PIL import Image, ImageTk

# Defina o tópico ao qual a lâmpada irá responder
lamp_topic = "/casa/quarto/lampada"

# Função para ligar a lâmpada
def ligar_lampada():
   client.publish(lamp_topic, "ligar")
   atualizar_imagem("ligada")

# Função para desligar a lâmpada
def desligar_lampada():
   client.publish(lamp_topic, "desligar")
   atualizar_imagem("desligada")

# Função para atualizar a imagem da lâmpada com base no estado
def atualizar_imagem(estado):
   if estado == "ligada":
       img = ImageTk.PhotoImage(Image.open("/home/eve/Downloads/codigoLampada/imgs/lampada_ligada.png"))
   else:
       img = ImageTk.PhotoImage(Image.open("/home/eve/Downloads/codigoLampada/imgs/lampada_desligada.png"))
   label_imagem.config(image=img)
   label_imagem.image = img

# Função de callback quando a conexão com o broker MQTT é estabelecida
def on_connect(client, userdata, flags, rc):
   print(f"Lâmpada conectada ao broker com resultado: {str(rc)}")
   client.subscribe(lamp_topic)

# Função de callback quando uma mensagem é recebida no tópico
def on_message(client, userdata, message):
   msg = message.payload.decode('utf-8')
   if msg == "ligar":
       print("Lâmpada ligada")
       atualizar_imagem("ligada")
   elif msg == "desligar":
       print("Lâmpada desligada")
       atualizar_imagem("desligada")

# Crie um cliente MQTT para a lâmpada
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Conecte-se ao broker MQTT
client.connect("127.0.0.1", 1883)  #substitua pelo ip do broker MQTT

# Crie a janela Tkinter
root = tk.Tk()
root.title("Controle da Lâmpada")

# Carregue a imagem da lâmpada desligada
img_desligada = ImageTk.PhotoImage(Image.open("/home/eve/Downloads/codigoLampada/imgs/lampada_desligada.png"))

# Crie um rótulo para exibir a imagem
label_imagem = tk.Label(root, image=img_desligada)
label_imagem.pack()

# Crie botões para ligar e desligar a lâmpada
ligar_button = tk.Button(root, text="Ligar Lâmpada", command=ligar_lampada)
desligar_button = tk.Button(root, text="Desligar Lâmpada", command=desligar_lampada)

# Posicione os botões na janela
ligar_button.pack()
desligar_button.pack()

# Inicie o loop de recepção de mensagens MQTT
client.loop_start()

# Inicie o loop da interface gráfica
root.mainloop()
