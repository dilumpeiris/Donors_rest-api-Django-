-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: localhost    Database: donors_db
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$H0c1OqgjYaoL$Rh3YE93HWRLyhkioy7l7f+DFHAKWHzsyWtkpx5IR+UQ=','2020-12-26 12:00:11.158366',1,'root','','','dilum.peiris@icloud.com',1,1,'2020-12-13 03:49:23.873606'),(2,'pbkdf2_sha256$216000$yIv9VfyEaeui$gXQEPYTQKTUnz1nGQKwoMRTwsldTVcddNrgK4K2dAZs=','2020-12-25 05:34:17.688281',0,'admin','','','dilum.peiris2@icloud.com',0,1,'2020-12-25 05:34:17.510728'),(3,'pbkdf2_sha256$216000$gIYRwPXV8Jcd$Dc49QQ7xhjavS9LhmQiV9uH56uOgDAW0GS+YhiLvwYE=',NULL,0,'john','','','lennon@thebeatles.com',0,1,'2020-12-25 06:07:16.497531'),(6,'pbkdf2_sha256$216000$4AcxWy8reGkS$1qIbN4e4CWzdF6pLzIfpFNhMrqNwxRkkNx0Iq9m0rfo=',NULL,0,'jooohn','','','lennon@thebeooatles.com',0,1,'2020-12-25 06:13:48.735488'),(11,'pbkdf2_sha256$216000$lwX22QG6oyt6$x0Uo82h4lEE4xQ0tvTuhhybYv2w/HBw/qnNJ1ayOBUo=',NULL,0,'Rick','','','dilump.Rick@icloud.com',0,1,'2020-12-26 06:16:24.665539'),(12,'0768005064','2020-12-26 07:06:41.000000',1,'marty','marty','peiris','dilum.peiris@icloud.com',1,1,'2020-12-26 07:07:05.000000'),(13,'pbkdf2_sha256$216000$6BmJklk27SPV$9OAhHpmJiW+LhAzwkkbdmbHz6IqGih7YT9/4hAc9eJg=',NULL,0,'morty','','','dilum.peiris@icloud.com',0,1,'2020-12-26 07:52:10.791119'),(17,'Blah Blah Blah Blah',NULL,0,'Delum','Dilum','Peiris','Delum.prasanga@icloud.com',0,1,'2020-12-27 01:52:17.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-30 16:48:32
