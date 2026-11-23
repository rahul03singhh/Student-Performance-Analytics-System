-- MySQL dump 10.13  Distrib 8.0.45, for macos15 (arm64)
--
-- Host: 127.0.0.1    Database: your_new_database_name
-- ------------------------------------------------------
-- Server version	9.7.1

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ 'a7de7e88-a877-11f1-9061-3573a1ce2651:1-98';

--
-- Table structure for table `assessments`
--

DROP TABLE IF EXISTS `assessments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assessments` (
  `assessment_id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(20) DEFAULT NULL,
  `subject` varchar(30) DEFAULT NULL,
  `marks_obtained` int DEFAULT NULL,
  `max_marks` int DEFAULT NULL,
  PRIMARY KEY (`assessment_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `assessments_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assessments`
--

LOCK TABLES `assessments` WRITE;
/*!40000 ALTER TABLE `assessments` DISABLE KEYS */;
INSERT INTO `assessments` VALUES (1,'S101','Database Systems',42,50),(2,'S101','Data Structures',38,50),(3,'S102','Database Systems',45,50),(4,'S102','Data Structures',40,50),(5,'S103','Database Systems',25,50),(6,'S103','Data Structures',18,50),(7,'S104','Database Systems',35,50),(8,'S104','Data Structures',30,50),(9,'S105','Database Systems',44,50),(10,'S105','Data Structures',41,50),(11,'S106','Database Systems',15,50),(12,'S106','Data Structures',12,50),(13,'S107','Database Systems',39,50),(14,'S107','Data Structures',37,50),(15,'S108','Database Systems',40,50),(16,'S108','Data Structures',42,50),(17,'S109','Database Systems',20,50),(18,'S109','Data Structures',22,50),(19,'S110','Database Systems',48,50),(20,'S110','Data Structures',46,50);
/*!40000 ALTER TABLE `assessments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `attendance_id` int NOT NULL AUTO_INCREMENT,
  `student_id` varchar(20) DEFAULT NULL,
  `subject` varchar(30) DEFAULT NULL,
  `attended_classes` int DEFAULT NULL,
  `total_classes` int DEFAULT NULL,
  PRIMARY KEY (`attendance_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (1,'S101','Database Systems',18,20),(2,'S101','Data Structures',19,20),(3,'S102','Database Systems',20,20),(4,'S102','Data Structures',19,20),(5,'S103','Database Systems',10,20),(6,'S103','Data Structures',11,20),(7,'S104','Database Systems',16,20),(8,'S104','Data Structures',17,20),(9,'S105','Database Systems',19,20),(10,'S105','Data Structures',18,20),(11,'S106','Database Systems',12,20),(12,'S106','Data Structures',10,20),(13,'S107','Database Systems',17,20),(14,'S107','Data Structures',18,20),(15,'S108','Database Systems',18,20),(16,'S108','Data Structures',19,20),(17,'S109','Database Systems',14,20),(18,'S109','Data Structures',15,20),(19,'S110','Database Systems',20,20),(20,'S110','Data Structures',20,20);
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` varchar(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `department` varchar(30) DEFAULT NULL,
  `semester` int DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES ('S101','Rahul Singh','Computer Science',4,'rahul@mail.com'),('S102','Bhoomika Sharma','Computer Science',4,'bhoomika@mail.com'),('S103','Aman Verma','IT',4,'aman@mail.com'),('S104','Priya Gupta','Computer Science',2,'priya@mail.com'),('S105','Rohit Kumar','Electronics',6,'rohit@mail.com'),('S106','Neha Singh','IT',2,'neha@mail.com'),('S107','Amit Kumar','Computer Science',4,'amit@mail.com'),('S108','Sneha Sharma','Mechanical',6,'sneha@mail.com'),('S109','Vikas Yadav','Civil',8,'vikas@mail.com'),('S110','Pooja Verma','Computer Science',4,'pooja@mail.com');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-18 19:18:50
