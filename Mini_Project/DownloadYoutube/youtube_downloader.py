# Importing necessary packages
from tkinter import *
from pytube import YouTube
  
root = Tk()
root.geometry('600x400')
root.resizable(0,0)
root.title("Thanh's video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()
ouput = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 50, y = 90)
Label(root, text = 'Ouput Path Here:', font = 'arial 15 bold').place(x= 160 , y = 120)
output_path = Entry(root, width = 70,textvariable = ouput).place(x = 50, y = 160)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download(str(ouput.get()))
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 220)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 210)

root.mainloop()