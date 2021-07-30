-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: app_finanzas
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS app_finanzas;
USE app_finanzas;
--
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` char(60) DEFAULT NULL,
  `idusuario` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `categorias_ibfk_1` (`idusuario`),
  CONSTRAINT `categorias_ibfk_1` FOREIGN KEY (`idusuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (3,'Pagos',2),(4,'Transporte',2),(5,'Integrantes',1),(7,'Compras',1),(9,'Mercado',3),(11,'Gastos',3);
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `descripciones`
--

DROP TABLE IF EXISTS `descripciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `descripciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `detalle` char(60) DEFAULT NULL,
  `valor` float DEFAULT NULL,
  `idcategoria` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `descripciones_ibfk_1` (`idcategoria`),
  CONSTRAINT `descripciones_ibfk_1` FOREIGN KEY (`idcategoria`) REFERENCES `categorias` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `descripciones`
--

LOCK TABLES `descripciones` WRITE;
/*!40000 ALTER TABLE `descripciones` DISABLE KEYS */;
INSERT INTO `descripciones` VALUES (1,'Arriendo',1000000,3),(2,'SOAT sin moto',400000,3),(3,'Pasajes',180000,4),(23,'Lina',5000,5),(24,'Andrea',5000,5),(25,'Andrés',0,5),(26,'James',5000,5),(30,'Arroz',15000,7),(31,'Otros',20000,4),(33,'Arroz',12000,9),(34,'Papa',25000,9),(36,'Control',120000,11);
/*!40000 ALTER TABLE `descripciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres` char(50) DEFAULT NULL,
  `apellidos` char(50) DEFAULT NULL,
  `email` char(30) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `saldo` float DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `UQ_usuarios_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Yésica Andrea','Lugo López','andrelugolopez@gmail.com','$2b$12$HBCBR6zhrzlF5YGzPn4zzuQutP9dXpaDJUmLT8rJOdECMETfkfkI.',1200000),(2,'Lina María','Sanabria Páramo','linamsp19@gmail.com','$2b$12$9RDMehFkO9Hku9lJoxPrTuqpHrGvudCbEJVEtDgLdP3lRYwxdFeZe',1675000),(3,'John James','Valencia Cardona','jhonjamesillo@gmail.com','$2b$12$WW3qWHv7op0Uug5uSAFZB.pv9rD1FgRpdwqYwxjgfhMVJ1/dOyQHG',1250000),(4,'Andrés Felipe','Sierra Rojas','andressierrarojas7@gmail.com','$2b$12$DGfTbBoU77B11rSWPp09T.O7753XJk8yl7VYk5xQK07HA8QU9P5V6',0),(9,'Antonio','Banderas','test@email.com','$2b$12$99vYM0A19XJ5Cw0l3hcqsuzybfAVZPelXutMIe6UlG8S5sbfxPMK2',0);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-30 14:14:35
