-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: freshPrints
-- ------------------------------------------------------
-- Server version	8.0.24

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
-- Table structure for table `cargo`
--

DROP TABLE IF EXISTS `cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargo` (
  `itemName` varchar(255) NOT NULL,
  `itemQuantity` int DEFAULT NULL,
  `itemID` int NOT NULL AUTO_INCREMENT,
  `clientID` int NOT NULL,
  `projectID` int NOT NULL,
  PRIMARY KEY (`itemID`),
  KEY `clientID` (`clientID`),
  KEY `projectID` (`projectID`),
  CONSTRAINT `cargo_ibfk_1` FOREIGN KEY (`clientID`) REFERENCES `client` (`clientID`) ON DELETE CASCADE,
  CONSTRAINT `cargo_ibfk_2` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargo`
--

LOCK TABLES `cargo` WRITE;
/*!40000 ALTER TABLE `cargo` DISABLE KEYS */;
/*!40000 ALTER TABLE `cargo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `clientName` varchar(255) NOT NULL,
  `clientID` int NOT NULL AUTO_INCREMENT,
  `clientOrg` varchar(255) DEFAULT NULL,
  `clientNumber` varchar(255) DEFAULT NULL,
  `clientEmail` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`clientID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES ('Chirs Kriss',1,'Swiss Army','2129987655','chriskriss@swiss.com');
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `departmentName` varchar(255) NOT NULL,
  `departmentID` int NOT NULL AUTO_INCREMENT,
  `numEmployees` int DEFAULT NULL,
  PRIMARY KEY (`departmentID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('Coats',1,NULL),('Hats',2,NULL);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `employeeName` varchar(255) NOT NULL,
  `employeeID` int NOT NULL,
  `employeeSSN` int NOT NULL,
  `hireDate` date DEFAULT NULL,
  `dateOfBirth` date DEFAULT NULL,
  PRIMARY KEY (`employeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('Dan Man',3123,123123123,'2021-05-06','2000-01-09'),('Vector Victor',4789,123654789,'2021-05-08','1980-07-02');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manages`
--

DROP TABLE IF EXISTS `manages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manages` (
  `employeeID` int NOT NULL,
  `departmentID` int NOT NULL,
  KEY `employeeID` (`employeeID`),
  KEY `departmentID` (`departmentID`),
  CONSTRAINT `manages_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`employeeID`) ON DELETE CASCADE,
  CONSTRAINT `manages_ibfk_2` FOREIGN KEY (`departmentID`) REFERENCES `department` (`departmentID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manages`
--

LOCK TABLES `manages` WRITE;
/*!40000 ALTER TABLE `manages` DISABLE KEYS */;
INSERT INTO `manages` VALUES (3123,1);
/*!40000 ALTER TABLE `manages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `projectTitle` varchar(255) NOT NULL,
  `projectID` int NOT NULL AUTO_INCREMENT,
  `projectStatus` varchar(255) NOT NULL,
  `deliverByDate` date DEFAULT NULL,
  PRIMARY KEY (`projectID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `clientID` int NOT NULL,
  `projectID` int NOT NULL,
  KEY `clientID` (`clientID`),
  KEY `projectID` (`projectID`),
  CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`clientID`) REFERENCES `client` (`clientID`) ON DELETE CASCADE,
  CONSTRAINT `requests_ibfk_2` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shipment`
--

DROP TABLE IF EXISTS `shipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shipment` (
  `shipmentID` int NOT NULL AUTO_INCREMENT,
  `shippingCompany` varchar(255) DEFAULT NULL,
  `arriveByDate` date DEFAULT NULL,
  `itemCount` int DEFAULT NULL,
  `deliveryLocation` varchar(255) NOT NULL,
  PRIMARY KEY (`shipmentID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shipment`
--

LOCK TABLES `shipment` WRITE;
/*!40000 ALTER TABLE `shipment` DISABLE KEYS */;
/*!40000 ALTER TABLE `shipment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shippedby`
--

DROP TABLE IF EXISTS `shippedby`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shippedby` (
  `shipmentID` int NOT NULL,
  `projectID` int NOT NULL,
  KEY `shipmentID` (`shipmentID`),
  KEY `projectID` (`projectID`),
  CONSTRAINT `shippedby_ibfk_1` FOREIGN KEY (`shipmentID`) REFERENCES `shipment` (`shipmentID`) ON DELETE CASCADE,
  CONSTRAINT `shippedby_ibfk_2` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shippedby`
--

LOCK TABLES `shippedby` WRITE;
/*!40000 ALTER TABLE `shippedby` DISABLE KEYS */;
/*!40000 ALTER TABLE `shippedby` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `worksfor`
--

DROP TABLE IF EXISTS `worksfor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `worksfor` (
  `employeeID` int NOT NULL,
  `departmentID` int NOT NULL,
  KEY `employeeID` (`employeeID`),
  KEY `departmentID` (`departmentID`),
  CONSTRAINT `worksfor_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`employeeID`) ON DELETE CASCADE,
  CONSTRAINT `worksfor_ibfk_2` FOREIGN KEY (`departmentID`) REFERENCES `department` (`departmentID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `worksfor`
--

LOCK TABLES `worksfor` WRITE;
/*!40000 ALTER TABLE `worksfor` DISABLE KEYS */;
/*!40000 ALTER TABLE `worksfor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workson`
--

DROP TABLE IF EXISTS `workson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workson` (
  `departmentID` int NOT NULL,
  `projectID` int NOT NULL,
  KEY `departmentID` (`departmentID`),
  KEY `projectID` (`projectID`),
  CONSTRAINT `workson_ibfk_1` FOREIGN KEY (`departmentID`) REFERENCES `department` (`departmentID`),
  CONSTRAINT `workson_ibfk_2` FOREIGN KEY (`projectID`) REFERENCES `project` (`projectID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workson`
--

LOCK TABLES `workson` WRITE;
/*!40000 ALTER TABLE `workson` DISABLE KEYS */;
/*!40000 ALTER TABLE `workson` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-08 12:08:45
