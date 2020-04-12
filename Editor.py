import tkinter as tk
import tkinter.messagebox
import hashlib
import pyperclip
import tkinter.filedialog
import tkinter.font as tkfont

fileName = "Untitled"
saved = False
previousText = ""
currentText = ""
beforeEditText = ""
afterEditText = ""


def checkSave(event):
    global previousText
    global currentText
    global fileName
    global saved
    global afterEditText
    global beforeEditText
    beforeEditText = currentText
    afterEditText = textBox.get("1.0", "end-1c")
    print(f"before edit text\"{beforeEditText}\" after edit text \"{afterEditText}\"")
    if not saved and afterEditText != beforeEditText or saved and afterEditText != beforeEditText:
        wn.title("*"+fileName + " - Text Editor")  # rename window according to file name


def saveFile():
    global fileName
    global previousText
    global saved
    f = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = textBox.get("1.0", "end-1c")
    '''
    The first part, "1.0" means that the input should be read from line one, 
    character zero (ie: the very first character).
     END is an imported constant which is set to the string "end". 
     The END part means to read until the end of the text box is reached. 
     The only issue with this is that it actually adds a newline to our input. 
     So, in order to fix it we should change END to end-1c .
     The -1c deletes 1 character, while -2c would mean delete two characters, and so on.
    '''
    f.write(text2save)
    previousText = textBox.get("1.0", "end-1c")
    reverseFileName = ''.join(reversed(f.name))
    fileName = ""
    start = False
    for i in reverseFileName:
        if i == ".":
            start = True
        elif i == "/":
            break
        elif start == True:
            fileName += i
    fileName = ''.join(reversed(fileName))
    wn.title(fileName + " - Text Editor")  # rename window according to file name
    saved = True
    f.close()


def openFile():
    global currentText
    global previousText
    global fileName
    currentText=textBox.get("1.0", "end-1c")
    if currentText == previousText:
        File1 = tk.filedialog.askopenfilename()
        File2 = open(File1, "r")
        textBox.delete("1.0", "end")  # clearing TextBox
        textBox.insert("1.0", File2.read())
        reverseFileName = ''.join(reversed(File2.name))
        fileName = ""
        start = False
        for i in reverseFileName:
            if i == ".":
                start = True
            elif i == "/":
                break
            elif start == True:
                fileName += i
        fileName = ''.join(reversed(fileName))
        wn.title(fileName + " - Text Editor")  # rename window according to file name
        File2.close()  # Make sure you close the file when done
        currentText = textBox.get("1.0", "end-1c")
        print(f"current text {currentText}")
    else:
        decision = tk.messagebox.askyesnocancel(title="Text Editor", message="Do you want to save file?")
        if decision == False:
            File1 = tk.filedialog.askopenfilename()
            File2 = open(File1, "r")
            textBox.delete("1.0", "end")  # clearing TextBox
            textBox.insert("1.0", File2.read())
            reverseFileName = ''.join(reversed(File2.name))
            fileName = ""
            start = False
            for i in reverseFileName:
                if i == ".":
                    start = True
                elif i == "/":
                    break
                elif start == True:
                    fileName += i
            fileName = ''.join(reversed(fileName))
            wn.title(fileName + " - Text Editor")  # rename window according to file name
            File2.close()  # Make sure you close the file when done
        elif decision == True:
            saveFile()
        elif decision == "cancel":
            pass


def exit():
    wn.destroy()


def countVowels():
    input = textBox.get("1.0", "end-1c")
    input = input.lower()  # converting full string to lowercase
    vowels = 0
    for letter in input:
        if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
            vowels += 1
    tk.messagebox.showinfo(title="Vowels", message=f"There are {vowels} vowels in this text")


def countConsonants():
    input = textBox.get("1.0", "end-1c")
    input = input.lower()
    consonants = 0
    for letter in input:
        if (letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u'):
            if letter.isalpha():
                consonants += 1
    tk.messagebox.showinfo(title="Consonants", message=f"There are {consonants} consonants in this text")


def countSpecialCharacters():
    input = textBox.get("1.0", "end-1c")
    specialCharacters = 0
    for letter in input:
        if letter.isalpha() == False and letter.isdigit() == False and letter.isspace() == False:
            specialCharacters += 1
    tk.messagebox.showinfo(title="Special Characters",
                           message=f"There are {specialCharacters} special characters in this text")


def countSpecificCharacter():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("200x200")

    inputLabel = tk.Label(inputWindow, text="Enter Character")
    inputLabel.grid(row=0, column=0, padx=50, pady=10)

    inputBox = tk.Entry(inputWindow, width=10)
    inputBox.grid(row=1, column=0, padx=50, pady=10)

    def getChar():
        charcter = inputBox.get()
        specificCharacter = 0
        for letter in input:
            if (letter == charcter):
                specificCharacter += 1
        tk.messagebox.showinfo(title="Specific Character",
                               message=f"\'{charcter}\' appeared {specificCharacter} times in this text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Submit", command=getChar)
    submitButton.grid(row=2, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def countSpecificWord():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("200x180")

    inputLabel = tk.Label(inputWindow, text="Enter Word")
    inputLabel.grid(row=0, column=0, padx=30, pady=10)

    inputBox = tk.Entry(inputWindow, width=20)
    inputBox.grid(row=1, column=0, padx=30, pady=10)

    def getWord():
        word = inputBox.get()
        specificWord = 0

        index = 0

        for letter in input:
            if letter == word[index]:
                index += 1
                if index == len(word):
                    specificWord += 1
                    index = 0
            else:
                index = 0

        tk.messagebox.showinfo(title="Specific Word",
                               message=f"\"{word}\" appeared {specificWord} times in this text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Submit", command=getWord)
    submitButton.grid(row=2, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def countSpecificSentence():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("200x200")

    inputLabel = tk.Label(inputWindow, text="Enter Sentence")
    inputLabel.grid(row=0, column=0, padx=50, pady=10)

    inputBox = tk.Text(inputWindow, height=5, width=20)
    inputBox.grid(row=1, column=0, padx=20, pady=10)

    def getSentence():
        sentence = inputBox.get("1.0", "end")
        specificSentence = 0

        index = 0

        for i in range(len(input)):
            if input[i] == sentence[index]:
                index += 1
                if index == len(sentence) - 1:
                    specificSentence += 1
                    index = 0
            else:
                index = 0

        tk.messagebox.showinfo(title="Specific Sentence",
                               message=f"\"{sentence}\" appeared {specificSentence} times in this text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Submit", command=getSentence)
    submitButton.grid(row=2, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def replaceWord():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("250x250")

    inputLabel1 = tk.Label(inputWindow, text="Enter the Word you want to replace")
    inputLabel1.grid(row=0, column=0, padx=20, pady=10)

    inputBox1 = tk.Entry(inputWindow, width=20)
    inputBox1.grid(row=1, column=0, padx=30, pady=10)

    inputLabel2 = tk.Label(inputWindow, text="Enter Word to replace")
    inputLabel2.grid(row=2, column=0, padx=30, pady=10)

    inputBox2 = tk.Entry(inputWindow, width=20)
    inputBox2.grid(row=3, column=0, padx=30, pady=10)

    def getWord():
        word1 = inputBox1.get()
        replaceword = inputBox2.get()

        specificWord = 0

        editedString = input.replace(word1, replaceword)

        index = 0

        for letter in input:
            if letter == word1[index]:
                index += 1
                if index == len(word1):
                    specificWord += 1
                    index = 0
            else:
                index = 0

        textBox.delete("1.0", "end")  # clearing TextBox
        textBox.insert("1.0", editedString)
        if specificWord > 0:
            tk.messagebox.showinfo(title="Word Replacement",
                                   message=f"\"{word1}\" replaced with {replaceword} in {specificWord} places")
        else:
            tk.messagebox.showwarning(message=f"{word1} doesn't exist in the text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Replace", command=getWord)
    submitButton.grid(row=4, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def removeWord():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("250x180")

    inputLabel1 = tk.Label(inputWindow, text="Enter the Word you want to remove")
    inputLabel1.grid(row=0, column=0, padx=20, pady=10)

    inputBox1 = tk.Entry(inputWindow, width=20)
    inputBox1.grid(row=1, column=0, padx=50, pady=10)

    def getWord():
        word1 = inputBox1.get()
        replaceword = ""

        specificWord = 0

        editedString = input.replace(word1, replaceword)

        index = 0

        for letter in input:
            if letter == word1[index]:
                index += 1
                if index == len(word1):
                    specificWord += 1
                    index = 0
            else:
                index = 0

        textBox.delete("1.0", "end")  # clearing TextBox
        textBox.insert("1.0", editedString)
        if specificWord > 0:
            tk.messagebox.showinfo(title="Word Removal", message=f"\"{word1}\" removed in {specificWord} places")
        else:
            tk.messagebox.showwarning(message=f"\"{word1}\" doesn't exist in the text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Remove", command=getWord)
    submitButton.grid(row=4, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def removeSentence():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("250x180")

    inputLabel1 = tk.Label(inputWindow, text="Enter the Sentence you want to remove")
    inputLabel1.grid(row=0, column=0, padx=20, pady=10)

    inputBox1 = tk.Entry(inputWindow, width=20)
    inputBox1.grid(row=1, column=0, padx=50, pady=10)

    def getSentence():
        sentence1 = inputBox1.get()
        replaceSentence = ""

        specificSentence = 0

        editedString = input.replace(sentence1, replaceSentence)

        index = 0

        for letter in input:
            if letter == sentence1[index]:
                index += 1
                if index == len(sentence1):
                    specificSentence += 1
                    index = 0
            else:
                index = 0

        textBox.delete("1.0", "end")  # clearing TextBox
        textBox.insert("1.0", editedString)
        if specificSentence > 0:
            tk.messagebox.showinfo(title="Sentence Removal",
                                   message=f"\"{sentence1}\" removed in {specificSentence} places")
        else:
            tk.messagebox.showwarning(message=f"\"{sentence1}\" doesn't exist in the text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Remove", command=getSentence)
    submitButton.grid(row=4, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def replaceSentence():
    input = textBox.get("1.0", "end-1c")

    # to take small inputs for search or stuff
    inputWindow = tk.Tk()
    inputWindow.geometry("250x250")

    inputLabel1 = tk.Label(inputWindow, text="Enter the Sentence you want to replace")
    inputLabel1.grid(row=0, column=0, padx=20, pady=10)

    inputBox1 = tk.Entry(inputWindow, width=20)
    inputBox1.grid(row=1, column=0, padx=30, pady=10)

    inputLabel2 = tk.Label(inputWindow, text="Enter Sentence to replace")
    inputLabel2.grid(row=2, column=0, padx=30, pady=10)

    inputBox2 = tk.Entry(inputWindow, width=20)
    inputBox2.grid(row=3, column=0, padx=30, pady=10)

    def getSentence():
        sentence1 = inputBox1.get()
        replaceSentence = inputBox2.get()

        specificSentence = 0

        editedString = input.replace(sentence1, replaceSentence)

        index = 0

        for letter in input:
            if letter == sentence1[index]:
                index += 1
                if index == len(sentence1):
                    specificSentence += 1
                    index = 0
            else:
                index = 0

        textBox.delete("1.0", "end")  # clearing TextBox
        textBox.insert("1.0", editedString)
        if specificSentence > 0:
            tk.messagebox.showinfo(title="Sentence Replacement",
                                   message=f"\"{sentence1}\" replaced with {replaceSentence} in {specificSentence} places")
        else:
            tk.messagebox.showwarning(message=f"\"{sentence1}\" doesn't exist in the text")
        inputWindow.destroy()  # close window after extracting input

    submitButton = tk.Button(inputWindow, text="Replace", command=getSentence)
    submitButton.grid(row=4, column=0, padx=50, pady=10)

    inputWindow.mainloop()


def sha256():
    input = textBox.get("1.0", "end-1c")
    # To print hashed code
    inputWindow = tk.Tk()
    inputWindow.title("SHA256 Hash Code")
    inputWindow.geometry("300x180")

    outputBox = tk.Text(inputWindow, width=30, height=5, padx=10, pady=10)
    outputBox.grid(row=0, column=0, padx=20, pady=10)

    code = hashlib.sha256(input.encode())  # we need .encode to make input readable for hash functions

    outputBox.insert("1.0", code.hexdigest())

    def copyText():
        pyperclip.copy(code.hexdigest())  # we nedd .hexdigest to see the encrypted code
        copiedText = pyperclip.paste()
        inputWindow.destroy()

    copyButton = tk.Button(inputWindow, text="Copy", command=copyText)
    copyButton.grid(row=1, column=0)

    inputWindow.mainloop()


def sha384():
    input = textBox.get("1.0", "end-1c")
    # To print hashed code
    inputWindow = tk.Tk()
    inputWindow.title("SHA384 Hash Code")
    inputWindow.geometry("300x180")

    outputBox = tk.Text(inputWindow, width=30, height=5, padx=10, pady=10)
    outputBox.grid(row=0, column=0, padx=20, pady=10)

    code = hashlib.sha384(input.encode())  # we need .encode to make input readable for hash functions

    outputBox.insert("1.0", code.hexdigest())  # we nedd .hexdigest to see the encrypted code

    def copyText():
        pyperclip.copy(code.hexdigest())
        copiedText = pyperclip.paste()
        inputWindow.destroy()

    copyButton = tk.Button(inputWindow, text="Copy", command=copyText)
    copyButton.grid(row=1, column=0)

    inputWindow.mainloop()


def sha224():
    input = textBox.get("1.0", "end-1c")
    # To print hashed code
    inputWindow = tk.Tk()
    inputWindow.title("SHA224 Hash Code")
    inputWindow.geometry("300x180")

    outputBox = tk.Text(inputWindow, width=30, height=5, padx=10, pady=10)
    outputBox.grid(row=0, column=0, padx=20, pady=10)

    code = hashlib.sha224(input.encode())  # we need .encode to make input readable for hash functions

    outputBox.insert("1.0", code.hexdigest())  # we nedd .hexdigest to see the encrypted code

    def copyText():
        pyperclip.copy(code.hexdigest())
        copiedText = pyperclip.paste()
        inputWindow.destroy()

    copyButton = tk.Button(inputWindow, text="Copy", command=copyText)
    copyButton.grid(row=1, column=0)

    inputWindow.mainloop()


def sha512():
    input = textBox.get("1.0", "end-1c")
    # To print hashed code
    inputWindow = tk.Tk()
    inputWindow.title("SHA512 Hash Code")
    inputWindow.geometry("300x180")

    outputBox = tk.Text(inputWindow, width=30, height=5, padx=10, pady=10)
    outputBox.grid(row=0, column=0, padx=20, pady=10)

    code = hashlib.sha512(input.encode())  # we need .encode to make input readable for hash functions

    outputBox.insert("1.0", code.hexdigest())  # we nedd .hexdigest to see the encrypted code

    def copyText():
        pyperclip.copy(code.hexdigest())
        copiedText = pyperclip.paste()
        inputWindow.destroy()

    copyButton = tk.Button(inputWindow, text="Copy", command=copyText)
    copyButton.grid(row=1, column=0)

    inputWindow.mainloop()


def sha1():
    input = textBox.get("1.0", "end-1c")
    # To print hashed code
    inputWindow = tk.Tk()
    inputWindow.title("SHA1 Hash Code")
    inputWindow.geometry("300x180")

    outputBox = tk.Text(inputWindow, width=30, height=5, padx=10, pady=10)
    outputBox.grid(row=0, column=0, padx=20, pady=10)

    code = hashlib.sha1(input.encode())  # we need .encode to make input readable for hash functions

    outputBox.insert("1.0", code.hexdigest())  # we nedd .hexdigest to see the encrypted code

    def copyText():
        pyperclip.copy(code.hexdigest())
        copiedText = pyperclip.paste()
        inputWindow.destroy()

    copyButton = tk.Button(inputWindow, text="Copy", command=copyText)
    copyButton.grid(row=1, column=0)

    inputWindow.mainloop()


def md5():
    input = textBox.get("1.0", "end-1c")
    # To print hashed code
    inputWindow = tk.Tk()
    inputWindow.title("MD5 Hash Code")
    inputWindow.geometry("300x180")

    outputBox = tk.Text(inputWindow, width=30, height=5, padx=10, pady=10)
    outputBox.grid(row=0, column=0, padx=20, pady=10)

    code = hashlib.md5(input.encode())  # we need .encode to make input readable for hash functions

    outputBox.insert("1.0", code.hexdigest())  # we nedd .hexdigest to see the encrypted code

    def copyText():
        pyperclip.copy(code.hexdigest())
        copiedText = pyperclip.paste()
        inputWindow.destroy()

    copyButton = tk.Button(inputWindow, text="Copy", command=copyText)
    copyButton.grid(row=1, column=0)

    inputWindow.mainloop()


def lightMode():
    textBox.config(bg="white", fg="black")
    textBox.config(insertbackground="black")


def darkMode():
    textBox.config(bg="black", fg="white")
    textBox.config(insertbackground="white")


def draculaMode():
    textBox.config(bg="#676D6D", fg="#05DA12")
    textBox.config(insertbackground="#05DA12")


def materialMode():
    textBox.config(bg="#575962", fg="#ec6d10")
    textBox.config(insertbackground="#ec6d10")


def agilaMode():
    textBox.config(bg="#352F4B", fg="#20C812")
    textBox.config(insertbackground="#20C812")


def brogrammerMode():
    textBox.config(bg="#1F1E26", fg="#1587CC")
    textBox.config(insertbackground="#1587CC")


def darkmatterMode():
    textBox.config(bg="#202832", fg="#04DAC9")
    textBox.config(insertbackground="#04DAC9")


def matrixMode():
    textBox.config(bg="black", fg="#05DA12")
    textBox.config(insertbackground="#05DA12")


# window
wn = tk.Tk()
wn.title(fileName + "-Text Editor")
wn.geometry("500x500")
wn.bind("<KeyRelease>", checkSave)

menu = tk.Menu(wn)
wn.config(menu=menu)

fileMenu = tk.Menu(menu, tearoff=False)
viewMenu = tk.Menu(menu, tearoff=False)
editMenu = tk.Menu(menu, tearoff=False)
hashMenu = tk.Menu(menu, tearoff=False)
themesMenu = tk.Menu(menu, tearoff=False)

# dding count menu to main menu

menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="View", menu=viewMenu)
menu.add_cascade(label="Edit", menu=editMenu)  # adding editmenu to main menu
menu.add_cascade(label="Hash", menu=hashMenu)
menu.add_cascade(label="Themes", menu=themesMenu)

fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="Exit", command=exit)

viewMenu.add_command(label="Vowels", command=countVowels)
viewMenu.add_command(label="Consonants", command=countConsonants)
viewMenu.add_command(label="Special Character", command=countSpecialCharacters)
viewMenu.add_command(label="Specific Character", command=countSpecificCharacter)
viewMenu.add_command(label="Specific word", command=countSpecificWord)
viewMenu.add_command(label="Specific Sentence", command=countSpecificSentence)

editMenu.add_command(label="Replace Word", command=replaceWord)
editMenu.add_command(label="Remove Word", command=removeWord)
editMenu.add_command(label="Replace Sentence", command=replaceSentence)
editMenu.add_command(label="Remove Sentence", command=removeSentence)

hashMenu.add_command(label="SHA256", command=sha256)
hashMenu.add_command(label="SHA384", command=sha384)
hashMenu.add_command(label="SHA224", command=sha224)
hashMenu.add_command(label="SHA512", command=sha512)
hashMenu.add_command(label="SHA1", command=sha1)
hashMenu.add_command(label="MD5", command=md5)

themesMenu.add_command(label="Light", command=lightMode)
themesMenu.add_command(label="Dark", command=darkMode)
themesMenu.add_command(label="Dracula", command=draculaMode)
themesMenu.add_command(label="Material", command=materialMode)
themesMenu.add_command(label="Agila", command=agilaMode)
themesMenu.add_command(label="Brogrammer", command=brogrammerMode)
themesMenu.add_command(label="Darkmatter", command=darkmatterMode)
themesMenu.add_command(label="Matrix", command=matrixMode)

textBox = tk.Text(wn, width=450, height=450, padx=5, pady=5)
textBox.pack()

# runs window
wn.mainloop()
