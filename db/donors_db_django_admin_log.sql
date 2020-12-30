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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-12-13 05:09:05.350394','1','Districts object (1)',1,'[{\"added\": {}}]',9,1),(2,'2020-12-13 05:09:20.400840','1','Cities object (1)',1,'[{\"added\": {}}]',8,1),(3,'2020-12-13 05:11:07.862722','1','BloodTypes object (1)',1,'[{\"added\": {}}]',11,1),(4,'2020-12-13 05:11:15.627726','1','Users object (1)',1,'[{\"added\": {}}]',10,1),(5,'2020-12-14 04:13:28.874490','2','Districts object (2)',1,'[{\"added\": {}}]',9,1),(6,'2020-12-15 03:34:18.046635','1','Blood',1,'[{\"added\": {}}]',15,1),(7,'2020-12-15 03:37:09.543878','1','Panadura Hall',1,'[{\"added\": {}}]',24,1),(8,'2020-12-15 03:37:20.449169','1','Panadura Hall',2,'[]',24,1),(9,'2020-12-15 03:42:13.118219','6','DonationHistory object (6)',1,'[{\"added\": {}}]',12,1),(10,'2020-12-15 03:50:49.027209','1','DilumPeirisBlood',1,'[{\"added\": {}}]',14,1),(11,'2020-12-16 07:21:00.866182','1','Blood',1,'[{\"added\": {}}]',13,1),(12,'2020-12-16 07:21:15.204021','2','I dont Know',1,'[{\"added\": {}}]',13,1),(13,'2020-12-16 07:41:23.818062','1','This is a Priority',1,'[{\"added\": {}}]',20,1),(14,'2020-12-16 07:41:28.407819','1','request1',1,'[{\"added\": {}}]',21,1),(15,'2020-12-16 07:41:38.278819','1','request1',2,'[]',21,1),(16,'2020-12-16 07:50:53.721630','1','Money',2,'[{\"changed\": {\"fields\": [\"Donation type\"]}}]',15,1),(17,'2020-12-16 07:57:42.922615','2','Money - I dont Know',1,'[{\"added\": {}}]',16,1),(18,'2020-12-16 07:58:35.302762','3','Blood',1,'[{\"added\": {}}]',15,1),(19,'2020-12-16 07:58:41.013244','3','Blood - Blood',1,'[{\"added\": {}}]',16,1),(20,'2020-12-16 08:01:08.562493','4','Yeah I know',1,'[{\"added\": {}}]',13,1),(21,'2020-12-16 08:02:11.622975','4','Test',1,'[{\"added\": {}}]',15,1),(22,'2020-12-16 08:04:09.566145','5','test2',1,'[{\"added\": {}}]',15,1),(23,'2020-12-16 08:05:16.762458','6','test3',1,'[{\"added\": {}}]',15,1),(24,'2020-12-16 08:09:58.075200','1','Donation Camp',1,'[{\"added\": {}}]',18,1),(25,'2020-12-16 08:10:22.951305','1','Blah Blah',1,'[{\"added\": {}}]',19,1),(26,'2020-12-16 08:10:25.511231','1','Blood Camp',1,'[{\"added\": {}}]',17,1),(28,'2020-12-16 09:02:05.110730','7','Blood',1,'[{\"added\": {}}]',15,1),(29,'2020-12-16 09:02:21.975059','8','Blah B;ah',1,'[{\"added\": {}}]',15,1),(30,'2020-12-16 09:03:17.441557','5','Priority',1,'[{\"added\": {}}]',20,1),(31,'2020-12-16 09:10:10.423563','1','Daily',1,'[{\"added\": {}}]',22,1),(32,'2020-12-16 09:18:57.342232','2','DilumPeiris - Donation Camp',1,'[{\"added\": {}}]',23,1),(33,'2020-12-16 09:41:04.396232','1','A+ - A+',1,'[{\"added\": {}}]',7,1),(34,'2020-12-16 10:16:57.452812','1','A+',3,'',11,1),(35,'2020-12-16 10:17:12.716282','1','A+',3,'',11,1),(36,'2020-12-16 10:17:16.076141','1','A+',3,'',11,1),(38,'2020-12-16 10:17:47.443516','1','Panadura',3,'',8,1),(39,'2020-12-16 10:19:36.946327','1','Blood Camp',3,'',17,1),(40,'2020-12-25 06:13:07.337014','5','jooohn',3,'',27,1),(41,'2020-12-26 06:05:10.013413','9','DilumPrasanga',2,'[{\"changed\": {\"fields\": [\"Last login\", \"First name\", \"Last name\", \"Is staff\"]}}]',27,1),(42,'2020-12-26 06:06:12.691158','9','DilumPrasanga',2,'[{\"changed\": {\"fields\": [\"Is superuser\"]}}]',27,1),(46,'2020-12-27 01:48:11.856834','14','ec5a3b02775e7f2c6f2b240c537105914c897b78',3,'',26,1),(47,'2020-12-27 01:48:22.640235','14','Prasanga',3,'',27,1),(48,'2020-12-27 01:57:27.104169','17','Dilum',2,'[{\"changed\": {\"fields\": [\"Username\", \"First name\", \"Last name\"]}}]',27,1),(49,'2020-12-27 01:59:24.340313','17','Balum',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',27,1),(50,'2020-12-27 02:00:25.044093','17','Dilum',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',27,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-30 16:48:31
