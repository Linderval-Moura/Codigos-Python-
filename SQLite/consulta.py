import sqlite3

con = sqlite3.connect("meu_banco.db")

cursor = con.cursor()

cursor.execute("INSERT INTO cliente (nome, cpf, email) VALUES ('ABC', '1234', 'a@hotmail.com');")

con.commit()  #Para que os códigos sejam executados
con.close()
