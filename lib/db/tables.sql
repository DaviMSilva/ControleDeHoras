CREATE TABLE IF NOT EXISTS tb_horas (id INTEGER PRIMARY KEY AUTOINCREMENT, data VARCHAR(10), e1_hora VARCHAR(4), s1_hora text(4), e2_hora text(4), s2_hora text(4), horas_totais text(4))

CREATE TABLE IF NOT EXISTS tb_user (id INTEGER PRIMARY KEY AUTOINCREMENT, us_login VARCHAR(15), us_senha VARCHAR(15), us_email VARCHAR(30), us_tel VARCHAR(10))