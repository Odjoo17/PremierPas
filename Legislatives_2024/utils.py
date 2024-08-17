import pickle as pk
import logging


def create_pickle(scrapped_data : dict, pickle_name : str):
    with open(pickle_name+".pkl", 'wb') as f:
        pk.dump(scrapped_data, f)
    #print(scrapped_data)

def use_pickle(pickle_name : str):
    with open(pickle_name+".pkl", 'rb') as f:
        loaded_data = pk.load(f)
        #print("This is the loaded data from "+pickle_name+".pkl :\n",loaded_data)
    return loaded_data

def init_logger(file_name : str, mode ='w'): # mode a = ecriture à la suite - mode w = réecriture sur le fichier existant

    # Configuration du logger
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)

    # Création d'un handler de fichier avec encodage UTF-8
    file_handler = logging.FileHandler(file_name+'.log', mode=mode, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Création d'un formatter et ajout au handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Ajout du handler au logger
    logger.addHandler(file_handler)
    return logger