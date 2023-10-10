import tkinter as tk
from tkinter import ttk
import pandas as pd

file_path = "/Users/omer.chandna/Documents/projects/encryption/decodekey.csv" 
encryption_key = pd.read_csv(file_path, sep=',' , names=['Character' , 'Byte'], header=None, skiprows=[0]) # setting up pandas to read the ecnryption csv file

dframe = pd.DataFrame(data=encryption_key) # creating the data frame for pandas
dframe['Character'] = dframe['Character'].astype(str)
dframe['Byte'] = dframe['Byte'].astype(str)


def split_by_char(message):
    return [char for char in message] 



def encrypt_message(to_encript):
    to_encript = split_by_char(to_encript)
    
    encrypted_ = ""
    temp_char = ""

    for i in range(len(to_encript)):
        x = to_encript[i]

        try:
            temp_char = encryption_key.loc[encryption_key['Character'] == x, 'Byte'].iloc[0]

        except:
            print(to_encript[x] + "not found in key")
            temp_char = "---"

        encrypted_ += temp_char

    return encrypted_


def decrypt_message(encrypted_):
    decoded_message = []
    decoded_ = ""

    for i in range(0, len(encrypted_), 2):
        x = encrypted_[i:i+2]
        index_ = dframe[dframe.eq(x).any(1)] #

        dframe2 = index_['Character'].tolist() # searching the pandas data frame for the alphanumeric code that matches with the character

        temp_string = [str(j) for j in dframe2]

        decoded_message += temp_string

    decoded_ = "".join(decoded_message)

    return decoded_

class encryptionApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = "true")

        container.configure(bg = "black")
        container.columnconfigure(0, weight = 1)
        container.rowconfigure(0, weight = 1)

        self.frames = {} # initialized a dictionary to store all the different frames in the program

        for x in (Main_page, encode_page, decode_page):
            frame = x(container, self)

            self.frames[x] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(Main_page)

    def show_frame(self, con):
        frame = self.frames[con]
        frame.tkraise()


class Main_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "black")

        label_main = tk.Label(self, text = "Main", fg= "green", bg = "black", highlightbackground = "green", highlightcolor = "green", highlightthickness = 1)
        label_main.grid(row = 0, column = 5, padx = 10, pady = 10)

        info_main = tk.Label(
            self,
            text = "This application will encrypt and decrypt a given message" + "\nusing a propreitary encryption key",
            fg= "green",
            bg= "black"
            
            )

        info_main.grid(row = 1, column = 5, padx = 10, pady= 15)


        encode_button = tk.Button(
            self,
            text = "Encode",
            bg="black",
            fg= "green",
            highlightbackground = "black", 
            highlightcolor = "black",
            highlightthickness = 1,
            activebackground="black",
            command = lambda : controller.show_frame(encode_page)
        )

        

        encode_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        decode_button = tk.Button(
            self,
            text = "Decode",
            bg="black",
            fg= "green",
            highlightbackground = "black", 
            highlightcolor = "black",
            highlightthickness = 1,
            activebackground= "black",
            command = lambda: controller.show_frame(decode_page)
        )
        
#---------------------------------------END MAIN PAGE-------------------------------------------------

        

        decode_button.grid(row = 2, column = 1, padx = 10, pady = 10)

class decode_page(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, bg = "black")
        decode_label = tk.Label(self, text = "Decode", fg= "green", bg = "black", highlightbackground = "green", highlightcolor = "green", highlightthickness = 1)
        decode_label.grid(row = 0, column = 2, padx = 10, pady = 10)

        decode_message_label = tk.Label(self, text="What message would you like to decrypt?: ", fg="green", bg="black")
        decode_message_label.grid(row=1, column=2)

        input_decode = tk.Entry(self, background="black", highlightcolor="green", fg="green", highlightbackground="green")
        input_decode.grid(row=2, column=2)

        decoded_label = tk.Label(self, text="Decrypted Message: ", fg="green", bg="black")
        decoded_label.grid(row=3, column=2)

        def get_input():
            user_input = input_decode.get()
            user_input = decrypt_message(user_input)
            decoded_display.config(text=user_input)
            
        confirm_button = tk.Button(self, text = "Confirm", command = get_input, fg="green", bg="black", background="black")
        confirm_button.grid(row=2, column=4)
        

        
        decoded_display = tk.Label(self, text="", fg = "green", bg = "black", wraplength=225)
        decoded_display.grid(row=4, column=2)

        def copy_text():
            disp_text = decoded_display.cget("text")
            app.clipboard_clear()
            app.clipboard_append(disp_text)
            app.update()

        copy_decode =tk.Button(self, bg="black", text="copy", command=copy_text, fg="green")
        copy_decode.grid(row=4, column=4)
        
        #---------------------------------------END DECODE PAGE-------------------------------------------------

        main_button = tk.Button(
            self,
            text = "Main",
            bg="black",
            fg= "green",
            highlightbackground = "black", 
            highlightcolor = "black",
            highlightthickness = 1,
            activebackground= "black",
            command = lambda : controller.show_frame(Main_page))

        main_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        encode_button = tk.Button(
            self,
            text = "Encode",
            bg="black",
            fg= "green",
            highlightbackground = "black", 
            highlightcolor = "black",
            highlightthickness = 1,
            activebackground= "black",
            command = lambda: controller.show_frame(encode_page)
        )
        encode_button.grid(row = 2, column = 1, padx = 10, pady = 10)


class encode_page(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent, background= "black")
        encode_label = tk.Label(self, 
        text = "Encode", 
        fg= "green", 
        bg = "black", 
        highlightbackground = "green", 
        highlightcolor = "green", 
        highlightthickness = 1)

        encode_label.grid(row = 0, column = 2, padx = 10, pady = 10)
        encode_message_label = tk.Label(self, text="What message would you like to encript?: ", fg="green", bg="black")
        encode_message_label.grid(row=1, column=2)

        input_encode = tk.Entry(self, background="black", highlightcolor="green", fg="green", highlightbackground="green")
        input_encode.grid(row=2, column=2)

        message = input_encode.get()
        
        encoded_label = tk.Label(self, text="Encrypted Message: ", fg="green", bg="black")
        encoded_label.grid(row=3, column=2)

        def get_input():
            user_input = input_encode.get()
            user_input = encrypt_message(user_input)
            encoded_display.config(text=user_input)
            
        confirm_button = tk.Button(self, text = "Confirm", command = get_input, fg="green", bg="black", background="black")
        confirm_button.grid(row=2, column=4)
        

        
        encoded_display = tk.Label(self, text="", fg = "green", bg = "black", wraplength=300)
        encoded_display.grid(row=4, column=2)

        def copy_text():
            disp_text = encoded_display.cget("text")
            app.clipboard_clear()
            app.clipboard_append(disp_text)
            app.update()

        copy_encode = tk.Button(self, bg="black", fg="green", text="copy", command=copy_text)
        copy_encode.grid(row=4, column=4)

        ## at this point the output of the user input has been coded, need to now incorporate this onto the decode page, and then also wokr on figuring out a way for the uset ot be able to copy it ot their clipboard, then just cleaninig up code and colours and formatting
#---------------------------------------END ENCODE PAGE-------------------------------------------------


        main_button = tk.Button(
            self, 
            text = "Main",
            bg="black",
            fg= "green",
            highlightbackground = "black", 
            highlightcolor = "black",
            highlightthickness = 1,
            activebackground= "black", command = lambda : controller.show_frame(Main_page))
        
        main_button.grid(row = 1, column = 1, padx = 10, pady = 10)

        decode_button = tk.Button(
            self,
            text = "Decode",
            bg="black",
            fg= "green",
            highlightbackground = "black", 
            highlightcolor = "black",
            highlightthickness = 1,
            activebackground= "black",
            command = lambda: controller.show_frame(decode_page)
        )
        
        decode_button.grid(row = 2, column = 1, padx = 10, pady = 10)


app = encryptionApp()
app.configure(background = "black")
app.geometry("525x325")
app.title('Message Encryption Software')
app.mainloop()  

