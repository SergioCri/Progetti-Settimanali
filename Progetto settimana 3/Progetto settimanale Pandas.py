from sqlalchemy import create_engine
import pandas as pd


db_connection_str = 'mysql+pymysql://root1:root1@127.0.0.1/ecommerce2'
db_connection = create_engine(db_connection_str)


sql1 = "SELECT avg(p.valore) PREZZO_MEDIO_CASE from prezzo as p join prodotto as pr on p.pid=pr.pid join categoria as c on c.cid=pr.cid where c.nome='CASE'"
sql2 = "SELECT count(o.oid) tot_ordini_Roma from ordine o join indirizzo i  on o.inid=i.inid where citta='Roma' ;"
sql3 = "select pr.nome NOME_PRODOTTO, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid order by m.nome,pr.nome ;"
sql4 = "select count(pr.nome) TOT_PRODOTTI, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid group by m.nome order by m.nome;"
sql5 = "select count(pr.nome) TOT_PRODOTTI, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid group by m.nome order by TOT_PRODOTTI desc;"
sql6 = "select count(oid) TOT_ORDINI, sp.nome TIPO_SPEDIZIONE from ordine o join pasp01 pa on o.paspid=pa.paspid join spedizione sp on sp.spid=pa.spid group by sp.nome;"
sql7 = "select nome,cognome,avg(prezzo) SPESA_MEDIA from utente u join ordine o on u.uid=o.oid join orpr01 op on op.oid=o.oid group by nome,cognome HAVING SPESA_MEDIA >= 100 order by SPESA_MEDIA DESC"
sql8 = "select i.provincia PROVINCIA, max(prezzo) MAX_SPESA from indirizzo i join ordine o on i.uid=o.uid join orpr01 op on op.oid=o.oid group by PROVINCIA"
sql9 = "select p.nome TIPOLOGIA_PAGAMENTO, count(p.nome) N_ORDINI from pagamento p join pasp01 pa on p.paid=pa.paid join ordine o on o.paspid=pa.paspid group by p.nome ;"
sql10 = "select o.time,orp.quantita,p.nome from ordine o join orpr01 orp on o.oid=orp.oid join prodotto p on p.pid=orp.pid  group by p.nome order by orp.quantita desc;"

"""
def read_sql_query(query, db_connection):

    stm = pd.read_sql(query, db_connection)

    return stm

print(read_sql_query(sql1, db_connection))

"""

df_prezzo = pd.read_sql("prezzo", db_connection)
df_prodotto = pd.read_sql("prodotto", db_connection)
df_categoria = pd.read_sql("categoria", db_connection)
df_ordine = pd.read_sql("ordine", db_connection)
df_indirizzo = pd.read_sql("indirizzo", db_connection)
df_marca = pd.read_sql("marca", db_connection)
df_pasp01 = pd.read_sql("pasp01", db_connection)
df_spedizione = pd.read_sql("spedizione", db_connection)
df_orpr01 = pd.read_sql("orpr01", db_connection)
df_pagamento = pd.read_sql("pagamento", db_connection)
df_utente= pd.read_sql("utente",db_connection)

#SQL 1 Prezzo medio dei prodotti di categoria CASE
"""
join_prezzo_prodotto=pd.merge(df_prezzo,df_prodotto)
del join_prezzo_prodotto['nome']#cancella colonna nome tabella prodotto
join_prezzo_prodotto_categoria=pd.merge(join_prezzo_prodotto,df_categoria, how='outer')
Prezzo_medio_categoria_CASE = join_prezzo_prodotto_categoria[join_prezzo_prodotto_categoria.nome == 'CASE'].valore.mean()
#print(Prezzo_medio_categoria_CASE)
"""

#SQL2 Ordini totali effettuati nella città di ROMA
"""
join_ord_ind= pd.merge(df_ordine,df_indirizzo, how='outer')
ordini_ROMA= join_ord_ind[join_ord_ind.citta == 'Roma'].oid.count() #selezione righe per valore colonna citta==Roma, conteggio oid
#print(ordini_ROMA)
"""

#sql3 Catalogo prodotti ordinato per nome prodotto e nome marca
"""
df_prodotto.rename(columns={'nome':'nome_prod'}, inplace=True) #modifica nome colonna tabella prodotto
join_prod_marca=pd.merge(df_prodotto, df_marca, how='outer')
catalogo_ordinato=join_prod_marca[['nome_prod','nome']].sort_values(by=['nome', 'nome_prod']) #sort by delle due colonne
#print(catalogo_ordinato)
"""

#Numero di prodotti per ogni marca
#sql4 = "select count(pr.nome) TOT_PRODOTTI, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid group by m.nome order by m.nome;"

"""
df_prodotto.rename(columns={'nome':'nome_prod'}, inplace=True) #modifica nome colonna tabella prodotto
join_prod_marca=pd.merge(df_prodotto, df_marca, how='outer')
grouped_join_prod_marca=join_prod_marca.groupby(['nome']).count()#raggruppamento per nome marca
sorted_grouped_join_prod_marca=grouped_join_prod_marca['nome_prod'].sort_index()
print(sorted_grouped_join_prod_marca)
"""



#Marche con più prodotti a catalogo
#sql5 = "select count(pr.nome) TOT_PRODOTTI, m.nome NOME_MARCA from prodotto pr join marca m on pr.mid=m.mid group by m.nome order by TOT_PRODOTTI desc;"
"""
df_prodotto.rename(columns={'nome':'nome_prod'}, inplace=True) #modifica nome colonna tabella prodotto
join_prod_marca=pd.merge(df_prodotto, df_marca, how='outer')
grouped_join_prod_marca=join_prod_marca.groupby(['nome']).count()#raggruppamento per nome marca
sorted_grouped_join_prod_marca=grouped_join_prod_marca['nome_prod'].sort_index()
ordered_grouped_join_prod_marca=sorted_grouped_join_prod_marca.sort_values(ascending=False)
print(ordered_grouped_join_prod_marca)
"""

#Totale ordini per tipologia di spedizione scelta
#sql6 = "select count(oid) TOT_ORDINI, sp.nome TIPO_SPEDIZIONE from ordine o join pasp01 pa on o.paspid=pa.paspid join spedizione sp on sp.spid=pa.spid group by sp.nome;"
"""
join_ord_pasp01=pd.merge(df_ordine,df_pasp01)
join_ord_pasp01_sped=pd.merge(join_ord_pasp01,df_spedizione, how='outer')
grouped_join_ord_pasp01_sped=join_ord_pasp01_sped.groupby(['nome']).count()
clean_grouped_join_ord_pasp01_sped=grouped_join_ord_pasp01_sped.drop(['uid','stid', 'time', 'inid', 'paspid', 'paid', 'spid', 'costo'], axis = 1)
print(clean_grouped_join_ord_pasp01_sped)
"""

#Utenti con spesa media superiore ad euro 100
#sql7 = "select nome,cognome,avg(prezzo) SPESA_MEDIA from utente u join ordine o on u.uid=o.oid join orpr01 op on op.oid=o.oid group by nome,cognome HAVING SPESA_MEDIA >= 100 order by SPESA_MEDIA DESC"


"""
join_ut_ord=pd.merge(df_utente,df_ordine, how='outer')
join_ut_ord_orpr=pd.merge(join_ut_ord,df_orpr01, how='outer')
clean_join_ut_ord_orpr=join_ut_ord_orpr.drop(['piva', 'telefono', 'rag_soc', 'cfisc',
       'email', 'user', 'pass', 'newsletter', 'lsid', 'enabled', 'societa',
       'time', 'stid', 'inid', 'paspid', 'pid', 'quantita'], axis = 1)
#x=clean_join_ut_ord_orpr.dropna(inplace=True)
grp_clean_join_ut_ord_orpr=clean_join_ut_ord_orpr.groupby(['prezzo']).mean()
print(grp_clean_join_ut_ord_orpr)
"""

#Spesa massima effettuata per provincia
#sql8 = "select i.provincia PROVINCIA, max(prezzo) MAX_SPESA from indirizzo i join ordine o on i.uid=o.uid join orpr01 op on op.oid=o.oid group by PROVINCIA
"""
join_in_ord=pd.merge(df_indirizzo,df_ordine)
join_ind_ord_orpr= pd.merge(join_in_ord,df_orpr01)

x=join_ind_ord_orpr.drop(['inid', 'uid', 'via', 'numero', 'citta', 'cap', 'telefono',
       'nome', 'cognome', 'principale', 'oid', 'stid', 'time', 'paspid', 'pid',
       'quantita', 'lsid'], axis = 1)

grp_join_ind_ord_orpr=x.groupby(['provincia']).max()
print(grp_join_ind_ord_orpr)

"""

#Numero ordini effettuati per tipologia pagamento
#sql9 = "select p.nome TIPOLOGIA_PAGAMENTO, count(p.nome) N_ORDINI from pagamento p join pasp01 pa on p.paid=pa.paid join ordine o on o.paspid=pa.paspid group by p.nome ;"

"""
join_pag_pasp=pd.merge(df_pagamento,df_pasp01)
join_pag_pasp_ord=pd.merge(join_pag_pasp,df_ordine)
cln_join_pag_pasp_ord= join_pag_pasp_ord.drop(['paid', 'spid', 'paspid', 'uid', 'oid', 'stid', 'time','inid'],axis=1)
cln_join_pag_pasp_ord.rename(columns={'costo':'n_ordini'}, inplace=True)
print(cln_join_pag_pasp_ord.groupby(['nome']).count())

"""

#Data nella quale è stato effettuato l'ordine con la maggior quantità del prodotto stesso
#sql10 = "select o.time,orp.quantita,p.nome from ordine o join orpr01 orp on o.oid=orp.oid join prodotto p on p.pid=orp.pid  group by p.nome order by orp.quantita desc;"
"""
join_ord_orpr=pd.merge(df_ordine,df_orpr01 [['oid','pid']],on='oid')
join_ord_orpr_pro=pd.merge(join_ord_orpr,df_prodotto [['quantita','nome','pid']],how='left',on='pid')
print(join_ord_orpr)
"""

