# metodi#

# calcolo del massimo tra 3 variabili#

primo = int(input('leggi numero:'))
secondo = int(input('leggi numero:'))
terzo = int(input('leggi numero:'))


def massimo(x, y, z):
    """Calcola il massimo tra tre interi
    : param x: primo input
    : param z: secondo input
    : param y: terzo input
    : return: torna il massimo tra tre interi
    """
    if x > y:
        if x > z:
            return x
        else:
            return z
    elif y > z:
        return y
    else:
        return z


m = massimo(primo, secondo, terzo)
print('il massimo è :', m)
print('finito')


def media(numero1, numero2):
    somma = numero1 + numero2
    m = somma / 2
    return m


def somma_diff(numero1, numero2):
    s = numero1 + numero2
    d = numero1 - numero2
    p = numero1 * numero2
    return s, d, p


print(somma_diff(10, 17))

v1, v2, v3 = somma_diff(10, 17)

print(v1)
print(v2)
print(v3)


def incrementa_elem(l):
    for i in range(len(l)):
        l[i] = l[i] + 1


lista = [1, 2, 3, 4, 5]
print(lista)
incrementa_elem(lista)
print(lista)

import csv
import json


def read_csv_as_dict(file_path):
    """
    Legge un file CSV e inserisce i dati in un dizionario
    :param file_path: file path of csv
    :return: data read from file
    """
    with open(file_path, mode='r') as csv_file:
        data = csv.DictReader(csv_file)
    return data


def read_csv_as_list(file_path, delimiter=","):
    """
    Legge un file CSV e inserisce i dati in una lista di liste (lista di righe)
    :param file_path: file path of csv
    :param delimiter: delimiter used in the csv file
    :return: data read from file
    """
    with open(file_path) as csv_file:
        data = csv.reader(csv_file, delimiter=delimiter)
    return data


def read_json(file_path):
    """
    Legge un file JSON e inserisce i dati in un dizionario
    :param file_path: file path of json
    :return: data read from file
    """
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data


if __name__ == '__main__':
    read_csv_as_dict('/scrivere/il/percorso/del/file/csv')
    read_csv_as_list('/scrivere/il/percorso/del/file/csv', ',')
    read_json('/scrivere/il/percorso/del/file/json')
