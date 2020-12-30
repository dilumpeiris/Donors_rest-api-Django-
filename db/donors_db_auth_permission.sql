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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=105 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add cities',8,'add_cities'),(26,'Can change cities',8,'change_cities'),(27,'Can delete cities',8,'delete_cities'),(28,'Can view cities',8,'view_cities'),(29,'Can add districts',9,'add_districts'),(30,'Can change districts',9,'change_districts'),(31,'Can delete districts',9,'delete_districts'),(32,'Can view districts',9,'view_districts'),(33,'Can add donation history',12,'add_donationhistory'),(34,'Can change donation history',12,'change_donationhistory'),(35,'Can delete donation history',12,'delete_donationhistory'),(36,'Can view donation history',12,'view_donationhistory'),(37,'Can add donation modes',13,'add_donationmodes'),(38,'Can change donation modes',13,'change_donationmodes'),(39,'Can delete donation modes',13,'delete_donationmodes'),(40,'Can view donation modes',13,'view_donationmodes'),(41,'Can add donation reg',14,'add_donationreg'),(42,'Can change donation reg',14,'change_donationreg'),(43,'Can delete donation reg',14,'delete_donationreg'),(44,'Can view donation reg',14,'view_donationreg'),(45,'Can add donations',15,'add_donations'),(46,'Can change donations',15,'change_donations'),(47,'Can delete donations',15,'delete_donations'),(48,'Can view donations',15,'view_donations'),(49,'Can add donations donation modes',16,'add_donationsdonationmodes'),(50,'Can change donations donation modes',16,'change_donationsdonationmodes'),(51,'Can delete donations donation modes',16,'delete_donationsdonationmodes'),(52,'Can view donations donation modes',16,'view_donationsdonationmodes'),(53,'Can add events',17,'add_events'),(54,'Can change events',17,'change_events'),(55,'Can delete events',17,'delete_events'),(56,'Can view events',17,'view_events'),(57,'Can add event type',18,'add_eventtype'),(58,'Can change event type',18,'change_eventtype'),(59,'Can delete event type',18,'delete_eventtype'),(60,'Can view event type',18,'view_eventtype'),(61,'Can add organization',19,'add_organization'),(62,'Can change organization',19,'change_organization'),(63,'Can delete organization',19,'delete_organization'),(64,'Can view organization',19,'view_organization'),(65,'Can add priority',20,'add_priority'),(66,'Can change priority',20,'change_priority'),(67,'Can delete priority',20,'delete_priority'),(68,'Can view priority',20,'view_priority'),(69,'Can add requests',21,'add_requests'),(70,'Can change requests',21,'change_requests'),(71,'Can delete requests',21,'delete_requests'),(72,'Can view requests',21,'view_requests'),(73,'Can add subscription mode',22,'add_subscriptionmode'),(74,'Can change subscription mode',22,'change_subscriptionmode'),(75,'Can delete subscription mode',22,'delete_subscriptionmode'),(76,'Can view subscription mode',22,'view_subscriptionmode'),(77,'Can add user event subscription',23,'add_usereventsubscription'),(78,'Can change user event subscription',23,'change_usereventsubscription'),(79,'Can delete user event subscription',23,'delete_usereventsubscription'),(80,'Can view user event subscription',23,'view_usereventsubscription'),(81,'Can add users',10,'add_users'),(82,'Can change users',10,'change_users'),(83,'Can delete users',10,'delete_users'),(84,'Can view users',10,'view_users'),(85,'Can add venues',24,'add_venues'),(86,'Can change venues',24,'change_venues'),(87,'Can delete venues',24,'delete_venues'),(88,'Can view venues',24,'view_venues'),(89,'Can add blood type compatibility',7,'add_bloodtypecompatibility'),(90,'Can change blood type compatibility',7,'change_bloodtypecompatibility'),(91,'Can delete blood type compatibility',7,'delete_bloodtypecompatibility'),(92,'Can view blood type compatibility',7,'view_bloodtypecompatibility'),(93,'Can add blood types',11,'add_bloodtypes'),(94,'Can change blood types',11,'change_bloodtypes'),(95,'Can delete blood types',11,'delete_bloodtypes'),(96,'Can view blood types',11,'view_bloodtypes'),(97,'Can add Token',25,'add_token'),(98,'Can change Token',25,'change_token'),(99,'Can delete Token',25,'delete_token'),(100,'Can view Token',25,'view_token'),(101,'Can add token',26,'add_tokenproxy'),(102,'Can change token',26,'change_tokenproxy'),(103,'Can delete token',26,'delete_tokenproxy'),(104,'Can view token',26,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
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
