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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` VALUES (3,'Pagos',2),(4,'Transporte',2),(5,'Integrantes',1),(7,'Compras',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `descripciones`
--

LOCK TABLES `descripciones` WRITE;
/*!40000 ALTER TABLE `descripciones` DISABLE KEYS */;
INSERT INTO `descripciones` VALUES (1,'Arriendo',1000000,3),(2,'SOAT sin moto',400000,3),(3,'Pasajes',180000,4),(23,'Lina',5000,5),(24,'Andrea',5000,5),(25,'Andrés',0,5),(26,'James',5000,5),(30,'Arroz',15000,7),(31,'Otros',20000,4);
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
  `saldo` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `UQ_usuarios_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Yésica Andrea','Lugo López','andrelugolopez@gmail.com','1234',1200000),(2,'Lina María','Sanabria Páramo','linamsp19@gmail.com','1234',1500000),(3,'John James','Valencia Cardona','jhonjamesillo@gmail.com','1234',0),(4,'Andrés Felipe','Sierra Rojas','andressierra7@gmail.com','1234',0);
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

-- Dump completed on 2021-06-28 16:54:55
