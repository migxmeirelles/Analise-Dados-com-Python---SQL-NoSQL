USE DW;

CREATE TABLE AGENCIAS (
	CD VARCHAR(1) NOT NULL,
	NM VARCHAR(15) NULL,
	SG VARCHAR(15) NULL,
	UF VARCHAR(2) NULL
);

INSERT INTO AGENCIAS (CD, NM, SG, UF)
VALUES
('1', 'PORTO ALEGRE', 'AGPOA', 'RS'),
('2', 'FLORIANOPOLIS', 'AGFLO', 'SC'),
('3', 'CURITIBA', 'AGCUR', 'PR');

SELECT * FROM AGENCIAS;