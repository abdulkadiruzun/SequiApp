import tkinter as tk
import datetime
import os

# oluşturulan kişilerde zaman damgası kullanabilmek için date değişkeni oluşturuldu
date = datetime.datetime.now()

window=tk.Tk()
window.title("Sequi App | İşe Çalışan Ekleme")
window.geometry("500x500")
window.configure(background="#EBF3E8")

sequiapp = os.getcwd()
workFilesName = tk.Label(text="Klasördeki iş dosyaları;", fg="#86A789", font="Arial 16 bold")
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

# iş adı alınıyor
jobName=tk.Label(text="\nHangi iş için çalışan veya takım eklemek istiyorsunuz?", font="Arial 12")
jobName.pack()
# Entry ile input alındı, width ile alan ölçüsü belirlendi
teamNameInput=tk.Entry(width=35, font=12)
teamNameInput.pack()

jobName=tk.Label(text="\n Eklenecek çalışan veya takımın adını yazınız", font="Arial 12")
jobName.pack()
teamInput = tk.Entry(width=35, font=12)
teamInput.pack()

# ekip-çalışan ekleme fonksiyonu tanımlandı
def teamVerifired():
    # teamNameInput string'e dönüştürüldü ve name değişkenine atandı
    name=str(teamNameInput.get())
    space = tk.Label(text = "\n")
    space.pack()
    # teamInput'tan gelen veri string'e dönüştürüldü ve teamDetails değişkenine atandı
    teamDetails = str(teamInput.get())
    # kullanıcıdan gelen dosya ismi ile ilgili dosya açıldı
    jobFile=open(name + ".txt", "a")
    # teamDetails'tan gelen veri açılan dosyaya yazdırıldı
    # karışıklık olmaması için \n ile her bir aşağı satıra geçildi
    # iş oluşturulma tarihleri yazıldı
    CreateDate = datetime.datetime.ctime(date)
    # dosya adı ve ne zaman oluşturulduğu oluşturulan text dosyasına yazıldı
    jobFile.write("\n" + CreateDate + " tarihinde " + teamDetails + " takimi / kisisi eklendi")

    recordSuccess = tk.Label(text="Kayıt başarılı, çalışan eklendi!")
    recordSuccess.pack()

space = tk.Label(text = "\n")
space.pack()

# iş adı onaylama ve işlem doğrulama butonu tanımlandı
# aksiyon olarak teamVerifired fonksiyonu verildi
teamVerifiredButton=tk.Button(text=   "Onayla",
                                bg=      "#B2C8BA",
                                fg=      "black",
                                font=    "Arial 11",
                                width=   25,
                                command= teamVerifired)
teamVerifiredButton.pack()

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