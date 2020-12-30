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
-- Table structure for table `donation_history`
--

DROP TABLE IF EXISTS `donation_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donation_history` (
  `donation_history_item_id` int NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `donation_id` int NOT NULL,
  `venue_id` int NOT NULL,
  `donation_date` date NOT NULL,
  `donation_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `verification_user_id` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`donation_history_item_id`,`user_id`,`donation_id`,`venue_id`),
  KEY `fk_donation_history_users1_idx` (`user_id`),
  KEY `fk_donation_history_users2_idx` (`verification_user_id`),
  KEY `fk_donation_history_donations_idx` (`donation_id`),
  KEY `fk_donation_history_venues1_idx` (`venue_id`),
  CONSTRAINT `fk_donation_history_donations1` FOREIGN KEY (`donation_id`) REFERENCES `donations` (`donation_id`),
  CONSTRAINT `fk_donation_history_users2` FOREIGN KEY (`verification_user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `fk_donation_history_venues1` FOREIGN KEY (`venue_id`) REFERENCES `venues` (`venue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donation_history`
--

LOCK TABLES `donation_history` WRITE;
/*!40000 ALTER TABLE `donation_history` DISABLE KEYS */;
INSERT INTO `donation_history` VALUES (6,1,1,1,'2020-12-15','2020-12-14 22:07:25',1);
/*!40000 ALTER TABLE `donation_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-30 16:48:34
