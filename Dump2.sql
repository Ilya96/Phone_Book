-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: phone_book
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contact`
--

DROP TABLE IF EXISTS `contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_key_idx` (`user_id`),
  CONSTRAINT `user_key` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact`
--

LOCK TABLES `contact` WRITE;
/*!40000 ALTER TABLE `contact` DISABLE KEYS */;
INSERT INTO `contact` VALUES (1,1,'Сергiй','9651234567','1994-12-12'),(3,2,'Петя','9654848484','1997-01-01'),(4,2,'Петя','9653838383','2000-01-01'),(6,2,'Аня','5858305830','2000-01-01'),(7,2,'Аня','9653838383','2000-01-01'),(8,2,'Пет','9653838383','2000-01-01'),(9,3,'Петя','9653838383','2000-01-01'),(10,3,'Ваня','9653838389','2000-01-01'),(11,1,'Петя','9653838383','2000-01-01'),(13,1,'Клим','9653838390','1980-01-01'),(14,1,'Максим','2829390403','1996-08-05'),(15,4,'Артём','9653838067','1996-03-01'),(16,1,'Ёрик','9653838383','2002-01-01'),(17,1,'Ы','4545454545','2005-01-01'),(18,1,'Jack','9659292929','1994-01-01'),(19,15,'Петя','9653838383','2000-01-01'),(20,15,'Федя','9653838383','2000-01-01'),(21,1,'Вася','9653838383','1997-01-01'),(23,1,'Вася','9653838386','2000-01-01'),(24,4,'Аня','9653838383','1998-01-01'),(27,1,'Шынгыз','9653838383','2000-01-01'),(28,1,'Ыз','9653838383','2000-01-01'),(29,1,'John Davidson','9653838383','2000-01-01'),(34,1,'Энтони','9653838383','2000-01-01'),(38,1,'Антон','9653838383','2000-01-01'),(39,1,'Боря','9653838383','2000-01-01'),(40,1,'Антонио','9653838383','2000-01-01'),(41,1,'Бенито','9653838383','2000-01-01'),(43,1,'Игорь','9653838383','2000-01-01'),(44,1,'Егор','9653838383','2000-01-01'),(45,1,'Шынгыз','9653838383','1996-01-16'),(46,1,'Батырхан','9653838383','1996-01-17'),(47,1,'Толя','9653838383','1996-01-15'),(48,1,'Аня','9653838383','2000-01-23'),(49,1,'Таня','9653838383','2000-01-24');
/*!40000 ALTER TABLE `contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `remember`
--

DROP TABLE IF EXISTS `remember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `remember` (
  `login` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `remember`
--

LOCK TABLES `remember` WRITE;
/*!40000 ALTER TABLE `remember` DISABLE KEYS */;
INSERT INTO `remember` VALUES ('Петя','123');
/*!40000 ALTER TABLE `remember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `birth_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Петя','123','Petya@gmail.com','1997-12-31'),(2,'Вася','234','Vasya@gmail.com','1996-02-28'),(3,'Аня','345','Anya@gmail.com','1995-04-10'),(4,'Илья','456','Ilya@gmail.com','1996-05-03'),(6,'Серёжа','567','Serj@gmail.com','1992-04-04'),(7,'Андрей','678','Андрей@mail.ru','1998-01-13'),(9,'Настя','789','Nastya@yandex.ru','1999-01-03'),(10,'Катя','890','Каtya@yandex.ru','1998-01-01'),(11,'Стас','901','Stas@gmail.com','1996-01-01'),(12,'Толя','012','Tolya@mail.ru','1998-05-03'),(15,'Коля','123','Kolya@mail.ru','1997-01-01');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-12  0:06:27
