import tkinter as tk
import datetime
import os

# oluşturulan dosyalarda zaman damgası kullanabilmek için date değişkeni oluşturuldu
date = datetime.datetime.now()

window=tk.Tk()
window.title("Sequi App | İş-Görev Oluşturma")
window.geometry("500x500")
window.configure(background="#EBF3E8")

sequiapp = os.getcwd()
workFilesName = tk.Label(text="Klasördeki iş dosyaları", fg="#86A789", font="Arial 16 bold")
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
jobName=tk.Label(text="\nHangi dosya için iş oluşturmak istiyorsunuz?", font="Arial 12")
jobName.pack()
# Entry ile input alındı, width ile alan ölçüsü belirlendi
jobNameInput=tk.Entry(width=35, font=12)
jobNameInput.pack()

jobName=tk.Label(text="\n Oluşturulacak iş için görev detaylarını yazınız", font="Arial 12")
jobName.pack()
jobInput = tk.Entry(width=35, font=12)
jobInput.pack()

# iş onaylama ve işlem doğrulama fonksiyonu tanımlandı
def jobNameVerifired():
    # jobNameInput string'e dönüştürüldü ve name değişkenine atandı
    name=str(jobNameInput.get())
    space = tk.Label(text = "\n")
    space.pack()
    # jobInput'tan gelen veri string'e dönüştürüldü ve jobDetails değişkenine atandı
    jobDetails = str(jobInput.get())
    # kullanıcıdan gelen dosya ismi ile ilgili dosya açıldı
    jobFile=open(name + ".txt", "a")
    # jobDetails'tan gelen veri açılan dosyaya yazdırıldı
    # karışıklık olmaması için \n ile her bir aşağı satıra geçildi
    # iş oluşturulma tarihleri yazıldı
    CreateDate = datetime.datetime.ctime(date)
    # dosya adı ve ne zaman oluşturulduğu oluşturulan text dosyasına yazıldı
    jobFile.write("\n" + CreateDate + " tarihinde " + jobDetails + " isi olusturuldu.")

    recordSuccess = tk.Label(text="Kayıt başarılı!")
    recordSuccess.pack()

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