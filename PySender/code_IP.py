from Custom_Error import *

def reduce_IP(ip):
    parties_transformees = ip.split('.')

    # Vérifier si l'adresse IP est valide
    if len(parties_transformees) != 4:
        raise WrongIPError()
    
    try:
        # Enlever les zéros non significatifs à gauche pour chaque partie
        parties_detransformees = [str(int(x)) for x in parties_transformees]
        adresse_detransformee = ".".join(parties_detransformees)
        return adresse_detransformee
    except ValueError as e:
        LOGGER.error("ValueError while reducing the IP:")
        LOGGER.error(e)
        return None

def increase_IP(ip):
    parties = ip.split('.')
    
    # Vérifier si l'adresse IP est valide
    if len(parties) != 4:
        raise WrongIPError()
    
    try:
        # Ajouter des zéros non significatifs à gauche pour chaque partie
        parties_transformees = [f"{int(x):03d}" for x in parties]
        adresse_transformee = ".".join(parties_transformees)
        return adresse_transformee
    except ValueError as e:
        LOGGER.error("ValueError while increasing the IP:")
        LOGGER.error(e)
        return None

def create_code(ip):
    parties =   ip.split('.')

    # Vérifier si l'adresse IP est valide
    if len(parties) != 4:
        raise WrongIPError()

    try:
        # Transformer chaque partie en une chaîne de trois chiffres
        parties_transformees = [f"{int(x):03d}" for x in parties]
        adresse_transformee = "".join(parties_transformees)
        return adresse_transformee
    except ValueError as e:
        LOGGER.error("ValueError while reducing the IP:")
        LOGGER.error(e)
        return None

def read_code(adresse_transformee):
    # Vérifier si l'adresse IP transformée est constituée de 12 chiffres
    if len(adresse_transformee) != 12 or not adresse_transformee.isdigit():
        raise WrongIPError()
    
    # Détacher chaque groupe de trois chiffres pour former l'adresse IP détransformée
    parties_detransformees = [adresse_transformee[i:i+3] for i in range(0, 12, 3)]
    adresse_detransformee = ".".join(parties_detransformees)
    
    return adresse_detransformee