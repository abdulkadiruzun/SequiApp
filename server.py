# socket ve threading çağrıldı
from socket import *
from threading import *

# client ve names adında diziler oluşturuldu 
clients = []
names = []

# thread için fonksiyon oluşturuldu
def clientThread(client):
    # bağlantının doğruluğu kontrol için flag isimli değişken oluşturuldu
    flag = True
    while True:
        try:
            # mesajın client'tan gelen paketler olduklarını ve ne ile çözüleceklerini blirlendi
            message = client.recv(1024).decode('utf8')
            if flag:
                # bağlanan kullanıcı için server'da mesaj yazdırıldı
                names.append(message)
                print(message, 'bağlandı')
                flag = False
            # mesajlar ile gönderilen -mesajın yanındaki isimler- aşağıdaki döngüde veriliyor    
            for i in clients:
                if i != client:
                    index = clients.index(client)
                    name = names[index]
                    i.send((name + ':' + message).encode('utf8'))
        # client mesajlaşmadan çıkınca server'da kayıt bırakıyor
        except:
            index = clients.index(client)
            clients.remove(client)
            name=names[index]
            # mesaj indexlerinden logout olan user siliniyor
            names.remove(name)
            print(name + ' çıktı')
            break

# server'in hangi portları dinleyeceği bilgisi verildi 
server = socket(AF_INET, SOCK_STREAM)
 
ip = '127.0.0.1'
port = 888
server.bind((ip, port))
server.listen()
print('Server dinlemede...')
 
# request'lere true cevap döndüğünde bağlantı başarılı mesajı veriliyor
while True:
    client, address = server.accept()
    clients.append(client)
    print('Bağlantı yapıldı..', address[0] + ':' + str(address[1]))
    thread = Thread(target=clientThread, args=(client, ))
    thread.start()