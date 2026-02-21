import customtkinter
from rembg import remove
from PIL import Image 
from tkinter import filedialog
from tkinter import Tk
import os

# I added comments to input what I learned 

def openFile():
    #this pops an file dialog(lets u select files), filetype limits what filetype user can select
    fileLoc = filedialog.askopenfilename(title= "Please input image", filetypes=[("Image Files", "*.jpeg *.jpg *.webp *.png")] )

    # if file loc is found(IS NOT SIMILAR TO x == true)
    if fileLoc:

        # this line is ackshually crazy, filedir, origImage gets splits based on position. Filedir get directory, while image gets title with extension
        fileDir, origImage = os.path.split(fileLoc)

        # Slits imageTitle and extension = img.png -> img
        nameOnly = os.path.splitext(origImage)[0]

        newFileName = f"{nameOnly}_bgRemoved.png"

        # join filedir and new filename into a single line in a variable using / = this/img,png
        finalPath  = os.path.join(fileDir, newFileName) 

        inputImage = Image.open(fileLoc)
        cleanedImage = remove(inputImage)

        cleanedImage.save(finalPath) 

        # userImage = customtkinter.CTkImage(light_image=userImage, 
        #                         dark_image=userImage,
        #                         size=(300, 300))

        print(f"Background removed and saved to {finalPath}")
    else:
        print("No file selected.")

app = customtkinter.CTk()
app.geometry("400x400")
app.title("Background remover")


# button = customtkinter.CTkButton(app, text="Remove Background", command=processImage)
button = customtkinter.CTkButton(app, text="Remove Background", command=openFile)
button.pack(padx = 20, pady = 20)
button.place(relx=0.5, rely=0.5, anchor="center")


app.mainloop()
