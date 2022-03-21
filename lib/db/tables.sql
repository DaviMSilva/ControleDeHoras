CREATE TABLE IF NOT EXISTS tb_horas (id INTEGER PRIMARY KEY AUTOINCREMENT, data text(10), e1_hora text, s1_hora text, e2_hora text, s2_hora text, horas_totais text)

CREATE TABLE IF NOT EXISTS tb_user (id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(15), senha VARCHAR(15), email VARCHAR(30), tel VARCHAR(10)