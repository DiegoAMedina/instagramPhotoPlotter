from Tkinter import *
import tkMessageBox
import webbrowser, os.path

class App(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Instagram ID")
        self.root.geometry('400x400')
        self.label = Label (self.root, text= "Please Enter Your Instagram Dispaly Name")
        self.label.pack()


        self.entrytext = StringVar()
        Entry(self.root, textvariable=self.entrytext).pack()

        self.buttontext = StringVar()
        self.buttontext.set("Enter")
        Button(self.root, textvariable=self.buttontext, command=self.clicked1).pack()

        self.root.mainloop()
      

    def clicked1(self):
        input = self.entrytext.get()
        #print input
        userId= "https://api.instagram.com/v1/users/search?q=" + input + "&access_token= 186357295.1677ed0.6ce9f99b45fc4ecfb460fd12acc0653f"
        webbrowser.open(userId)

    def button_click(self, e):
        pass

App()

"""
def __init__(self, master):
        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM)

        self.quitButton = Button(bottomFrame, text="Quit", command=self.close_window)
        self.quitButton.pack(side=BOTTOM)


        self.highQualityButton = Button(bottomFrame, text="Search", command= self.Search)
        self.highQualityButton.pack(side=BOTTOM)

        imageTitle = Image.open("C:\Users\Thalia\Desktop\instagramPhotoPlotter-DiegoAMedina-patch-1\instagramPhotoPlotter-DiegoAMedina-patch-1\TitleImage.jpg")
        photo = ImageTk.PhotoImage(imageTitle)
        self.Title = Label(image=photo)
        self.Title.image = photo
        self.Title.pack()
"""
