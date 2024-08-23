
# Imports

import os           # OS Module
import sys          # SYS Module
import shutil       # Shutil Module
import zipfile      # Zipfile Module
import requests     # Requests Module
import datetime     # Datetime Module

Debug:bool = False  # Special debug control. Leave this 'false.'

# Setup

# Inorder to use this you firstly need to have a valid Discord account,
# and you need to have a valid Discord Webhook URL.

WebhookURL:str = ''     # Put your Discord Webhook URL here.
MassUploadFolder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'MassUpload') # Remove this and replace it with your file path, or you can leave it.
NitroAccount = False # If you have a NITRO account then put True.

# - Below this line you shouldn't touch anything 
# unless you know how it works. -

def CheckFileSize(FilePath):
    
    FileSize = os.path.getsize(FilePath)
    
    FileSizeInMegabytes = FileSize / (1024 * 1024)
    
    if NitroAccount:
        
        if FileSizeInMegabytes < 500:
            
            return True
        
        else:
            
            return False
        
    else:
        
        if FileSizeInMegabytes < 25:
            
            return True

        else:
            
            return False
    
def UploadFileToDiscord(FilePath:str, MassUpload:bool):
    
    Payload = {
        'content': f'\n`Saved File! [{datetime.datetime.now()}]`'
    }
                    
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'https://youtube.com',
        'DNT': '1'
    }   
                    
    if FilePath:

        try:
            
            if os.path.exists(FilePath):
                
                FileSizeValid = CheckFileSize(FilePath)
            
                if FileSizeValid:
                
                    with open(FilePath, 'rb') as File:
                                            
                        Files = {
                            'file': File,
                        }
            
                        Response = requests.post(WebhookURL, data=Payload, files=Files)
                        
                        print(f'\n[UPLOADED]: {File}')
                    
        except Exception as e:
            
            if Debug:
                
                print(e)
            
            else:
                
                sys.exit(e)

        input('\n\nPress enter to quit')
        
    elif FilePath == None and MassUpload:
        
        try:
            
            if os.path.exists(MassUploadFolder):
                
                for File in os.listdir(MassUploadFolder):
                    
                    if os.path.isfile(os.path.join(MassUploadFolder, File)):
                        
                        FileSizeValid = CheckFileSize(os.path.join(MassUploadFolder, File))
                        
                        if FileSizeValid:
                        
                            with open(os.path.join(MassUploadFolder, File), 'rb') as File:
                                
                                Files = {
                                    'file': File,
                                }
                
                                Response = requests.post(WebhookURL, data=Payload, files=Files)

                                print(f'\n[UPLOADED]: {File}')
        except Exception as e:
            
            if Debug:
                
                print(e)
            
            else:
                
                sys.exit(e)
                
        input('\n\nPress enter to quit')
                    
    else:
        
        sys.exit('[ERROR]')
            

def Main():
    
    try:
            
        print(f'Welcome to DiscordFileSaver! Options\n\n1. Mass Upload\n2. Single Upload\n\n[WARNING]: Please view the Python file, and configure all settings for this to work properly.')
        
        while True:
            
            UserOption = input('\n\nOption 1-2: ')
            
            if UserOption == '1':
                
                UploadFileToDiscord(None, True)
                
                break
                
            elif UserOption == '2':
                
                FilePath = input(str('\n\nFile Path: '))
                
                UploadFileToDiscord(FilePath, False)
                
                break
                
            else:
                
                pass
            
                
                
        
    except Exception as e:
            
            if Debug:
                
                print(e)
            
            else:
                
                sys.exit(e)
        


if __name__ == "__main__":
    
    Main()