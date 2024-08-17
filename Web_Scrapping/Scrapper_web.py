import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pickle as pk

def scrapping_data():
    summer_olympics_years = list(range(1896, 2024, 4))
    dict_df = {}
    for year in summer_olympics_years :
        dict_df[year] = scrapped_one_game_medals(year)
        with open('medals_data.pkl', 'wb') as f:
            pk.dump(dict_df, f)
    print(dict_df)


def scrapped_one_game_medals(year) :
    URL = f"fr.wikipedia.org/wiki/Tableau_des_m%C3%A9dailles_des_Jeux_olympiques_d%27%C3%A9t%C3%A9_de_{year}"
    #URL = r"olympics.com/en/olympic-games/tokyo-2020"#input("Please put the URL of the website that you want to scrap : ")
    URL_complet = ("https://"+URL)
    #URL_complet = r"https://olympics.com/en/olympic-games/tokyo-2020/medals.com"
    response = requests.request(method="get",url=URL_complet)
    html_content = response.text
    #print (URL_complet,html_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    #print(soup)
    table = soup.find('table')
    #print(table)
    # caption = table.find("caption")
    # print("Titre du tableau : ",caption.text.strip())
    tbody = table.findAll('tbody')[0]
    trow = tbody.findAll('tr')
    #print(trow[0])
    data = []
    cpt = 0
    for row in trow:
        row_data = [elt.text.strip() for elt in row]
        if len(row_data)<11 and cpt == 1 :
            #print("ICI")
            row_data.insert(1,last_rank)
            row_data.insert(2,"")
        cpt = 1
        last_rank=row_data[1]
        #print("LA")
        data.append(row_data)
        print(row_data)
    df = pd.DataFrame(data)
    print(df)
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.replace("", np.nan)
    df = df.dropna(axis=1, how='all')
    #df.to_excel(f"Tableaux_des_médailles_JO_{year}.xlsx",index=False)
    return df

def data_analysis():
    with open('medals_data.pkl', 'rb') as f:
        # Load the Python object from the pickle file
        loaded_data = pk.load(f)
    df_total_medals_per_year = pd.DataFrame(columns=["Year","Total medals"])
    print(df_total_medals_per_year)
    for elt in loaded_data:
        df = loaded_data[elt]
        col = df.columns
        if "Rang" in col :
            print(elt,"\n",df)
            n = len(df)
            #print(n)
            tot_medals = (df.iloc[n-1]["Total"])
            print(tot_medals)
            df_total_medals_per_year = (elt,tot_medals)
    print(df_total_medals_per_year)
            #print (elt,df)
            #print(df_medals_concat)
    
#scrapping_data()
data_analysis()