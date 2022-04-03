CREATE TABLE IF NOT EXISTS tb_horas(id INTEGER PRIMARY KEY AUTOINCREMENT, data VARCHAR(10), e1_hora VARCHAR(4), s1_hora text(4), e2_hora text(4), s2_hora text(4), horas_totais text(4))

CREATE TABLE IF NOT EXISTS tb_user(id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(15), senha VARCHAR(15), email VARCHAR(30), tel VARCHAR(10))