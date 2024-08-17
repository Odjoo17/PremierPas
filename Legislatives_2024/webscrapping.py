import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import create_pickle,use_pickle,init_logger

def scrapping_1_votes_total() :
    scrapper = init_logger('scrapper_1')
    data = init_logger('data_1')
    URL = "https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/index.html"
    response = requests.request(method="get",url=URL)
    response.encoding = 'utf-8'
    html_content = response.text
    #print ("response.text",html_content)
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding=response.encoding)
    page_content = soup.prettify()
    #print("soup",page_content)
    table = soup.findAll('table')
    #print(table[1])
    scrapper.debug(f'Tables from {URL}:\n{table}')

    df={}
    data.debug(f'Data from {URL}')

    for i in range(0,4):
        headers = []
        rows = []
        # Extraire les lignes de données
        for j, row in enumerate(table[i].find_all('tr')):
            #print(j,rows)
            cells = row.find_all(['td', 'th'])
            row_data = [cell.text.strip().replace('\u202f', '').replace('\xa0', '') for cell in cells]
            
            # Si c'est la première ligne, extraire les en-têtes
            if j == 0:
                # Gérer les en-têtes vides ou manquants
                for k, header in enumerate(row_data):
                    if header == "":
                        headers.append(f"Column{k+1}")  # Nom générique si l'en-tête est vide
                        #print(header)
                    else:
                        headers.append(header)
                        #print(header)
            else:
                # Ajouter des valeurs None pour les cellules manquantes
                while len(row_data) < len(headers):
                    row_data.append(None)
                rows.append(row_data)
            #print(headers,rows)

        #Création du DataFrame
        df[i] = pd.DataFrame(rows, columns=headers)
        df[i].replace("", np.nan, inplace=True)
        #print(df[i])
        data.info(f'\ndf{i}:\n{df[i]}')
    create_pickle(df,'scrapping_1_votes_total')

def scrapping_2_new_assemblee() :
    scrapper = init_logger('scrapper_2')
    data = init_logger('data_2')
    URL = "https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/nouvelle_assemblee/index.html"

    response = requests.request(method="get",url=URL)
    response.encoding = 'utf-8'
    html_content = response.text
    #print ("response.text",html_content)
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding=response.encoding)
    page_content = soup.prettify()
    #print("soup",page_content)
    table = soup.findAll('table')
    #print(table[1])
    scrapper.debug(f'Tables from {URL}:\n{table}')

    df={}
    data.debug(f'Data from {URL}')

    for i in range(0,1):
        headers = []
        rows = []
        # Extraire les lignes de données
        for j, row in enumerate(table[i].find_all('tr')):
            #print(j,rows)
            cells = row.find_all(['td', 'th'])
            row_data = [cell.text.strip().replace('\u202f', '').replace('\xa0', '') for cell in cells]
            
            # Si c'est la première ligne, extraire les en-têtes
            if j == 0:
                # Gérer les en-têtes vides ou manquants
                for k, header in enumerate(row_data):
                    if header == "":
                        headers.append(f"Column{k+1}")  # Nom générique si l'en-tête est vide
                        #print(header)
                    else:
                        headers.append(header)
                        #print(header)
            else:
                # Ajouter des valeurs None pour les cellules manquantes
                while len(row_data) < len(headers):
                    row_data.append(None)
                rows.append(row_data)
            #print(headers,rows)

        #Création du DataFrame
        df[i] = pd.DataFrame(rows, columns=headers)
        df[i].replace("", np.nan, inplace=True)
        #print(df[i])
        data.info(f'\ndf{i}:\n{df[i]}')
    create_pickle(df,'scrapping_2_new_assemblee')

def scrapping_3_liste_circo() :
    scrapper = init_logger('scrapper_3')
    data = init_logger('data_3')
    URL = "https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/index.html"

    response = requests.request(method="get",url=URL)
    response.encoding = 'utf-8'
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding=response.encoding)
    page_content = soup.prettify()
    scrapper.debug(f'Tables from {URL}:\n{page_content}')
    options = soup.find_all('option')
    #print('options',options)
    dict_dept = {}

    for option in options: # On récupére les ID des différents départements
        dept = option.text.strip()
        dept_code = option['value']
        #print('value',dept_code)
        if dept_code.startswith('./') :
            dept_code = dept_code.split('/')[1]
            #liste_circo.append([dept_code])
            #print(dept,dept_code)
            dict_dept[dept] = [dept_code]
        elif dept_code == '' : pass
        else :
            dept_code = dept_code.split('/')[0]+"/"+dept_code.split('/')[1]
            #print(dept,dept_code)
            #liste_circo.append([dept_code])
            dict_dept[dept] = [dept_code]
    print(dict_dept)
    create_pickle(dict_dept,'scrapping_3_liste_circo_dict_dept')

    for dept, dept_code in dict_dept.items():
        scrapper_bis = init_logger('scrapper_3_bis')
        URL_dept = f"https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/{dept_code[0]}/index.html"
        response = requests.request(method="get",url=URL_dept)
        response.encoding = 'utf-8'
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding=response.encoding)
        page_content = soup.prettify()
        scrapper_bis.debug(f'Tables from {URL_dept}:\n{page_content}')
        options = soup.find_all('option')
        
        for option in options: # On récupére les ID des différents départements
            circo = option.text.strip()
            circo_code = option['value']
            #print('circo :',circo,'circo_code :',circo_code)
            if circo_code == '' : pass
            else :
                circo_code = circo_code.split('/')[0]
                #liste_circo.append([dept_code])
                print(circo_code)
                dept_code.append(circo_code)
    create_pickle(dict_dept,'scrapping_3_liste_circo_dict_circo')
    print(dict_dept)

def scrapping_4_votes_par_circo(dict_dept_pkl) :
    scrapper = init_logger('scrapper_4')
    data = init_logger('data_4')
    dict_dept = use_pickle(dict_dept_pkl)

    for dept, dept_code in dict_dept.items():
        print("dept",dept,"dept_code",dept_code)
        for i in range (1,len(dept_code)):
            URL_circo = f"https://www.resultats-elections.interieur.gouv.fr/legislatives2024/ensemble_geographique/{dept_code[0]}/{dept_code[i]}/index.html"
            print(URL_circo)
            response = requests.request(method="get",url=URL_circo)
            response.encoding = 'utf-8'
            html_content = response.text
            #print ("response.text",html_content)
            soup = BeautifulSoup(html_content, 'html.parser', from_encoding=response.encoding)
            page_content = soup.prettify()
            #print("soup",page_content)
            table = soup.findAll('table')
            #print(table)
            #scrapper.debug(f'Tables from {URL}:\n{table}')
            df={}
            for k in range(0,4):
                headers = []
                rows = []
                # Extraire les lignes de données
                try : # Gérer le cas où il n'y pas eu de second tour car le candidat a été elu au premier tour
                    for j, row in enumerate(table[k].find_all('tr')):
                        #print(j,rows)
                        cells = row.find_all(['td', 'th'])
                        row_data = [cell.text.strip().replace('\u202f', '').replace('\xa0', '') for cell in cells]
                        
                        # Si c'est la première ligne, extraire les en-têtes
                        if j == 0:
                            # Gérer les en-têtes vides ou manquants
                            for k, header in enumerate(row_data):
                                if header == "":
                                    headers.append(f"Column{k+1}")  # Nom générique si l'en-tête est vide
                                    #print(header)
                                else:
                                    headers.append(header)
                                    #print(header)
                        else:
                            # Ajouter des valeurs None pour les cellules manquantes
                            while len(row_data) < len(headers):
                                row_data.append(None)
                            rows.append(row_data)
                        #print(headers,rows)
                except IndexError : pass
                #Création du DataFrame
                dict_dept[dept].append(pd.DataFrame(rows, columns=headers))
                dict_dept[dept][-1].replace("", np.nan, inplace=True)
                #print(dict_dept[dept][-1])
                #data.info(f'\ndf{i}:\n{df[i]}')
            #print(dict_dept)
            #input("here")
    create_pickle(dict_dept,"scrapping_4_votes_par_circo")

def tampon(pickle_name):
    data = use_pickle(pickle_name)
    for circo, circo_code in data.items():

        print(circo,circo_code[-2])

def formattage(pickle_name):
    data = use_pickle(pickle_name)
    resultat_second_tour = data[0]
    proportion_votant_second_tour = data[1]
    resultat_premier_tour = data[2]
    proportion_votant_premier_tour = data[3]

    # Préciser de quels tours des élections il s'agit :
    new_columns = [col + '_second_tour' for col in resultat_second_tour.columns]
    resultat_second_tour.columns = new_columns

    new_columns = [col + '_premier_tour' for col in resultat_premier_tour.columns]
    resultat_premier_tour.columns = new_columns

    # On concatene les deux df :
    resultat_legislatif = pd.merge(resultat_premier_tour,resultat_second_tour,left_on=resultat_premier_tour.columns[0],right_on=resultat_second_tour.columns[0],how='outer')

    #On détermine les colonnes à convertir en float ou int : 
    colonnes_int = ['Voix_premier_tour', 'Sièges_premier_tour','Voix_second_tour', 'Sièges_second_tour']
    colonnes_float = ['% Inscrits_premier_tour', '% Exprimés_premier_tour','% Inscrits_second_tour', '% Exprimés_second_tour']

    resultat_legislatif[colonnes_int] = resultat_legislatif[colonnes_int].apply(pd.to_numeric, errors='coerce').fillna(0).astype(int)
    resultat_legislatif[colonnes_float] = resultat_legislatif[colonnes_float].apply(lambda x: x.str.replace(' ', '').str.replace(',', '.').astype(float))

    #On trie les résultats par nombre de voix obtenue au second tour par ordre décroissant :
    resultat_legislatif = resultat_legislatif.sort_values(by='Voix_second_tour', ascending=False)
    create_pickle(resultat_legislatif,"resultat_legislatif")
    return resultat_legislatif

