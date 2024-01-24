import socket
from tkinter import filedialog


def sendSTR(IPServeur, PortServeur, Data):
    # Créer un objet socket pour le client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Établir une connexion avec le serveur
    client_socket.connect((IPServeur, PortServeur))
    print(f"Connexion établie avec {IPServeur}:{PortServeur}")
    client_socket.send(Data.encode("utf-8"))

    # Fermer la connexion
    client_socket.close()


# La taille du tampon est le nombre d'octets (ou de bytes) lus ou écrits à chaque itération lors de la lecture ou de l'écriture d'un fichier. | ChatGPT
def sendFile(IPServeur, PortServeur, FilePath=filedialog.askdirectory(), TamponSize=1024):
    # Créer un objet socket pour le client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Établir une connexion avec le serveur
    client_socket.connect((IPServeur, PortServeur))
    print(f"Connexion établie avec {IPServeur}:{PortServeur}")

    # Lire les données binaires du fichier et les envoyer au serveur
    with open(FilePath, 'rb') as fichier:
        donnees_a_envoyer = fichier.read(TamponSize)
        while donnees_a_envoyer:
            client_socket.send(donnees_a_envoyer)
            donnees_a_envoyer = fichier.read(TamponSize)

    # Fermer la connexion
    client_socket.close()
