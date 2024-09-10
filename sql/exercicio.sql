-- Criação da tabela Curso (cod_curso, nome_curso)

CREATE TABLE IF NOT EXISTS CURSO(
  cod_curso INT AUTO_INCREMENT,
  nome VARCHAR(150) NOT NULL,
  CONSTRAINT curso_PK PRIMARY KEY (cod_curso)
);

CREATE TABLE IF NOT EXISTS SALA(
  cod_sala INT AUTO_INCREMENT,
  nome_sala VARCHAR(150) NOT NULL,
  CONSTRAINT sala_PK PRIMARY KEY (cod_sala)
);

CREATE TABLE IF NOT EXISTS EQUIPAMENTO(
  cod_equipamento INT AUTO_INCREMENT,
  nm_equipamento VARCHAR(100) NOT NULL,
  valor DECIMAL (10,2),
  quantidade INT NOT NULL,
  tipo VARCHAR(100) NOT NULL,
  CONSTRAINT equipamento_PK PRIMARY KEY (cod_equipamento)
);

CREATE TABLE IF NOT EXISTS PROFESSOR(
  cod_professor INT AUTO_INCREMENT,
  nm_professor VARCHAR(150) NOT NULL,
  telefone VARCHAR(20),
  cod_curso INT,
  salario DECIMAL (10,2),
  CONSTRAINT professor_PK PRIMARY KEY (cod_professor),
  CONSTRAINT professor_FK FOREIGN KEY (cod_curso) REFERENCES CURSO (cod_curso)
);

CREATE TABLE IF NOT EXISTS RESERVA(
  cod_equipamento INT,
  cod_professor INT,
  dt_reserva DATE,
  horário TIME,
  cod_sala INT,
  PRIMARY KEY (cod_equipamento, cod_professor, cod_sala),
  CONSTRAINT reserva_equipamento_FK FOREIGN KEY (cod_equipamento) REFERENCES EQUIPAMENTO (cod_equipamento),
  CONSTRAINT reserva_professor_FK FOREIGN KEY (cod_professor) REFERENCES PROFESSOR (cod_professor),
  CONSTRAINT reserva_sala_FK FOREIGN KEY (cod_sala) REFERENCES SALA (cod_sala)
);

INSERT INTO CURSO (nome) VALUES
('Desenvolvimento de Software'),
('Gestão de Projetos'),
('Marketing Digital'),
('Análise de Dados'),
('Design Gráfico');

INSERT INTO SALA (nome_sala) VALUES
('Sala Alpha'),
('Sala Orion'),
('Sala Everest'),
('Sala Phoenix'),
('Sala Lotus');

INSERT INTO EQUIPAMENTO (nm_equipamento, valor, quantidade, tipo) VALUES
('Projetor Multimídia', 2500.00, 5, 'Audiovisual'),
('Computador Desktop', 3500.00, 10, 'Informática'),
('Mesa de Reunião', 1200.00, 3, 'Mobiliário'),
('Impressora Laser', 800.00, 4, 'Escritório'),
('Quadro Branco Interativo', 1800.00, 2, 'Educação');

-- Utilizando Mock

insert into PROFESSOR (nm_professor, telefone, cod_curso, salario) values ('Sidonia', '(673) 4365287', 2, 6204.93);
insert into PROFESSOR (nm_professor, telefone, cod_curso, salario) values ('Janet', '(588) 9842544', 4, 6594.07);
insert into PROFESSOR (nm_professor, telefone, cod_curso, salario) values ('Basil', '(861) 4426009', 2, 8644.03);
insert into PROFESSOR (nm_professor, telefone, cod_curso, salario) values ('Florian', '(419) 1494845', 1, 8176.31);
insert into PROFESSOR (nm_professor, telefone, cod_curso, salario) values ('Mollee', '(817) 7309056', 4, 9663.73);

-- Utilizando Mock

insert into RESERVA (cod_equipamento, cod_professor, dt_reserva, cod_sala, horário) values (1, 1, '2023/08/26', 4, '12:02:31');
insert into RESERVA (cod_equipamento, cod_professor, dt_reserva, cod_sala, horário) values (4, 1, '2022/08/07', 2, '7:51:16');
insert into RESERVA (cod_equipamento, cod_professor, dt_reserva, cod_sala, horário) values (3, 3, '2023/03/08', 5, '6:34:36');
insert into RESERVA (cod_equipamento, cod_professor, dt_reserva, cod_sala, horário) values (1, 5, '2022/12/23', 4, '10:17:47');
insert into RESERVA (cod_equipamento, cod_professor, dt_reserva, cod_sala, horário) values (5, 4, '2024/04/02', 1, '12:04:29');

