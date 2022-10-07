"""L’analisi prende in considerazione i numeri relativi a due paesi aventi un simile numero di popolazione totale
ma molto diversi tra loro: Italia e Sud Africa. Essi infatti, sono geograficamente molto distanti,
appartengono a due continenti diversi e sono rispettivamente un paese sviluppato ed uno in via di svilippo."""

import csv

dataset = []
with open('C:\\Users\\sergi\\Desktop\\data.csv.csv', 'r') as file:   #importazione dataset ospedalizzazioni
    reader = csv.reader(file)
    for row in reader:
        dataset.append(row)            # Creazione lista di lista contenente dati dataset importato



def media_(paese, indicatore):


    """Calcola la media aritmetica
       : param paese: primo input
       : param indicatore: secondo input
       : return: torna la media di n valori
       """


    l_media=[]
    for i in dataset:
        if i[0] == paese and i[3] == indicatore:
            l_media.append(i[4])
    i = 0
    somma = 0
    while i >= 0 and i < len( l_media):
        somma = somma + float( l_media[i])
        i = i + 1
    med_ = somma / len( l_media)
    return med_


media_ITA_dho= media_('Italy','Daily hospital occupancy')
media_ITA_ICU= media_('Italy','Daily ICU occupancy')
media_ZAF_dho= media_('South Africa','Daily hospital occupancy')
media_ZAF_ICU= media_('South Africa','Daily ICU occupancy')


def max_min(paese, indicatore):


    """Calcola i valori massimo e minimo
    : param paese: primo input
    : param indicatore: secondo input
    : return: torna i valori massimo e minimo di n valori ed i relativi indici
    """


    l_max_min=[]
    data_max_min=[]
    for i in dataset:
        if i[0] == paese and i[3] == indicatore:
            l_max_min.append(float(i[4]))
            data_max_min.append(i[2])
    v_max=max(l_max_min)
    v_min=min(l_max_min)
    i_max = l_max_min.index(v_max)
    datamax= data_max_min[i_max]
    i_min = l_max_min.index(v_min)
    datamin= data_max_min[i_min]
    return v_max, v_min, datamax, datamin


max_ITA, min_ITA, datamax_ITA, datamin_ITA=max_min('Italy','Daily hospital occupancy')
max_ITA_ICU, min_ITA_ICU, datamax_ITA_ICU, datamin_ITA_ICU=max_min('Italy','Daily ICU occupancy')
max_ZAF, min_ZAF, datamax_ZAF, datamin_ZAF=max_min('South Africa','Daily hospital occupancy')
max_ZAF_ICU, min_ZAF_ICU, datamax_ZAF_ICU, datamin_ZAF_ICU=max_min('South Africa','Daily ICU occupancy')


print('Dai dati importati si può notare che la media giornaliera degli ospedalizzati per Covid-19 è ', round(media_ITA_dho,1), 'in Italia mentre ', round(media_ZAF_dho,1), 'in Sud Africa; inoltre, si può notare che, dei pazienti ospedalizzati, quelli in terapia intensiva sono al giorno mediamente ', round(media_ITA_ICU,1), 'in Italia e ', round(media_ZAF_ICU,1), 'in Sud Africa.')
print('I valori massimi degli ospedalizzati sono stati rispettivamente ', max_ITA, 'e ', max_ZAF, 'verificatisi il ', datamax_ITA, 'ed il ', datamax_ZAF, ';')
print('i valori massimi degli ospedalizzati in terapia intensiva in Italia e Sud Africa sono stati rispettivamente ', max_ITA_ICU, 'e ', max_ZAF_ICU, 'verificatisi il ', datamax_ITA_ICU, 'ed il ', datamax_ZAF_ICU,'.')




import json

f = open('C:\\Users\\sergi\\Desktop\\morti.json')
data = json.load(f)

keys=list(data.keys())


valori_continente=data['continent']
valori_tot_death=data['total_deaths']


valori_cont_totdeath=[valori_continente]+[valori_tot_death]


#def total_deaths(paese)
l_total=[]

for i in valori_cont_totdeath:



