DROP DATABASE IF EXISTS TRUONGHOC;

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE TRUONGHOC CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 

USE `TRUONGHOC`;

--
-- Table structure for table `loaihinh`
--

DROP TABLE IF EXISTS `loaihinh`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loaihinh` (
  `MALH` tinyint NOT NULL,
  `LOAIHINH` nvarchar(30) DEFAULT NULL,
 PRIMARY KEY (`malh`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
--
-- Table structure for table `loaitruong`
--

DROP TABLE IF EXISTS `loaitruong`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loaitruong` (
  `MALT` tinyint NOT NULL ,
  `LOAITRUONG` nvarchar(50) DEFAULT NULL,
 PRIMARY KEY (`malt`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `phongdt`
--

DROP TABLE IF EXISTS `phongdt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phongdt` (
  `MAPHONG` tinyint NOT NULL,
  `PHONGDT` nvarchar(50) DEFAULT NULL,
 PRIMARY KEY (`maphong`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `school`
--
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
  `MATRG` nvarchar(30) NOT NULL ,
  `TEN` nvarchar(200) DEFAULT NULL,
  `DCHI` nvarchar(200) DEFAULT NULL,
  `MALH` tinyint DEFAULT NULL,
  `MALT` tinyint DEFAULT NULL,
  `MAPHONG` tinyint DEFAULT NULL,
  `TENSO` nvarchar(30) NOT NULL,
 PRIMARY KEY (`matrg`), 
 FOREIGN KEY (`malh`) REFERENCES loaihinh (`malh`),
 FOREIGN KEY (`malt`) REFERENCES loaitruong (`malt`),
 FOREIGN KEY (`maphong`) REFERENCES phongdt (`maphong`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

