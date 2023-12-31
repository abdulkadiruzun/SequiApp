import tkinter as tk
import datetime
import os

# oluşturulan dosyalarda zaman damgası kullanabilmek için date değişkeni oluşturuldu
date = datetime.datetime.now()

window=tk.Tk()
window.title("Sequi App | İş Dosyası Oluşturma")
window.geometry("500x500")
window.configure(background="#EBF3E8")

# iş adı alınıyor
jobName=tk.Label(text="İş dosyası oluşturmak için dosya adını giriniz", font="Arial 14 bold", fg="#86A789")
jobName.pack()
space = tk.Label(text = "\n")
space.pack()

# Entry ile input alındı, width ile alan ölçüsü belirlendi
jobNameInput=tk.Entry(width=25, font=12)
jobNameInput.pack()

# iş adı onaylama ve işlem doğrulama fonksiyonu tanımlandı
def jobNameVerifired():
    # dosya ismi jobNameInput'tan gelen veriye eşitlendi
    # jobNameInput'tan gelen veri tipi tk.label
    # jobNameInput'tan gelen veriyi dosya isminde kullanmamız gerektiği için veri str'a dönüştürüldü
    name=str(jobNameInput.get())
    space = tk.Label(text = "\n")
    space.pack()
    # girilen dosya ismiyle dosya oluşturuldu mesajı verildi
    fileCreateMessage=tk.Label(text=name + " Dosyası oluşturuldu!", font=10)
    fileCreateMessage.pack()
    # girilen dosya ismiyle txt dosyası oluşturuldu, append ile açıldı
    fileCreate = open(name + ".txt", "a")
    # dosyaya yazdırma için createDate değişkeni olşturuldu ve parametre olarak date değişkeni verildi
    CreateDate = datetime.datetime.ctime(date)
    # dosya adı ve ne zaman oluşturulduğu oluşturulan text dosyasına yazıldı
    fileCreate.write(name + " Dosyasi " + CreateDate + " tarihinde olusturuldu.")

space = tk.Label(text = "\n")
space.pack()

# iş adı onaylama ve işlem doğrulama butonu tanımlandı
# aksiyon olarak jobNameVerifired fonksiyonu verildi
jobNameVerifiredButton=tk.Button(text=   "Onayla",
                                bg=      "#B2C8BA",
                                fg=      "black",
                                font=    "Arial 11",
                                width=   25,
                                command= jobNameVerifired)
jobNameVerifiredButton.pack()

space = tk.Label(text = "\n")
space.pack()

# klasördekli txt dosyalarını listeleme
def workFolder():
    # os ile dizin içine bakıldı
    sequiapp = os.getcwd()
    workFilesName = tk.Label(text="Klasördeki iş dosyaları", fg="black", font=10)
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

# dosyaları listeleme
fileList=tk.Button(text=  "Dosyaları Göster",
                bg=       "#B2C8BA",
                fg=       "black",
                font=     "Arial 11",
                width=    25,
                command=  workFolder)
fileList.pack()

# ana menüye dönüş
backButton=tk.Button(text=   "Geri Dön",
                    bg=      "#B2C8BA",
                    fg=      "black",
                    font=    "Arial 11",
                    width=   25,
                    command= window.destroy)
backButton.pack()

space = tk.Label(text = "\n")
space.pack()

# kod hızlıca çalışıp ekran hemen gitmemesi içn mainloop'a aldık
window.mainloop()