-- Dimensão cliente
CREATE TABLE dim_cliente AS
SELECT DISTINCT
		c.idCliente,
		c.nomeCliente,
		e.idEstado,
		e.cidadeCliente,
		e.paisCliente
	FROM cliente as c, endereco as e;
	
-- Dimensão Tempo Locação
CREATE TABLE dim_tempoloc AS
SELECT DISTINCT
		l.idlocacao,
		l.dataLocacao,
		l.horaLocacao,
		c.idcliente,
		e.cidadecliente,
		v.idvendedor
	FROM locacao as l, endereco as e, cliente as c, vendedor as v;

-- Dimensão Tempo Entrega
CREATE TABLE dim_tempoent AS
SELECT DISTINCT
		l.idlocacao,
		l.dataentrega,
		l.horaentrega,
		c.idcliente,
		e.cidadecliente,
		v.idvendedor,
		ca.idcarro
	FROM locacao as l, endereco as e, cliente as c, vendedor as v, carro as ca;
			
					
-- Dimensão Vendedor
CREATE TABLE dim_vendedor AS
SELECT DISTINCT
		v.idVendedor,
		v.nomeVendedor,
		v.sexoVendedor,
		e.idestado,
		e.estadovendedor
	FROM vendedor as v, endereco as e;
	
-- Dimensão Carro
CREATE TABLE dim_carro AS
SELECT DISTINCT
		c.idCarro,
		c.kmCarro,
		c.classiCarro,
		c.marcaCarro,
		c.modeloCarro,
		c.anoCarro,
		co.idcombustivel,
		cl.idcliente,
		v.idvendedor,
		lo.idlocacao
	FROM carro as c, combustivel as co, cliente as cl, vendedor as v, locacao as lo;
		
	
-- Dimensão Diaria
CREATE TABLE dim_diaria AS
SELECT DISTINCT
		l.idlocacao,
		l.qtdDiaria,
		l.vlrDiaria,
		cl.idcliente,
		v.idvendedor
	FROM locacao as l, cliente as cl, vendedor as v;


-- Fato Vendas
CREATE VIEW fato_vendas AS
SELECT lo.idLocacao,
		cl.idCliente,
		ca.idCarro,
		co.idCombustivel,
		lo.qtdDiaria,
		lo.vlrDiaria,
		lo.dataLocacao,
		lo.dataEntrega,
		v.idVendedor
	FROM locacao as lo, cliente as cl, carro as ca, vendedor as v;

	

