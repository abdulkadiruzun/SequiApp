# ip ve port bilgileri ile iletişim için socket kütüphanesi eklendi
# multiple işlemler için (mesajların aynı anda gidip gelmesi) threading kütüphanesi eklendi
from socket import *
from threading import *
from tkinter import *

# client'ın nereye gideceği bilgisi verildi 
client = socket(AF_INET, SOCK_STREAM)
# client'ın gideceği adres
ip = '127.0.0.1'
# client'ın gideceği port
port = 888
# client ilgili adres ve porta yönlendirildi 
client.connect((ip, port))

# tkinter ile mesaj atılacak ekran oluşturuldu 
messagingWindow = Tk()
messagingWindow.title(ip + " adresli sunucuya " + str(port) + " üzerinden bağlandı")
# pencere boyutu ayarlandı
messagingWindow.geometry("500x550")
# pencere arka planı tanımlandı
messagingWindow.configure(background="#EBF3E8")

# mesaj alanı oluşturuldu 
messages = Text(messagingWindow, width=50)
messages.grid(row=0, column=0, padx=10, pady=10)
# mesaj yazılacak alan oluşturuldu
yourMessage = Entry(messagingWindow, width=80)
yourMessage.insert(0, 'Isminiz')
yourMessage.grid(row=1, column=0, padx=10, pady=10)
yourMessage.focus()
yourMessage.selection_range(0, END)
# mesaj gönderme fonksiyonu oluşturuldu
def sendMessage():
    clientMessage = yourMessage.get()
    messages.insert(END, '\n' + 'Siz: ' + clientMessage)
    client.send(clientMessage.encode('utf8'))
    yourMessage.delete(0, END)

# gönder butonu ve işlevi verildi 
messageSender = Button(messagingWindow, text='Gönder', width=20, command=sendMessage)
messageSender.grid(row=2, column=0, padx=10, pady=10)

# geri dön butonu ve işlevi verildi 
backButton = Button(messagingWindow, text='Geri Dön', width=20, command=messagingWindow.destroy)
backButton.grid(row=3, column=0, padx=10, pady=10)

# server'da yazılacak mesajlar için fonksiyon oluşturuldu 
def recvMessage():
    while True:
        # client'dan paketlerin ne ile çözümleneceği belirlendi
        serverMessage = client.recv(1024).decode('utf8')
        messages.insert(END, '\n' + serverMessage)
# thread işlemi başlatıldı 
recvThread = Thread(target=recvMessage)
recvThread.daemon = True
recvThread.start()
 
messagingWindow.mainloop()
