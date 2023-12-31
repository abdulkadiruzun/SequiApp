# konsol ortamından daha iyi bir arayüz için tkinter kullandık
# kütüphane içindeki tk() sınıfını çağırıyoruz
import tkinter as tk
# dosya listeleme işlemlerinde kullanmak için os kütüphanesi
import os

# window adında bir nesne oluşturuldu
# tkinter modülündeki Tk() sınıfını çağırıyoruz
window = tk.Tk()
# pencere ismi verildi
window.title("Sequi App | İş Planlayıcısı")
# pencere boyutu ayarlandı
window.geometry("500x500")
# pencere arka planı tanımlandı
window.configure(background="#EBF3E8")

# ekrana yazı yazdırmak için introduction adında bir label tanımlandı
introduction = tk.Label(text="Sequi'ye Hoşgeldiniz",font="Arial 16 bold", fg="#86A789", bg="#EBF3E8")
# introduction içeriği pack() ile ekrana yazdırıldı
introduction.pack()

# ekrana yazı yazdırmak için introduction adında bir label tanımlandı
chooseText=tk.Label(text="\nLütfen yapmak istediğiniz seçeneği seçiniz", font="Arial 12", fg="black", bg="#EBF3E8")
# introduction içeriği pack() ile ekrana yazdırıldı
chooseText.pack()

space = tk.Label(text = "\n")
space.pack()

# iş dosyası tanımlama butonu oluşturuldu
def jobFileDescription():
    # dizin içerisindeki ilgili dosya cmd üzerinden açıldı
    os.system('cmd /c' "python jobFileDescription.py")
    
# aksiyon olarak jobDescription fonksiyonu verildi
jobFileDescriptionButton = tk.Button(text=  "İş Dosyası Tanımlama",
                               bg=      "#B2C8BA",
                               fg=      "black",
                               font=    "Arial 11",
                               width=   25,
                               command= jobFileDescription)

# iş tanımlama butonu oluşturuldu
def jobDescription():
    # dizin içerisindeki ilgili dosya cmd üzerinden açıldı
    os.system('cmd /c' "python jobDescription.py")
    
# aksiyon olarak jobDescription fonksiyonu verildi
jobDescriptionButton = tk.Button(text=  "Dosyaya İş Tanımlama",
                               bg=      "#B2C8BA",
                               fg=      "black",
                               font=    "Arial 11",
                               width=   25,
                               command= jobDescription)

# işe çalışan/takım ekleme butonu oluşturuldu
def team():
    # dizin içerisindeki ilgili dosya cmd üzerinden açıldı
    os.system('cmd /c' "python teamDescription.py")
    
# aksiyon olarak jobDescription fonksiyonu verildi
teamButton = tk.Button(text=  "Dosyaya Çalışan Ekleme",
                               bg=      "#B2C8BA",
                               fg=      "black",
                               font=    "Arial 11",
                               width=   25,
                               command= team)

# klasördekli txt dosyalarını listeleme
def workFolder():
    # os ile dizin içine bakıldı
    sequiapp = os.getcwd()
    workFilesName = tk.Label(text="\nKlasördeki iş dosyaları", fg="black", font=10)
    workFilesName.pack()
    # sequiapp içinde tarama yapıldı
    with os.scandir(sequiapp) as directory:
        doc = tk.Label()
        # yapılan tarama doc parametresi içine atıldı
        for doc in directory:
            # endswith ile sadece txt uzantılı dosyalar alındı
            if doc.name.endswith("txt"):
                fileName = tk.Label(text=doc.name + " dosyası")
                fileName.pack()

# dosyaları listeleme fonksiyonu çağırıldı
fileList=tk.Button(text=  "İş Dosyalarını Göster",
                bg=       "#B2C8BA",
                fg=       "black",
                font=     "Arial 11",
                width=    25,
                command=  workFolder)

# işe çalışan/takım ekleme butonu oluşturuldu
def messaging():
    # dizin içerisindeki ilgili dosya cmd üzerinden açıldı
    os.system('cmd /c' "python clients.py")
    
# aksiyon olarak messaging fonksiyonu verildi
messagingButton = tk.Button(text=  "Mesajlaşma Başlat",
                               bg=      "#B2C8BA",
                               fg=      "black",
                               font=    "Arial 11",
                               width=   25,
                               command= messaging)

# fonksiyonlar çağırıldı
jobFileDescriptionButton.pack()
jobDescriptionButton.pack()
teamButton.pack()
fileList.pack()
messagingButton.pack()

# kod hızlıca çalışıp ekran hemen gitmemesi içn mainloop'a aldık
window.mainloop()