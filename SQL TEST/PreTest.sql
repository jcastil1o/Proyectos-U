Create Schema `sql`;
Create Table `sql`.`prueba1`
(
	`codigo` INT NOT NULL,
    `Nombre` VARCHAR(100) NULL,
    `Altura` VARCHAR(100) NULL,
    PRIMARY KEY (`codigo`)
);
SELECT * FROM sql.prueba1;

INSERT INTO `sql`.`prueba1` (`codigo`, `Nombre`, `Altura`) VALUES (1, 'Jonathan', 160);
INSERT INTO `sql`.`prueba1` (`codigo`, `Nombre`, `Altura`) VALUES (2, 'Camilo', 173);
INSERT INTO `sql`.`prueba1` (`codigo`, `Nombre`, `Altura`) VALUES (3, 'Iza', 150);

Create Table `sql`.`peso`
(
	`codigo` INT NOT NULL,
    `Nombre` VARCHAR(100) NULL,
    `Peso` VARCHAR(100) NULL,
    FOREIGN KEY (`codigo`) REFERENCES prueba1 (`codigo`)
);
SELECT * FROM sql.peso;
INSERT INTO `sql`.`peso` (`codigo`, `Nombre`, `Peso`) VALUES (1, 'Jonathan', 156);
INSERT INTO `sql`.`peso` (`codigo`, `Nombre`, `Peso`) VALUES (2, 'Camilo', 175);
INSERT INTO `sql`.`peso` (`codigo`, `Nombre`, `Peso`) VALUES (3, 'Iza', 100);

SELECT p.codigo, p.Nombre, p.Altura, peso.peso FROM `sql`.`prueba1` p INNER JOIN `sql`.`peso` ON peso.codigo = p.codigo WHERE peso.Peso >= 150 AND peso.Peso <= 200;
SELECT p.codigo, p.Nombre, p.Altura, peso.peso FROM `sql`.`prueba1` p LEFT JOIN `sql`.`peso` ON peso.codigo = p.codigo WHERE peso.Peso >= 150 AND peso.Peso <= 200;
SELECT p.codigo, p.Nombre, p.Altura, peso.peso FROM `sql`.`prueba1` p RIGHT JOIN `sql`.`peso` ON peso.codigo = p.codigo WHERE peso.Peso >= 150 AND peso.Peso <= 200;