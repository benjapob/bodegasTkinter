-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.25-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para proyectoinventario
CREATE DATABASE IF NOT EXISTS `proyectoinventario` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `proyectoinventario`;

-- Volcando estructura para tabla proyectoinventario.bodega
CREATE TABLE IF NOT EXISTS `bodega` (
  `idBodega` int(11) NOT NULL AUTO_INCREMENT,
  `capacidadBodega` int(11) DEFAULT NULL,
  `numeroBodega` int(11) NOT NULL,
  `idTrabajador` int(11) NOT NULL,
  PRIMARY KEY (`idBodega`),
  UNIQUE KEY `numeroBodega` (`numeroBodega`),
  KEY `fkBodega1` (`idTrabajador`),
  CONSTRAINT `fkBodega1` FOREIGN KEY (`idTrabajador`) REFERENCES `trabajador` (`idTrabajador`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Volcando estructura para tabla proyectoinventario.categoria
CREATE TABLE IF NOT EXISTS `categoria` (
  `idCategoria` int(11) NOT NULL AUTO_INCREMENT,
  `nombreCategoria` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla proyectoinventario.categoria: ~3 rows (aproximadamente)
INSERT INTO `categoria` (`idCategoria`, `nombreCategoria`) VALUES
	(1, 'LIBRO'),
	(2, 'REVISTA'),
	(3, 'ENCICLOPEDIA');

-- Volcando estructura para tabla proyectoinventario.detallemovimiento
CREATE TABLE IF NOT EXISTS `detallemovimiento` (
  `idDetalle` int(11) NOT NULL AUTO_INCREMENT,
  `cantidadProducto` int(11) DEFAULT NULL,
  `idProducto` int(11) NOT NULL,
  `idRegistro` int(11) NOT NULL,
  PRIMARY KEY (`idDetalle`),
  KEY `fkDetalle1` (`idProducto`),
  KEY `fkDetalle2` (`idRegistro`),
  CONSTRAINT `fkDetalle1` FOREIGN KEY (`idProducto`) REFERENCES `producto` (`idProducto`),
  CONSTRAINT `fkDetalle2` FOREIGN KEY (`idRegistro`) REFERENCES `registromovimiento` (`idRegistro`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Volcando estructura para tabla proyectoinventario.editorial
CREATE TABLE IF NOT EXISTS `editorial` (
  `idEditorial` int(11) NOT NULL AUTO_INCREMENT,
  `numeroEditorial` int(11) NOT NULL,
  `nombreEditorial` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idEditorial`),
  UNIQUE KEY `numeroEditorial` (`numeroEditorial`),
  UNIQUE KEY `nombreEditorial` (`nombreEditorial`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- Volcando estructura para tabla proyectoinventario.producto
CREATE TABLE IF NOT EXISTS `producto` (
  `idProducto` int(11) NOT NULL AUTO_INCREMENT,
  `numeroProducto` int(11) NOT NULL,
  `nombreProducto` varchar(50) NOT NULL,
  `descripcionProducto` varchar(200) DEFAULT NULL,
  `autorProducto` varchar(100) DEFAULT NULL,
  `idEditorial` int(11) NOT NULL,
  `idCategoria` int(11) NOT NULL,
  PRIMARY KEY (`idProducto`),
  UNIQUE KEY `numeroProducto` (`numeroProducto`),
  UNIQUE KEY `nombreProducto` (`nombreProducto`),
  KEY `fkProducto1` (`idEditorial`),
  KEY `fkProducto2` (`idCategoria`),
  CONSTRAINT `fkProducto1` FOREIGN KEY (`idEditorial`) REFERENCES `editorial` (`idEditorial`),
  CONSTRAINT `fkProducto2` FOREIGN KEY (`idCategoria`) REFERENCES `categoria` (`idCategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;


-- Volcando estructura para tabla proyectoinventario.registromovimiento
CREATE TABLE IF NOT EXISTS `registromovimiento` (
  `idRegistro` int(11) NOT NULL AUTO_INCREMENT,
  `fechaCreacion` date DEFAULT current_timestamp(),
  `tiendaDestino` varchar(100) DEFAULT NULL,
  `proveedor` varchar(100) DEFAULT NULL,
  `bodegaOrigen` varchar(100) DEFAULT NULL,
  `idTipo` int(11) NOT NULL,
  `idBodega` int(11) NOT NULL,
  `idTrabajador` int(11) NOT NULL,
  PRIMARY KEY (`idRegistro`),
  KEY `fkRegistro1` (`idTipo`),
  KEY `fkRegistro2` (`idBodega`),
  KEY `fkRegistro3` (`idTrabajador`),
  CONSTRAINT `fkRegistro1` FOREIGN KEY (`idTipo`) REFERENCES `tipomovimiento` (`idTipo`),
  CONSTRAINT `fkRegistro2` FOREIGN KEY (`idBodega`) REFERENCES `bodega` (`idBodega`),
  CONSTRAINT `fkRegistro3` FOREIGN KEY (`idTrabajador`) REFERENCES `trabajador` (`idTrabajador`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Volcando estructura para tabla proyectoinventario.rol
CREATE TABLE IF NOT EXISTS `rol` (
  `idRol` int(11) NOT NULL AUTO_INCREMENT,
  `nombreRol` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla proyectoinventario.rol: ~3 rows (aproximadamente)
INSERT INTO `rol` (`idRol`, `nombreRol`) VALUES
	(1, 'ADMINISTRADOR'),
	(2, 'JEFE DE BODEGA'),
	(3, 'BODEGUERO');

-- Volcando estructura para tabla proyectoinventario.tipomovimiento
CREATE TABLE IF NOT EXISTS `tipomovimiento` (
  `idTipo` int(11) NOT NULL AUTO_INCREMENT,
  `nombreTipo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idTipo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla proyectoinventario.tipomovimiento: ~3 rows (aproximadamente)
INSERT INTO `tipomovimiento` (`idTipo`, `nombreTipo`) VALUES
	(1, 'ENTRADA'),
	(2, 'SALIDA'),
	(3, 'TRASLADO');

-- Volcando estructura para tabla proyectoinventario.trabajador
CREATE TABLE IF NOT EXISTS `trabajador` (
  `idTrabajador` int(11) NOT NULL AUTO_INCREMENT,
  `nombreTrabajador` varchar(50) DEFAULT NULL,
  `apellidoTrabajador` varchar(50) DEFAULT NULL,
  `rutTrabajador` varchar(10) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  `idRol` int(11) NOT NULL,
  `terminos` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`idTrabajador`),
  UNIQUE KEY `rutTrabajador` (`rutTrabajador`),
  UNIQUE KEY `correo` (`correo`),
  KEY `fkTrabajador1` (`idRol`),
  CONSTRAINT `fkTrabajador1` FOREIGN KEY (`idRol`) REFERENCES `rol` (`idRol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla proyectoinventario.trabajador: ~3 rows (aproximadamente)
INSERT INTO `trabajador` (`idTrabajador`, `nombreTrabajador`, `apellidoTrabajador`, `rutTrabajador`, `correo`, `contraseña`, `idRol`, `terminos`) VALUES
	(1, 'BENJAMIN', 'POBLETE', '1-1', 'CORREO@CORREO.COM', '81DC9BDB52D04DC20036DBD8313ED055', 2, 1),
	(2, 'JUAN', 'SOTO', '1-2', 'CORREO2@CORREO.COM', '81DC9BDB52D04DC20036DBD8313ED055', 2, 0),
	(3, 'JOSE', 'SOTO', '1-3', 'CORREO3@CORREO.COM', '81DC9BDB52D04DC20036DBD8313ED055', 3, 1);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
