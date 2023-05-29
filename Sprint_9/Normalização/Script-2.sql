CREATE TABLE endereco ( 
	idEstado INT PRIMARY KEY,
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR(40),
	paisCliente VARCHAR(40),
	estadoVendedor VARCHAR(255)
);

CREATE TABLE cliente (
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(255),
	idEstado VARCHAR(255)	
);

CREATE TABLE carro (
	idCarro INT PRIMARY KEY,
	kmCarro INT,
	classiCarro VARCHAR(50),
	marcaCarro VARCHAR(80),
	modeloCarro VARCHAR(80),
	anoCarro INT,
	idCombustivel INT
);

CREATE TABLE vendedor (
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR(15),
	sexoVendedor SMALLINT,
	idEstado VARCHAR(100)
);

CREATE TABLE combustivel(
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR(20),
	idCarro INT
);

CREATE TABLE locacao (
	idLocacao INT PRIMARY KEY,
	idCarro INT,
	dataLocacao DATE,
	horaLocacao TIME,
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INT,
	idVendedor INT,
	idEstado VARCHAR(255)
	qtdDiaria INT,
	vlrDiaria INT
);


ALTER TABLE endereco
ADD CONSTRAINT fk_idCliente
FOREIGN KEY (idCliente) REFERENCES cliente(idCliente);

ALTER TABLE endereco
ADD CONSTRAINT fk_idVendedor
FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor);

ALTER TABLE cliente
ADD CONSTRAINT fk_estado
FOREIGN KEY (idEstado) REFERENCES endereco(idEstado);

ALTER TABLE carro
ADD CONSTRAINT fk_idCombustivel
FOREIGN KEY (idCombustivel) REFERENCES combustivel(idCombustivel);

ALTER TABLE vendedor
ADD CONSTRAINT fk_estado
FOREIGN KEY (idEstado) REFERENCES endereco(idEstado);

CREATE TABLE combustivel
ADD CONSTRAINT fk_idCarro 
FOREIGN KEY (idCarro) REFERENCES carro(idCarro);

ALTER TABLE locacao
ADD CONSTRAINT fk_estado
FOREIGN KEY (idEstado) REFERENCES endereco(idEstado);

ALTER TABLE locacao
ADD CONSTRAINT fk_idCliente 
FOREIGN KEY (idCliente) REFERENCES cliente(idCliente);

ALTER TABLE locacao
ADD CONSTRAINT fk_idVendedor 
FOREIGN KEY (idVendedor) REFERENCES vendedor(idVendedor);

CREATE INDEX idEstado
ON endereco (idEstado)

INSERT INTO endereco (idestado, cidadeCliente, estadoCliente, paisCliente, estadoVendedor) SELECT DISTINCT cidadeCliente, estadoCliente, paisCliente, estadoVendedor, (SELECT DISTINCT estadoCliente AS estado FROM tb_locacao tl UNION SELECT DISTINCT estadoVendedor AS estado FROM tb_locacao) AS idestado FROM tb_locacao

INSERT INTO cliente (idCliente, nomeCliente, idEstado) SELECT DISTINCT loc.idCliente, loc.nomeCliente, endereco.idEstado FROM tb_locacao as loc, endereco;

INSERT INTO carro (idCarro, kmCarro, classiCarro, modeloCarro, anoCarro, idCombustivel) SELECT DISTINCT idCarro, kmCarro, classiCarro, modeloCarro, anoCarro, idCombustivel FROM tb_locacao;

INSERT INTO vendedor (idVendedor, nomeVendedor, sexoVendedor, idEstado) SELECT DISTINCT loc.idVendedor, loc.nomeVendedor, loc.sexoVendedor, endereco.idEstado FROM tb_locacao as loc, endereco;

INSERT INTO combustivel (idCombustivel, tipoCombustivel, idCarro) SELECT DISTINCT idCombustivel, tipoCombustivel, idCarro FROM tb_locacao;

INSERT INTO locacao (idLocacao, dataLocacao, horaLocacao, dataEntrega, horaEntrega, idCliente, idVendedor, idEstado) SELECT DISTINCT loc.idLocacao, loc.dataLocacao, loc.horaLocacao, loc.dataEntrega, loc.horaEntrega, loc.idCliente, loc.idVendedor, endereco.idEstado FROM tb_locacao as loc, endereco;

	