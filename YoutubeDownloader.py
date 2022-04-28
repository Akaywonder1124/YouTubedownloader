from distutils.log import ERROR
from urllib.error import URLError
from tkinter import *
import youtube_dl


#layout and title
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Downloader")
root.configure(bg="black")


#label
Label(root, text = "A SIMPLE YOUTUBE DOWNLOADER ", font= "roboto 10 bold",
     fg= "orange", bg= "black", pady= 12, bd =1 ).pack()
link = StringVar()


Label(root, text = "PASTE THE URL OF THE YOUTUBE VIDEO ", font= "roboto 10",
     fg= "orange", bg= "black", pady= 12, bd =1 ).pack()

#Download image
photo = PhotoImage(file= r"C:\Users\USER\Downloads\downloadbt.png") 


#Input Field
link_enter = Entry(root, width= "70",  textvariable= link ).place(x = 30, y=85)



def download():
     try:
          url = {'outtmpl': 'C:/Users/USER/Downloads/%(extractor_key)s/%(extractor)s-%(id)s-%(title)s.%(ext)s'}
          with youtube_dl.YoutubeDL(url) as video:
               video.download([str(link.get())])
          # Display a successful message
     except (URLError, youtube_dl.utils.DownloadError):
            Label(root, text = "Internet Connection Error", font= "roboto 15 bold",fg= "red",
                bg= "black", pady= 12, padx= 30, bd =1 ).place(y=200, x = 80)

     else:
   
          Label(root, text = "Successfully Downloaded", font= "roboto 18 bold",fg= "green",
                bg= "black", pady= 12, bd =1 ).place(y=200, x = 80)
     


   
     

#Download Button
Download = Button(root, text= "Download", image= photo, bg="black", bd=0, 
                    cursor="arrow black", command= download ).place(y = 130, x = 100)
#Author
Autor = Label(root, text = "Proudly Developed by Akay ", font= "roboto 10",fg= "orange",
                bg= "black", pady= 12, bd =2 ).place(y=250, x = 320)

root.mainloop()

