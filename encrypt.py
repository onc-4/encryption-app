import pandas as pd

file_path = "/Users/omer.chandna/Documents/projects/encryption/decodekey.csv" 
encryption_key = pd.read_csv(file_path, sep=',' , names=['Character' , 'Byte'], header=None, skiprows=[0]) # setting up pandas to read the ecnryption csv file

dframe = pd.DataFrame(data=encryption_key) # creating the data frame for pandas
dframe['Character'] = dframe['Character'].astype(str)
dframe['Byte'] = dframe['Byte'].astype(str)

def split_by_char(message): # creating a function which will split the message by characters in order to reference it with the encryption key and convert each character
    return [char for char in message] # returns a list containing each charcter in the message, which will then be encrypted character by character using the encryption key

message = input("What message would you like to encrypt?: ") # the user can enter any message they want to encrypt

to_encript = split_by_char(message)

def encrypt_message(to_encript):
    
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

print("your encrypted message: " + encrypt_message(to_encript))

coded = encrypt_message(to_encript)

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

print("your decrypted message: " + decrypt_message(coded))



