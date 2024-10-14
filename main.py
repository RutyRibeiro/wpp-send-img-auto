import pywhatkit as wkit
from colorama import Fore, Style

def readContactsFile():
    with open("contacts.txt", 'r') as file:
        lines = file.readlines()
        
        contacts = [line.strip() for line in lines]

        return contacts

def sendMessage(phoneNo):
    with open('cardapio-do-dia/msg/message.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    wkit.sendwhats_image(receiver = phoneNo, 
                     img_path = "cardapio-do-dia/img/image.jpeg",
                     caption = content,
                     wait_time = 20,
                     tab_close = True,
                     close_time = 4
                    )

print(f"{Fore.GREEN}Enviando mensagens...{Style.RESET_ALL}")

contacts = readContactsFile()

for contact in contacts:
    sendMessage(contact)

print(f"Cardápio enviado para {Fore.GREEN}{len(contacts)}{Style.RESET_ALL}clientes.")