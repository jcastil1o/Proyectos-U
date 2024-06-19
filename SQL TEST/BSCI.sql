Create Schema `bsci`;

Create table `bsci`.`APPX_employee`
(
	`id` INT NOT NULL,
    `firstname` VARCHAR (100) NULL,
    `lastname` VARCHAR (100) NULL,
    `department_id` VARCHAR (100) NULL,
    `salary` VARCHAR (100) NULL,
    `educationlevel_id` VARCHAR (100) NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO `bsci`.`APPx_employee` (`id`, `firstname`, `lastname`, `department_id`, `salary`, `educationlevel_id`) VALUES (1, 'Jonathan', 'Castillo', 'QA', 5000, 'Estudiante');
INSERT INTO `bsci`.`APPx_employee` (`id`, `firstname`, `lastname`, `department_id`, `salary`, `educationlevel_id`) VALUES (2, 'Juan', 'Perez', 'QA', 6000, 'Estudiante');
INSERT INTO `bsci`.`APPx_employee` (`id`, `firstname`, `lastname`, `department_id`, `salary`, `educationlevel_id`) VALUES (3, 'Luis', 'Lopez', 'Jr', 10000, 'Graduado');
INSERT INTO `bsci`.`APPx_employee` (`id`, `firstname`, `lastname`, `department_id`, `salary`, `educationlevel_id`) VALUES (4, 'Diego', 'Reyes', 'Middle', 70000, 'Graduado');

SELECT * FROM bsci.APPX_employee WHERE id = 3;

create table `bsci`.`APPX_departmet`
(
	`id` INT NOT NULL,
    `department_name` VARCHAR (100) NULL,
    `department_city` VARCHAR (100) NULL,
    FOREIGN KEY  (`id`) REFERENCES APPX_employee (`id`)
);

INSERT INTO `bsci`.`APPX_departmet` (`id`, `department_name`, `department_city`) VALUES (1, 'QA', 'Guatemala');
INSERT INTO `bsci`.`APPX_departmet` (`id`, `department_name`, `department_city`) VALUES (2, 'QA', 'El Salvador');
INSERT INTO `bsci`.`APPX_departmet` (`id`, `department_name`, `department_city`) VALUES (3, 'Jr', 'Mexico');

SELECT e.id, e.firstname, e.lastname, e.salary FROM bsci.APPX_employee AS e WHERE e.salary >= 50000 AND e.salary <= 100000 ORDER BY e.firstname ASC;