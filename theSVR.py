from tkinter import *
from model_tomp3_mp4 import star
import threading 
app=Tk()
status=StringVar()
def inicio():
    status.set("Baixando...")
    mp3Status=star(playlistUrl.get(), downloadPath.get(),valor_radio.get())
    status.set(mp3Status)
####teoricamente era pra alterar o status para exibir uma mensagem

valor_radio=StringVar()
playlistUrl=StringVar()
downloadPath=StringVar()

status.set("Status : ")
app.title("The VibeSVR")
width = app.winfo_screenwidth()
height = app.winfo_screenheight()
app.resizable(width=False, height=False)
app.geometry('%dx%d+%d+%d' % (950, 620 , width*0.2, height*0.1))

l_titulo=Label(app, text="The Vibe SVR", font=("Century Gothic", 20), fg="black")
l_titulo.place(x=360, y=100)
l_downloadPath=Label(app, text="Download Path", font=("Century Gothic", 13), fg="black")
l_downloadPath.place(x=150, y=160)
e_downloadPath=Entry(app,width=60,foreground="blue",font=("verdana",12),textvariable=downloadPath)
e_downloadPath.place(x=200, y=200)
b_pasteDownloadPath=Button(app, text="Paste Path", font=("Century Gothic", 10), bg="MIDNIGHTBLUE", fg="white",command=lambda:downloadPath.set(app.clipboard_get()))
b_pasteDownloadPath.place(x=800, y=200)
l_youtubeUrl=Label(app, text="Youtube URL", font=("Century Gothic", 13), fg="black")
l_youtubeUrl.place(x=150, y=240)
e_youtubeUrl=Entry(app,width=60,foreground="blue",font=("verdana",12),textvariable=playlistUrl)
e_youtubeUrl.place(x=200, y=280)
b_pasteYoutubeUrl=Button(app, text="Paste URL", font=("Century Gothic", 10), bg="MIDNIGHTBLUE", fg="white",command=lambda:playlistUrl.set(app.clipboard_get()))
b_pasteYoutubeUrl.place(x=800, y=280)
l_statusLabel=Label(app, font=("Century Gothic", 10), fg="black",bg="grey",textvariable=status,width=118,height=3)
l_statusLabel.place(x=0,y=320)
b_download = Button(app, text="Download", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white",command=lambda:threading.Thread(target=inicio,daemon=True).start())
b_download.place(x=400, y=500)
l_radio = Label(app, text='Qual o Formato?')
r_mp3= Radiobutton(app, text='mp3',
       variable = valor_radio, value="mp3")
r_mp3.select()
r_mp4 = Radiobutton(app, text='mp4',
       variable = valor_radio, value="mp4")
l_radio.place(x=400,y=420)
r_mp3.place(x=500,y=420)
r_mp4.place(x=550,y=420)
app.mainloop()
