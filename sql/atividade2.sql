-- BANCO DE DADOS EMPRESADB

CREATE TABLE IF NOT EXISTS DEPARTAMENTO (
    numdepto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS EMPREGADO (
    matricula INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(70) NOT NULL,
    salario DECIMAL(10,2),
    numdepto INT,
    CONSTRAINT EMPREGADO_FK FOREIGN KEY (numdepto) REFERENCES DEPARTAMENTO(numdepto)
);

CREATE TABLE IF NOT EXISTS PROJETO (
    codprojeto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_inicio DATE,
    data_fim DATE
);

CREATE TABLE IF NOT EXISTS TRABALHA_EM (
    matricula INT,
    codprojeto INT,
    data_inicio DATE,
    data_fim DATE,
    PRIMARY KEY (matricula, codprojeto),
    CONSTRAINT TRABALHA_FK FOREIGN KEY (matricula) REFERENCES EMPREGADO(matricula),
    CONSTRAINT TRABALHA_FK1 FOREIGN KEY (codprojeto) REFERENCES PROJETO(codprojeto)
);

CREATE TABLE IF NOT EXISTS HABILIDADE (
    codhabilidade INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS EMPREGADO_HABILIDADE (
    matricula INT,
    codhabilidade INT,
    PRIMARY KEY (matricula, codhabilidade),
    CONSTRAINT EMPREGADO_HAB_FK FOREIGN KEY (matricula) REFERENCES EMPREGADO(matricula),
    CONSTRAINT EMPREGADO_HAB_FK1 FOREIGN KEY (codhabilidade) REFERENCES HABILIDADE(codhabilidade)
);

-- 1. Empregados e seus Departamentos (INNER JOIN) 

SELECT * FROM EMPREGADO AS EMP INNER JOIN DEPARTAMENTO AS DEP ON DEP.numdepto = EMP.numdepto;

-- 2. Empregados sem Departamento (LEFT JOIN + IS NULL)

SELECT * FROM EMPREGADO AS EMP LEFT JOIN DEPARTAMENTO AS DEP ON DEP.numdepto = EMP.numdepto WHERE EMP.numdepto IS NULL;

-- 3, Projetos sem Empregados (LEFT JOIN + IS NULL) Liste todos os projetos que não têm empregados associados.

SELECT * FROM PROJETO AS PR LEFT JOIN TRABALHA_EM AS TR ON TR.codprojeto = PR.codprojeto LEFT JOIN EMPREGADO AS EMP ON EMP.matricula = TR.matricula WHERE TR.matricula IS NULL;

-- 4. Empregados e suas Habilidades (INNER JOIN)

SELECT * FROM EMPREGADO AS EMP INNER JOIN EMPREGADO_HABILIDADE AS EHA ON EMP.matricula = EHA.matricula INNER JOIN HABILIDADE AS H ON H.codhabilidade = EHA.codhabilidade; 

-- 5. Empregados sem Habilidades (LEFT JOIN + IS NULL) Liste todos os empregados que não têm habilidades associadas. 

SELECT * FROM EMPREGADO AS EMP LEFT JOIN EMPREGADO_HABILIDADE AS EHA ON EMP.matricula = EHA.matricula LEFT JOIN HABILIDADE AS H ON H.codhabilidade = EHA.codhabilidade WHERE EHA.codhabilidade IS NULL; 

-- 6. Departamentos e Número de Empregados (LEFT JOIN + COUNT) Liste todos os departamentos e o número de empregados em cada um.

SELECT DEP.numdepto, DEP.nome, COUNT(EMP.matricula) AS numero_de_empregados FROM DEPARTAMENTO AS DEP LEFT JOIN EMPREGADO AS EMP ON DEP.numdepto = EMP.numdepto GROUP BY DEP.numdepto;

-- 7. Empregados e seus Projetos (INNER JOIN) Liste todos os empregados juntamente com os projetos em que estão trabalhando.

SELECT * FROM EMPREGADO AS EM INNER JOIN TRABALHA_EM AS TR ON TR.matricula = EM.matricula INNER JOIN PROJETO AS PR ON PR.codprojeto = TR.codprojeto;

-- 8. Empregados em Projetos Atuais (INNER JOIN + WHERE) Liste todos os empregados que estão trabalhando em projetos que ainda não terminaram.

SELECT * FROM EMPREGADO AS EM INNER JOIN TRABALHA_EM AS TR ON TR.matricula = EM.matricula INNER JOIN PROJETO AS PR ON PR.codprojeto = TR.codprojeto WHERE PR.data_fim > CURDATE();

-- 9. Projetos e Duração (DATEDIFF) Liste todos os projetos juntamente com a duração em dias (diferente entre data_fim e data_inicio).

SELECT *, DATEDIFF(PR.data_fim, PR.data_inicio) AS dias_diferenca FROM PROJETO AS PR;

-- 10. Empregados com Mais de uma Habilidade (INNER JOIN + HAVING COUNT) Liste todos os empregados que têm mais de uma habilidade.

SELECT EMP.matricula, EMP.nome, EMP.salario, EMP.numdepto, COUNT(EHA.matricula) AS Numero_habilidades FROM EMPREGADO AS EMP INNER JOIN EMPREGADO_HABILIDADE AS EHA ON EMP.matricula = EHA.matricula INNER JOIN HABILIDADE GROUP BY EMP.matricula HAVING Numero_habilidades > 2; 

-- 11. Departamentos e Salário Médio (LEFT JOIN + AVG) Liste todos os departamentos juntamente com o salário médio dos empregados em cada departamento.

SELECT DEP.numdepto, DEP.nome, AVG(EMP.salario) AS Salário_Médio FROM DEPARTAMENTO AS DEP LEFT JOIN EMPREGADO AS EMP ON DEP.numdepto = EMP.numdepto GROUP BY DEP.numdepto

-- 12. Empregados e suas Habilidades Ordenadas (INNER JOIN + ORDER BY) Liste todos os empregados juntamente com suas habilidades, ordenando os resultados pelo nome do empregado e pela descrição da habilidade.

SELECT * FROM EMPREGADO AS EMP INNER JOIN EMPREGADO_HABILIDADE AS EHA ON EMP.matricula = EHA.matricula INNER JOIN HABILIDADE AS H ON H.codhabilidade = EHA.codhabilidade ORDER BY EMP.nome, H.descricao; 

-- 13. Projetos e Número de Empregados (INNER JOIN + COUNT) Liste todos os projetos juntamente com o número de empregados que estão trabalhando em cada projeto.

SELECT PR.codprojeto, PR.nome, PR.data_inicio, PR.data_fim, COUNT(TR.matricula) as Número_de_empregados FROM PROJETO AS PR INNER JOIN TRABALHA_EM AS TR ON PR.codprojeto = TR.codprojeto GROUP BY PR.codprojeto;

-- 14. Empregados com Habilidades Específicas (INNER JOIN + WHERE) Liste todos os empregados que possuem uma habilidade específica (por exemplo, "SQL").

SELECT * FROM EMPREGADO AS EMP INNER JOIN EMPREGADO_HABILIDADE AS EHA ON EMP.matricula = EHA.matricula INNER JOIN HABILIDADE AS H ON H.codhabilidade = EHA.codhabilidade WHERE H.descricao LIKE '%SQL%'; 

-- 15. Departamentos sem Empregados (LEFT JOIN + IS NULL) Liste todos os departamentos que não têm empregados associados.

SELECT * FROM DEPARTAMENTO AS DEP LEFT JOIN EMPREGADO AS EMP ON DEP.numdepto = EMP.numdepto WHERE EMP.matricula IS NULL;

-- 16. Projetos Ativos e seus Empregados (INNER JOIN + WHERE) Liste todos os projetos que ainda estão em andamento e os empregados que estão trabalhando neles.

SELECT * FROM PROJETO AS PR INNER JOIN TRABALHA_EM as TR ON PR.codprojeto = TR.codprojeto INNER JOIN EMPREGADO AS EM ON EM.matricula = TR.matricula WHERE PR.data_fim > CURDATE();

-- 17. Empregados e suas Habilidades e Projetos (INNER JOIN + Multiple Tables)  Liste todos os empregados juntamente com suas habilidades e os projetos em que estão trabalhando.

SELECT * FROM EMPREGADO AS EM INNER JOIN EMPREGADO_HABILIDADE AS EH ON EH.matricula = EM.matricula INNER JOIN HABILIDADE as HA ON HA.codhabilidade = EH.codhabilidade INNER JOIN TRABALHA_EM AS TR ON TR.matricula = EM.matricula INNER JOIN PROJETO AS PR ON PR.codprojeto = TR.codprojeto;

-- 18. Projetos e Data de Início mais Recente (INNER JOIN + MAX) Liste todos os projetos juntamente com a data de início mais recente de um empregado que começou a trabalhar nesse projeto.

SELECT * FROM EMPREGADO AS EM INNER JOIN TRABALHA_EM AS TR ON TR.matricula = EM.matricula INNER JOIN PROFESSOR AS PR ON TRABALHA_EM.codprojeto = PR.codprojeto ORDER BY TRABALHA_EM.data_inicio = (SELECT MAX(data_inicio) FROM TRABALHA_EM);

-- Empregados que Trabalham em Mais de um Projeto (INNER JOIN + HAVING COUNT) Liste todos os empregados que estão trabalhando em mais de um projeto.

SELECT EMP.matricula, EMP.nome, EMP.salario, EMP.numdepto, COUNT(PRO.codprojeto) AS Número_de_Projetos FROM EMPREGADO AS EMP INNER JOIN TRABALHA_EM AS TRA ON TRA.matricula = EMP.matricula INNER JOIN PROJETO AS PRO ON PRO.codprojeto = TRA.codprojeto GROUP BY EMP.matricula HAVING Número_de_Projetos > 1;

-- 20. Empregados e Departamento, Habilidade e Projeto (Multiple INNER JOINs) - Liste todos os empregados juntamente com o nome do departamento, a descrição da habilidade e o nome do projeto em que estão trabalhando.

SELECT * FROM EMPREGADO AS EM INNER JOIN DEPARTAMENTO AS DEP ON DEP.numdepto = EM.numdepto INNER JOIN EMPREGADO_HABILIDADE AS EH ON EH.matricula = EM.matricula INNER JOIN HABILIDADE as HA ON HA.codhabilidade = EH.codhabilidade INNER JOIN TRABALHA_EM AS TR ON TR.matricula = EM.matricula INNER JOIN PROJETO AS PR ON PR.codprojeto = TR.codprojeto;