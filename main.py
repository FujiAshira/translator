# Try import function #Debugging

def TryImport(Library,FullLibraryName="", ImportAs=""):
    if FullLibraryName == "":
        FullLibraryName = Library
    if ImportAs == "":
        ImportAs = Library
    try:
        exec(f"import {Library} as {ImportAs}")
    except:
        import os, time
        try:
            exec(f"os.system(\"py -m pip install -U {FullLibraryName} --user\")")
            print(f"Importing {Library} ({FullLibraryName}) as {ImportAs}")
        except:
            raise ImportError(f"{Library} ({FullLibraryName}) installation failed")
        time.sleep(15)
    finally:
        exec(f"global {Library}")
        print(f"Import {Library} finished")
        return f"import {Library} as {ImportAs}"
# importing
import tkinter as tk
import tkinter.messagebox
import cgitb as cgb
import time
exec(TryImport(Library="googletrans",FullLibraryName="googletrans==4.0.0-rc1"))
# import googletrans
import threading as thread

# Client size
client = tk.Tk()
client.geometry('530x350')
client.maxsize(530,350)
client.minsize(530,350)

# Font
Arial_Bold = tk.Label(text="English - Thai",font=('Arial',25,'bold'))
Arial_Bold.pack()

# Change Language Scroll bar
LangList = googletrans.LANGUAGES.values()
SourceLangGet = tk.StringVar()
SourceLangGet.set("english")
SourceLang = tk.OptionMenu(client,SourceLangGet,*LangList)
SourceLang.place(x=10,y=70)
SourceWord = tk.Text(client,width=30,height=10)
SourceWord.place(x=10,y=100)

DestinationLangGet = tk.StringVar()
DestinationLangGet.set("thai")
DestinationLang = tk.OptionMenu(client,DestinationLangGet,*LangList)
DestinationLang.place(x=275,y=70)
DestinationWord = tk.Text(client,width=30,height=10)
DestinationWord.place(x=275,y=100)

# translate function
def Source_To_Destination():
    try:
        Word = str(SourceWord.get(1.0,"end-1c"))
        Translator = googletrans.Translator()
        TranslateWord = Translator.translate(text=Word,src=f"{SourceLangGet.get()}",dest=f"{DestinationLangGet.get()}").text
        DestinationWord.delete(1.0,"end-1c")
        DestinationWord.insert(1.0,TranslateWord)

        UpdateLang()
    except:
        pass

# Update language
def UpdateLang():

    client.title(f"Translator {SourceLangGet.get()} to {DestinationLangGet.get()}")

    TranslateS_D.config(text=f"Translate {SourceLangGet.get()} to {DestinationLangGet.get()}")

    Arial_Bold.config(text=f"{SourceLangGet.get()} - {DestinationLangGet.get()}")

# Switching language
def SwitchLang():
    # Language get
    SourceLangUsing = SourceLangGet.get()
    DestinationLangUsing = DestinationLangGet.get()

    # Swap language
    SourceLangGet.set(DestinationLangUsing)
    DestinationLangGet.set(SourceLangUsing)

    # Word get
    SourceLangWord = SourceWord.get(1.0,"end-1c")
    DestinationLangWord = DestinationWord.get(1.0,"end-1c")

    # Delete word
    SourceWord.delete(1.0,"end-1c")
    DestinationWord.delete(1.0,"end-1c")

    # Swap word
    SourceWord.insert(1.0,DestinationLangWord)
    DestinationWord.insert(1.0,SourceLangWord)

    # Update language
    UpdateLang()

# close window
def Closing():
    if tk.messagebox.askyesno("Quit","Do you want to quit?"):
        client.destroy()
        exit(0)

if __name__ == '__main__':
    SwitchButton = tk.Button(client,text="<--->",command=SwitchLang)
    SwitchButton.place(x=245,y=170)
    TranslateS_D = tk.Button(client,text=f"Translate {SourceLangGet.get()} to {DestinationLangGet.get()}",command=Source_To_Destination)
    TranslateS_D.place(x=200,y=300)
    UpdateLang()
    client.protocol("WM_DELETE_WINDOW", Closing)
    client.mainloop()
