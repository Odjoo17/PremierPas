from webscrapping import (
    scrapping_1_votes_total,
    scrapping_2_new_assemblee,
    scrapping_3_liste_circo,
    scrapping_4_votes_par_circo,
    formattage,
    tampon
)

from analyse_data import (
    analyse
)

scrapping_1_votes_total()
scrapping_2_new_assemblee()
scrapping_3_liste_circo()
scrapping_4_votes_par_circo("scrapping_3_liste_circo_dict_circo")
#formattage("scrapping_1_votes_total")
#tampon("scrapping_4_votes_par_circo")
#analyse("resultat_legislatif")
