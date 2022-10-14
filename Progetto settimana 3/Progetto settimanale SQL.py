import mysql.connector

conn = mysql.connector.connect(user='root', password='123smr!@', host='127.0.0.1', database='ecommerce2')

cursor = conn.cursor()

# SQL SELECT STATEMENTS

#Prezzo medio dei prodotti di categoria CASE
sql1 = "SELECT avg(p.valore) PREZZO_MEDIO_CASE from prezzo as p join prodotto as pr on p.pid=pr.pid join categoria as c on c.cid=pr.cid where c.nome='CASE'"

#Ordini totali effettuati nella città di ROMA
sql2 = "SELECT count(o.oid) tot_ordini_Roma from ordine o join indirizzo i  on o.inid=i.inid where citta='Roma' ;"

#Catalogo prodotti ordinato per nome prodotto e nome marca
sql3 = "select pr.nome NOME_PRODOTTO, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid order by m.nome,pr.nome ;"

#Numero di prodotti per ogni marca
sql4 = "select count(pr.nome) TOT_PRODOTTI, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid group by m.nome order by m.nome;"

#Marche con più prodotti a catalogo
sql5 = "select count(pr.nome) TOT_PRODOTTI, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid group by m.nome order by TOT_PRODOTTI desc;"

#Totale ordini per tipologia di spedizione scelta
sql6 = "select count(oid) TOT_ORDINI, sp.nome TIPO_SPEDIZIONE from ordine o join pasp01 pa on o.paspid=pa.paspid join spedizione sp on sp.spid=pa.spid group by sp.nome;"

#Utenti con spesa media superiore ad euro 100
sql7 = "select nome,cognome,avg(prezzo) SPESA_MEDIA from utente u join ordine o on u.uid=o.oid join orpr01 op on op.oid=o.oid group by nome,cognome HAVING SPESA_MEDIA >= 100 order by SPESA_MEDIA DESC"

#Spesa massima effettuata per provincia
sql8 = "select i.provincia PROVINCIA, max(prezzo) MAX_SPESA from indirizzo i join ordine o on i.uid=o.uid join orpr01 op on op.oid=o.oid group by PROVINCIA"

#Numero ordini effettuati per tipologia pagamento
sql9 = "select p.nome TIPOLOGIA_PAGAMENTO, count(p.nome) N_ORDINI from pagamento p join pasp01 pa on p.paid=pa.paid join ordine o on o.paspid=pa.paspid group by p.nome ;"

#Data nella quale è stato effettuato l'ordine con la maggior quantità del prodotto stesso
sql10 = "select o.time,orp.quantita,p.nome from ordine o join orpr01 orp on o.oid=orp.oid join prodotto p on p.pid=orp.pid  group by p.nome order by orp.quantita desc;"

def trying(sql):

    """
    Esegue SQL SELECT Statement
    :param sql  Interrogazione database
    :return fetchall nuova tabella

    """
    try:
        cursor.execute(sql)
        result = cursor.fetchall()

    except:
        conn.rollback()
    return result



print(trying(sql1))

conn.close()