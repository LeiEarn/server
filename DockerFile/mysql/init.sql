-- MySQL dump 10.13  Distrib 5.7.21, for macos10.13 (x86_64)
--
-- Host: 127.0.0.1    Database: ZXQ
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

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
-- Table structure for table `audit_administrator`
--

DROP TABLE IF EXISTS `audit_administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_administrator` (
  `audit_id` int(11) NOT NULL,
  `name` varchar(16) NOT NULL,
  `account` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`audit_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_administrator`
--

LOCK TABLES `audit_administrator` WRITE;
/*!40000 ALTER TABLE `audit_administrator` DISABLE KEYS */;
INSERT INTO `audit_administrator` VALUES (227,'yunquan','yunquan','12345678');
/*!40000 ALTER TABLE `audit_administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `com_identity`
--

DROP TABLE IF EXISTS `com_identity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `com_identity` (
  `user_com_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(5) NOT NULL,
  `email` varchar(30) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `company` varchar(32) NOT NULL,
  `job_num` varchar(10) NOT NULL,
  `prove` varchar(255) NOT NULL,
  `state_prove` varchar(1) NOT NULL DEFAULT '0',
  `user_user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_com_id`,`user_user_id`),
  KEY `fk_job_identity_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_job_identity_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `com_identity`
--

LOCK TABLES `com_identity` WRITE;
/*!40000 ALTER TABLE `com_identity` DISABLE KEYS */;
/*!40000 ALTER TABLE `com_identity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `founder`
--

DROP TABLE IF EXISTS `founder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `founder` (
  `founder_id` int(11) NOT NULL AUTO_INCREMENT,
  `organization_org_name` varchar(16) NOT NULL,
  `organization_founder_name` varchar(16) NOT NULL,
  `user_user_id` int(11) NOT NULL,
  PRIMARY KEY (`founder_id`,`organization_org_name`,`organization_founder_name`,`user_user_id`),
  KEY `fk_founder_organization1_idx` (`organization_org_name`,`organization_founder_name`),
  KEY `fk_founder_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_founder_organization1` FOREIGN KEY (`organization_org_name`, `organization_founder_name`) REFERENCES `organization` (`org_name`, `founder_name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_founder_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `founder`
--

LOCK TABLES `founder` WRITE;
/*!40000 ALTER TABLE `founder` DISABLE KEYS */;
/*!40000 ALTER TABLE `founder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organization`
--

DROP TABLE IF EXISTS `organization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organization` (
  `org_name` varchar(16) NOT NULL,
  `introduction` varchar(255) NOT NULL,
  `founder_name` varchar(16) NOT NULL,
  PRIMARY KEY (`org_name`,`founder_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organization`
--

LOCK TABLES `organization` WRITE;
/*!40000 ALTER TABLE `organization` DISABLE KEYS */;
/*!40000 ALTER TABLE `organization` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organization_has_user`
--

DROP TABLE IF EXISTS `organization_has_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `organization_has_user` (
  `organization_org_name` varchar(16) NOT NULL,
  `user_user_id` int(11) NOT NULL,
  PRIMARY KEY (`organization_org_name`,`user_user_id`),
  KEY `fk_organization_has_user_user1_idx` (`user_user_id`),
  KEY `fk_organization_has_user_organization_idx` (`organization_org_name`),
  CONSTRAINT `fk_organization_has_user_organization` FOREIGN KEY (`organization_org_name`) REFERENCES `organization` (`org_name`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_organization_has_user_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organization_has_user`
--

LOCK TABLES `organization_has_user` WRITE;
/*!40000 ALTER TABLE `organization_has_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `organization_has_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stu_identity`
--

DROP TABLE IF EXISTS `stu_identity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stu_identity` (
  `user_stu_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(5) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `school` varchar(32) NOT NULL,
  `college` varchar(16) NOT NULL,
  `student_num` int(10) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `prove` varchar(255) NOT NULL,
  `state_prove` varchar(1) NOT NULL DEFAULT '0',
  `user_user_id` int(11) NOT NULL,
  PRIMARY KEY (`user_stu_id`,`user_user_id`),
  KEY `fk_stu_identity_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_stu_identity_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stu_identity`
--

LOCK TABLES `stu_identity` WRITE;
/*!40000 ALTER TABLE `stu_identity` DISABLE KEYS */;
INSERT INTO `stu_identity` VALUES (1,'何枷瑜','13169766417',' ','中山大学','',16341007,'M','http://172.26.47.246:8080/_uploads/photos/csCgjkGv.png','P',24),(2,'qweq','12312414242',' ','qweqwe',' ',16341000,'W',' ','P',1);
/*!40000 ALTER TABLE `stu_identity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  `type` varchar(1) NOT NULL,
  `publish_id` int(11) NOT NULL,
  `state` varchar(1) NOT NULL DEFAULT '0',
  `wjx_id` varchar(20) DEFAULT NULL,
  `task_intro` varchar(225) NOT NULL,
  `max_num` int(11) NOT NULL,
  `participants_num` int(11) NOT NULL DEFAULT '0',
  `money` float NOT NULL,
  `release_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sign_start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sign_end_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `audit_administrator_audit_id` int(11) NOT NULL,
  PRIMARY KEY (`task_id`,`audit_administrator_audit_id`),
  KEY `fk_task_audit_administrator1_idx` (`audit_administrator_audit_id`),
  CONSTRAINT `fk_task_audit_administrator1` FOREIGN KEY (`audit_administrator_audit_id`) REFERENCES `audit_administrator` (`audit_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,'亲卫队','O',1,'W','-','误区二',5,3,10,'2019-06-25 16:00:00','2019-07-01 16:00:00','2019-07-02 16:00:00',227),(2,'气温','W',2,'S','-','QWE',10,1,5,'2019-06-25 16:00:00','2019-07-02 16:00:00','2019-08-09 16:00:00',227),(3,'title','W',24,'W','wjxId','desc\nstring',6,1,0.800828,'2019-06-26 21:26:23','2019-06-26 21:26:23','2019-06-26 21:26:04',227),(4,'title','W',24,'W','wjxId','desc',6,1,0.800828,'2019-06-26 21:54:03','2019-06-26 21:54:03','2019-06-26 21:26:04',227),(5,'asdfsfa','O',24,'W','','sdafasf&&[]',12,0,12,'2019-06-27 02:30:22','2019-06-27 02:30:22','2019-06-27 02:30:00',227),(6,'adfasf','W',24,'P','39541637','None',12,0,0,'2019-06-27 03:16:57','2019-06-27 03:16:57','2019-06-27 03:15:00',227),(7,'调查问卷','W',24,'P','39541637','调查问卷',10,0,0,'2019-06-27 04:05:10','2019-06-27 04:05:10','2019-06-27 04:00:00',227);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `wechat_id` varchar(45) NOT NULL,
  `nickname` varchar(16) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `isprove` varchar(1) DEFAULT '0',
  `identity` varchar(1) DEFAULT '0',
  `intro` varchar(255) DEFAULT '""',
  `create_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `balance` float DEFAULT '0',
  `credit` int(11) DEFAULT '100',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'12345','haha','qwe','P','S','娇嗲设计的','2019-06-24 16:00:00',0,100),(2,'115','nickName','avartUrl','F','S','-','2019-06-25 06:55:35',0,45),(3,'043QQqy61N1nDM1Eu2C61Ynty61QQqyh','nick','','P','C','-','2019-06-25 08:15:20',0,10),(4,'023e75W60rUMnF1ozRV60GRsW60e75WZ','nick','','W','C','-','2019-06-25 08:16:07',0,68),(5,'023e75W60rUMnF1ozRV60GRsW60e75WZ','nick','','W','C','-','2019-06-25 08:22:47',0,75),(6,'023e75W60rUMnF1ozRV60GRsW60e75WZ','nick','','W','C','-','2019-06-25 08:25:01',0,12),(7,'string','string','string','P','S','-','2019-06-25 12:31:22',0,100),(8,'043QBrDi2tvD7B07rIFi2nTvDi2QBrDL','nick','','W','C','-','2019-06-25 14:10:54',0,54),(9,'023N8hyw1suNgg0B7Lzw1yo8yw1N8hyQ','nick','','N','U','-','2019-06-25 14:11:30',0,100),(10,'033hGefo0wCp4k1DZrco0b4zfo0hGefy','nick','','N','U','-','2019-06-25 14:12:22',0,100),(11,'033SxHZX0YyJ5W1jCuYX0VBKZX0SxHZm','nick','','N','U','-','2019-06-25 14:14:05',0,45),(12,'043rpqS80aYl3F12KzV80G50S80rpqS4','nick','','N','U','-','2019-06-25 14:14:58',0,100),(13,'043hNm4b27yJPN0SSe3b2imI4b2hNm4g','nick','','N','U','-','2019-06-25 14:17:29',0,99),(14,'023Cb1Z51rk1TS1UVX1616u8Z51Cb1Zd','nick','','N','U','-','2019-06-25 14:19:17',0,100),(15,'023HgWq12E7NnW0TXUo12HpNq12HgWqz','nick','','N','U','-','2019-06-25 14:23:50',0,24),(16,'033hEQd91qIu9P16PJc91lt5e91hEQdc','nick','','N','U','-','2019-06-25 14:24:28',0,11),(17,'033NKIf71JarbN1KDzd714XNf71NKIfT','nick','','N','U','-','2019-06-25 14:27:13',0,5),(18,'043t2Sq50Jeu1E1Qmhr50LLJq50t2Sqd','nick','','N','U','-','2019-06-25 14:28:33',0,4),(19,'043GOx4804pyfE1xys380naw480GOx45','nick','','N','U','-','2019-06-25 14:28:57',0,100),(20,'033vDeog16Ofmr01E4og1QK8og1vDeoQ','nick','','N','U','-','2019-06-25 14:29:11',0,67),(24,'ofAUV5mo9AjSRLiowX6i4PPVhTzw','hejiayu','http://172.26.47.246:8080/_uploads/photos/PGx6NSyI.png','P','S','-','2019-06-26 19:28:16',0,100);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_has_task`
--

DROP TABLE IF EXISTS `user_has_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_has_task` (
  `user_user_id` int(11) NOT NULL,
  `task_task_id` int(11) NOT NULL,
  `task_audit_administrator_audit_id` int(11) NOT NULL,
  `isagree` varchar(1) NOT NULL,
  PRIMARY KEY (`user_user_id`,`task_task_id`,`task_audit_administrator_audit_id`),
  KEY `fk_user_has_task_task1_idx` (`task_task_id`,`task_audit_administrator_audit_id`),
  KEY `fk_user_has_task_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_user_has_task_task1` FOREIGN KEY (`task_task_id`, `task_audit_administrator_audit_id`) REFERENCES `task` (`task_id`, `audit_administrator_audit_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_has_task_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_has_task`
--

LOCK TABLES `user_has_task` WRITE;
/*!40000 ALTER TABLE `user_has_task` DISABLE KEYS */;
INSERT INTO `user_has_task` VALUES (1,1,227,'N'),(1,2,227,'N'),(3,1,227,'N'),(7,1,227,'N'),(24,2,227,'Q');
/*!40000 ALTER TABLE `user_has_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_task_job`
--

DROP TABLE IF EXISTS `user_task_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_task_job` (
  `task_task_id` int(11) NOT NULL,
  `user_user_id` int(11) NOT NULL,
  `job_path` varchar(255) NOT NULL,
  `unload_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`task_task_id`,`user_user_id`,`unload_time`),
  KEY `fk_user_task_job_task1_idx` (`task_task_id`),
  KEY `fk_user_task_job_user1_idx` (`user_user_id`),
  CONSTRAINT `fk_user_task_job_task1` FOREIGN KEY (`task_task_id`) REFERENCES `task` (`task_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_user_task_job_user1` FOREIGN KEY (`user_user_id`) REFERENCES `user` (`user_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_task_job`
--

LOCK TABLES `user_task_job` WRITE;
/*!40000 ALTER TABLE `user_task_job` DISABLE KEYS */;
INSERT INTO `user_task_job` VALUES (3,24,'9e736b92-7528-4f52-b0af-3f7db001c913','2019-06-26 22:37:18');
/*!40000 ALTER TABLE `user_task_job` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-27 12:25:44
