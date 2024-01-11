import socket
from verification import fileVerification


def Find_open_port(InitialPort=58388, nbrTry=10):
    port = InitialPort
    essai = 0

    while essai < nbrTry:
        try:
            # Cr�er un socket pour tester la disponibilit� du port
            test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            test_socket.bind(('localhost', port))
            test_socket.close()

            # Si la liaison r�ussit, le port est libre
            return port
        except socket.error:
            # Si la liaison �choue, le port est d�j� utilis�, essayer un autre
            essai += 1
            port += 1

    # Si aucun port n'est trouv� apr�s le nombre d'essais sp�cifi�
    raise Exception("Aucun port libre trouv�.")


def getSTR(port="1234", ListenIP="0.0.0.0",TamponSIZE=1024,number_of_connextion_at_the_same_time=1):
    # Cr�er un objet socket pour le serveur
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lier l'objet socket � l'adresse et au port
    serveur_socket.bind((ListenIP, port))

    # Mettre le serveur en mode �coute
    serveur_socket.listen(1)  # 1 connexion � la fois

    print(f"Le serveur �coute sur {ListenIP}:{port}")

    # Accepter la connexion du client
    connexion, adresse_client = serveur_socket.accept()
    print(f"Connexion �tablie depuis {adresse_client}")

    # Recevoir des donn�es du client
    donnees_recues = connexion.recv(TamponSIZE).decode("utf-8")
    print(f"Donn�es re�ues : {donnees_recues}")
    return donnees_recues
    # Fermer la connexion
    connexion.close()
    serveur_socket.close()


def getFile(FileName, port):
    # D�finir l'adresse IP et le port d'�coute du serveur
    adresse_ip = "0.0.0.0"

    # Cr�er un objet socket pour le serveur
    serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Lier l'objet socket � l'adresse et au port
    serveur_socket.bind((adresse_ip, port))

    # Mettre le serveur en mode �coute
    serveur_socket.listen(1)  # 1 connexion � la fois

    print(f"Le serveur �coute sur {adresse_ip}:{port}")

    # Accepter la connexion du client
    connexion, adresse_client = serveur_socket.accept()
    print(f"Connexion �tablie depuis {adresse_client}")

    # Recevoir les donn�es binaires du client et les �crire dans un fichier
    with open(FileName, 'wb') as file:
        donnees_recues = connexion.recv(1024)
        while donnees_recues:
            file.write(donnees_recues)
            donnees_recues = connexion.recv(1024)
    
    fileVerification(FileName)

    # Fermer la connexion
    connexion.close()
    serveur_socket.close()
