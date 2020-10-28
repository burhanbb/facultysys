-- MySQL dump 10.10
--
-- Host: localhost    Database: facultysys
-- ------------------------------------------------------
-- Server version	5.0.24-community-nt

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
CREATE TABLE `auth_user` (
  `username` varchar(100) default NULL,
  `password` varchar(100) default NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--


/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
LOCK TABLES `auth_user` WRITE;
INSERT INTO `auth_user` VALUES ('burhan','123');
UNLOCK TABLES;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;

--
-- Table structure for table `facultydb`
--

DROP TABLE IF EXISTS `facultydb`;
CREATE TABLE `facultydb` (
  `regid` int(10) NOT NULL auto_increment,
  `first_name` varchar(50) NOT NULL,
  `second_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `role` varchar(20) NOT NULL,
  `myattend` int(11) NOT NULL,
  `totalattend` int(10) NOT NULL,
  `leaveapp` varchar(10) NOT NULL,
  `salary` int(10) NOT NULL,
  `experience` varchar(20) NOT NULL,
  PRIMARY KEY  (`regid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydb`
--


/*!40000 ALTER TABLE `facultydb` DISABLE KEYS */;
LOCK TABLES `facultydb` WRITE;
INSERT INTO `facultydb` VALUES (1,'Burhan','Bootwala','burhanuddinboot.am@gmail.com','1234','7869420882','Hasanji Nagar,Rau','male','admin',20,20,'no',23328,'4 Years'),(2,'Burhanuddin','Bootwala','burhanuddinbootwala6864@gmail.com','123','7974265551','Hasanji Nagar,Rau','male','manager',20,20,'no',1000000,'5 Months'),(3,'Burhanuddin','Bootwala','en18cs301071@medicaps.ac.in','123','8770488131','Hasanji Nagar,Rau','male','user',20,20,'yes',10000,'22 Months'),(6,'deep','Singh','deepkuldeep8777@gmail.com','123','8770488131','Indore','male','user',90,98,'yes',9000,'6 Years'),(7,'harsh','Narang','harshein02@gmail.com','12345','6266570610','kalindi midtown','female','user',15,20,'yes',25080,'5 Months'),(8,'isshita','trivedi','isshita2710@gmail.com','123','6266973037','Satna','female','manager',17,20,'no',30000,'1 Year'),(9,'Jayant','Parmar','parmarjayant987@gmail.com','123','6264515550','Pipalgon','male','user',1,1,'no',33250,'5 Years'),(10,'deepanshu ','kumar','deepanshu1297@gmail.com','0000','6265495916','burhan k ghar k pas','male','admin',90,20,'no',10000000,'no experience'),(11,'burhan','bootwala','matcrafttm@gmail.com','123','8770488131','Indore','male','user',1,1,'no',3000,'5 months'),(12,'Burhan','Bootwala','popingloving7@gmail.com','123','8770488131','Indore','male','user',1,1,'no',3000,'2 Years');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydb` ENABLE KEYS */;

--
-- Table structure for table `facultydbacademic`
--

DROP TABLE IF EXISTS `facultydbacademic`;
CREATE TABLE `facultydbacademic` (
  `regid` int(11) NOT NULL,
  `examination_passed` varchar(50) default NULL,
  `year_passing` int(11) default NULL,
  `board` varchar(30) default NULL,
  `marks` int(11) default NULL,
  `principal_subjects` varchar(30) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbacademic_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbacademic`
--


/*!40000 ALTER TABLE `facultydbacademic` DISABLE KEYS */;
LOCK TABLES `facultydbacademic` WRITE;
INSERT INTO `facultydbacademic` VALUES (3,'12th',2018,'CBSE',87,'PCM'),(1,'10th',2016,'CBSE',96,'None'),(1,'12th',2018,'CBSE',86,'PCM');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbacademic` ENABLE KEYS */;

--
-- Table structure for table `facultydbach`
--

DROP TABLE IF EXISTS `facultydbach`;
CREATE TABLE `facultydbach` (
  `regid` int(11) NOT NULL,
  `details` varchar(200) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbach_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbach`
--


/*!40000 ALTER TABLE `facultydbach` DISABLE KEYS */;
LOCK TABLES `facultydbach` WRITE;
INSERT INTO `facultydbach` VALUES (3,'Won Nothing'),(1,'Won 1st'),(1,'Won 2nd'),(1,'Won 3rd');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbach` ENABLE KEYS */;

--
-- Table structure for table `facultydbcert`
--

DROP TABLE IF EXISTS `facultydbcert`;
CREATE TABLE `facultydbcert` (
  `regid` int(11) NOT NULL,
  `details` varchar(200) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbcert_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbcert`
--


/*!40000 ALTER TABLE `facultydbcert` DISABLE KEYS */;
LOCK TABLES `facultydbcert` WRITE;
INSERT INTO `facultydbcert` VALUES (3,'Cousera Certificate');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbcert` ENABLE KEYS */;

--
-- Table structure for table `facultydbdept`
--

DROP TABLE IF EXISTS `facultydbdept`;
CREATE TABLE `facultydbdept` (
  `regid` int(11) NOT NULL,
  `deptname` varchar(30) default NULL,
  `deptid` varchar(20) default NULL,
  KEY `FK_regid` (`regid`),
  CONSTRAINT `FK_regid` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`),
  CONSTRAINT `facultydbdept_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbdept`
--


/*!40000 ALTER TABLE `facultydbdept` DISABLE KEYS */;
LOCK TABLES `facultydbdept` WRITE;
INSERT INTO `facultydbdept` VALUES (1,'cs','en3cs'),(12,'Engineering','EN3CS');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbdept` ENABLE KEYS */;

--
-- Table structure for table `facultydbdob`
--

DROP TABLE IF EXISTS `facultydbdob`;
CREATE TABLE `facultydbdob` (
  `regid` int(11) NOT NULL,
  `day` int(11) default NULL,
  `date` int(11) default NULL,
  `year` int(11) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbdob_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbdob`
--


/*!40000 ALTER TABLE `facultydbdob` DISABLE KEYS */;
LOCK TABLES `facultydbdob` WRITE;
INSERT INTO `facultydbdob` VALUES (1,11,17,2000),(12,17,11,2000);
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbdob` ENABLE KEYS */;

--
-- Table structure for table `facultydbstrengths`
--

DROP TABLE IF EXISTS `facultydbstrengths`;
CREATE TABLE `facultydbstrengths` (
  `regid` int(11) NOT NULL,
  `details` varchar(200) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbstrengths_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbstrengths`
--


/*!40000 ALTER TABLE `facultydbstrengths` DISABLE KEYS */;
LOCK TABLES `facultydbstrengths` WRITE;
INSERT INTO `facultydbstrengths` VALUES (3,'strong'),(3,''),(3,''),(3,'strong'),(1,'Won 1st'),(1,'Won 2nd');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbstrengths` ENABLE KEYS */;

--
-- Table structure for table `facultydbwe`
--

DROP TABLE IF EXISTS `facultydbwe`;
CREATE TABLE `facultydbwe` (
  `regid` int(11) NOT NULL,
  `industry` varchar(20) default NULL,
  `academic` varchar(20) default NULL,
  `research` varchar(20) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbwe_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbwe`
--


/*!40000 ALTER TABLE `facultydbwe` DISABLE KEYS */;
LOCK TABLES `facultydbwe` WRITE;
INSERT INTO `facultydbwe` VALUES (3,'7 Months','3 Months','3 months'),(1,'7 months','2 Years','8 Months');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbwe` ENABLE KEYS */;

--
-- Table structure for table `facultydbweakness`
--

DROP TABLE IF EXISTS `facultydbweakness`;
CREATE TABLE `facultydbweakness` (
  `regid` int(11) NOT NULL,
  `details` varchar(200) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbweakness_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbweakness`
--


/*!40000 ALTER TABLE `facultydbweakness` DISABLE KEYS */;
LOCK TABLES `facultydbweakness` WRITE;
INSERT INTO `facultydbweakness` VALUES (3,'allegric to everything'),(1,'Won 3rd'),(1,'Won 1st');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbweakness` ENABLE KEYS */;

--
-- Table structure for table `facultydbworkshopa`
--

DROP TABLE IF EXISTS `facultydbworkshopa`;
CREATE TABLE `facultydbworkshopa` (
  `regid` int(11) NOT NULL,
  `type` varchar(100) default NULL,
  `details` varchar(200) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbworkshopa_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbworkshopa`
--


/*!40000 ALTER TABLE `facultydbworkshopa` DISABLE KEYS */;
LOCK TABLES `facultydbworkshopa` WRITE;
INSERT INTO `facultydbworkshopa` VALUES (3,'Faculty Development Program','attended none');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbworkshopa` ENABLE KEYS */;

--
-- Table structure for table `facultydbworkshopo`
--

DROP TABLE IF EXISTS `facultydbworkshopo`;
CREATE TABLE `facultydbworkshopo` (
  `regid` int(11) NOT NULL,
  `details` varchar(200) default NULL,
  KEY `regid` (`regid`),
  CONSTRAINT `facultydbworkshopo_ibfk_1` FOREIGN KEY (`regid`) REFERENCES `facultydb` (`regid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `facultydbworkshopo`
--


/*!40000 ALTER TABLE `facultydbworkshopo` DISABLE KEYS */;
LOCK TABLES `facultydbworkshopo` WRITE;
INSERT INTO `facultydbworkshopo` VALUES (3,'attended none');
UNLOCK TABLES;
/*!40000 ALTER TABLE `facultydbworkshopo` ENABLE KEYS */;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
CREATE TABLE `register` (
  `regid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `city` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `role` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `dt` varchar(100) NOT NULL,
  PRIMARY KEY  (`regid`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--


/*!40000 ALTER TABLE `register` DISABLE KEYS */;
LOCK TABLES `register` WRITE;
INSERT INTO `register` VALUES (1,'vilekh','vilekh@gmail.com','123','indore mp','11111111111','Indore','male','admin',1,'Mon Jul 22 10:38:15 2019'),(2,'Burhan','burhanuddinboot.am@gmail.com','123','Hasanji Nagar,Rau','8770488131','Indore','male','manager',1,'Thurs'),(3,'Harshein','narang@gmail.com','123','Kalindi,Rau','33232','Indore','female','user',1,'Thurs');
UNLOCK TABLES;
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

