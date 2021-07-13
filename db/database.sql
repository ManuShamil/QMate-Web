/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - q_mate
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`q_mate` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `q_mate`;

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `Account_id` int(11) NOT NULL AUTO_INCREMENT,
  `Bank_name` varchar(99) DEFAULT NULL,
  `Account_number` int(11) DEFAULT NULL,
  `Balance` varchar(99) DEFAULT NULL,
  `password` varchar(99) DEFAULT NULL,
  PRIMARY KEY (`Account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`Account_id`,`Bank_name`,`Account_number`,`Balance`,`password`) values 
(1,'FEDERAL BNK',1234567890,'25000','fed18'),
(2,'BARODA',2147483647,'100000','bar67co'),
(3,'CHEMMAD',1234567444,'10000','che123'),
(4,'ICICI',2147483647,'25000','ic333'),
(5,'AXES',2147483647,'6000','axes345'),
(6,'BANK OF INDIA',2147483647,'567890','bi100'),
(7,'CANARA',3564,'25000','1'),
(8,'SBI',5645,'50000','2');

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `slot_id` int(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `bankname` varchar(30) DEFAULT NULL,
  `accountno` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`booking_id`,`slot_id`,`date`,`time`,`status`,`customer_id`,`bankname`,`accountno`) values 
(1,1,'2021-03-08','16:08:45','pending',5,'CANARA','1'),
(2,1,'2021-03-09','22:58:44','pending',6,'CANARA','1'),
(3,4,'2021-03-09','23:03:13','pending',6,'CANARA','1');

/*Table structure for table `booking_slot` */

DROP TABLE IF EXISTS `booking_slot`;

CREATE TABLE `booking_slot` (
  `booking_slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `space_slot_id` int(11) DEFAULT NULL,
  `date` varchar(60) DEFAULT NULL,
  `time` varchar(60) DEFAULT NULL,
  `status` varchar(60) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`booking_slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `booking_slot` */

insert  into `booking_slot`(`booking_slot_id`,`space_slot_id`,`date`,`time`,`status`,`customer_id`) values 
(1,1,'2021-03-08','16:07:16','entered',5),
(2,1,'2021-03-08','16:17:03','exit',5),
(3,5,'2021-03-09','22:36:23','pending',6),
(4,7,'2021-03-09','22:43:47','pending',6),
(5,59,'2021-03-10','11:28:59','entered',5),
(6,59,'2021-03-10','11:34:18','pending',5),
(7,59,'2021-03-10','16:37:35','pending',5),
(8,59,'2021-03-10','17:06:15','pending',5);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(20) DEFAULT NULL,
  `complaint` varchar(20) DEFAULT NULL,
  `reply` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`subject`,`complaint`,`reply`,`date`,`customer_id`) values 
(1,'Security','bad security behavio','we will  check it ou','2021-03-08',5),
(2,'surrounding','not clean','pending','2021-03-08',5),
(3,'fjfjckvlb','hdfjgvb','okkk','2021-03-09',6),
(4,'hh','okk\n','pending','2021-03-10',5),
(5,'fff','hh\n','pending','2021-03-10',5);

/*Table structure for table `covid_status` */

DROP TABLE IF EXISTS `covid_status`;

CREATE TABLE `covid_status` (
  `covid_status_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `Status` varchar(30) DEFAULT 'pending',
  PRIMARY KEY (`covid_status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `covid_status` */

insert  into `covid_status`(`covid_status_id`,`user_id`,`date`,`Status`) values 
(1,'5','2021-03-10','YES');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'kr@gmail.com','kr12','store'),
(3,'mk@gmail.com','mk12','store'),
(4,'ak@gmail.com','ak12','store'),
(5,'nee@gmail.com','nee123','user'),
(6,'sha@gmail.com','1','user'),
(7,'sp@gmail.com','sp123','parking'),
(8,'jk@gmail.com','jk12','parking'),
(9,'manu@gmail.com','2961','security'),
(10,'jal@gmail.com','1','security'),
(11,'','','user'),
(12,'nn','a','parking'),
(13,'ap@gmail.com','ap1','parking'),
(14,'','','store'),
(15,'','','store'),
(16,'am@gmail.com','am12','store'),
(17,'ir@gmail.com','9283','security'),
(18,'ap@gmail.com','ap1','parking'),
(19,'cvxf','444','user'),
(20,'neerajm1711@gmail.com','1519','security');

/*Table structure for table `parking` */

DROP TABLE IF EXISTS `parking`;

CREATE TABLE `parking` (
  `parking_slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `latitude` varchar(20) DEFAULT NULL,
  `longitude` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`parking_slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `parking` */

insert  into `parking`(`parking_slot_id`,`name`,`email`,`address`,`phone`,`login_id`,`latitude`,`longitude`,`status`) values 
(1,'SP slot','sp@gmail.com','kondotty',9446785433,7,'1.22.333','2.33.444','approved'),
(2,'JK slot','jk@gmail.com','kootilanghadi',6677889954,8,'2.33.4444','2.44.3333','approved'),
(3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(4,'Nirmala parking','nirmalaparking@gmail','thekkekkara',98765432134,12,'11','15','approved'),
(5,'Apmall','ap@gmail.com','kondotty',6677889965,13,'11.2543','75.3421','pending'),
(6,'Apmall','ap@gmail.com','kondotty',6677889965,18,'1.223.33','1.333.44','pending');

/*Table structure for table `parking_slot` */

DROP TABLE IF EXISTS `parking_slot`;

CREATE TABLE `parking_slot` (
  `parking_slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `parking_id` int(11) DEFAULT NULL,
  `slot_name` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`parking_slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `parking_slot` */

insert  into `parking_slot`(`parking_slot_id`,`parking_id`,`slot_name`,`status`) values 
(1,7,'1','empty'),
(2,7,'2','empty'),
(3,7,'3','filled'),
(4,12,'12','empty'),
(5,7,'11','filled'),
(6,13,'12','empty'),
(7,13,'','empty'),
(8,13,'','empty');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(20) DEFAULT NULL,
  `bookid` int(20) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `que_status` */

DROP TABLE IF EXISTS `que_status`;

CREATE TABLE `que_status` (
  `que_status_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `space_id` int(11) DEFAULT NULL,
  `tocken_no` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`que_status_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `que_status` */

/*Table structure for table `security` */

DROP TABLE IF EXISTS `security`;

CREATE TABLE `security` (
  `security_id` int(11) NOT NULL AUTO_INCREMENT,
  `security_name` varchar(20) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `pin` varchar(20) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `store_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`security_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `security` */

insert  into `security`(`security_id`,`security_name`,`age`,`gender`,`pin`,`photo`,`store_id`,`login_id`,`phone`,`email`,`post`,`place`,`city`,`state`) values 
(1,'Manu pk','1988-01-01','Male','676124','/static/store_security/WIN_20201230_15_50_39_Pro.jpg',2,9,9988776655,'manu@gmail.com','kondotty','kondotty','Malappuram','Kerala'),
(2,'Jalal k','1978-03-03','Male','676343','/static/store_security/IMG_20200606_085827_836.jpg',2,10,9677889954,'jal@gmail.com','Malappuram','Kootilanghadi','Malappuram','Kerala'),
(3,'Irshad','1999-02-02','Male','676121','/static/store_security/WIN_20201230_15_31_00_Pro.jpg',16,17,8987656754,'ir@gmail.com','malappuram','manjeri','malappuram','kerala'),
(4,'Neeraj.M.','2000-09-27','Male','676121','/static/store_security/WIN_20201230_15_31_00_Pro.jpg',2,20,7356029802,'neerajm1711@gmail.co','manjeri','manjeri','malappuram','kerala');

/*Table structure for table `space_slot` */

DROP TABLE IF EXISTS `space_slot`;

CREATE TABLE `space_slot` (
  `spaceslot_id` int(11) NOT NULL AUTO_INCREMENT,
  `store_id` varchar(20) DEFAULT NULL,
  `From_time` varchar(55) DEFAULT NULL,
  `T0_time` varchar(55) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`spaceslot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

/*Data for the table `space_slot` */

insert  into `space_slot`(`spaceslot_id`,`store_id`,`From_time`,`T0_time`,`Date`,`Status`) values 
(1,'2','15:57:00','16:07:00','2021-03-08','free'),
(2,'2','16:07:00','16:17:00','2021-03-08','free'),
(3,'2','16:54:00','17:04:00','2021-03-08','free'),
(4,'2','17:04:00','17:14:00','2021-03-08','free'),
(5,'2','01:59:00','02:09:00','2021-03-09','free'),
(6,'2','02:09:00','02:19:00','2021-03-09','free'),
(7,'2','02:19:00','02:29:00','2021-03-09','free'),
(8,'2','02:29:00','02:39:00','2021-03-09','free'),
(10,'2','02:49:00','02:59:00','2021-03-09','free'),
(11,'2','02:59:00','03:09:00','2021-03-09','free'),
(12,'2','03:09:00','03:19:00','2021-03-09','free'),
(13,'2','03:19:00','03:29:00','2021-03-09','free'),
(14,'2','03:29:00','03:39:00','2021-03-09','free'),
(15,'2','03:39:00','03:49:00','2021-03-09','free'),
(16,'2','03:49:00','03:59:00','2021-03-09','free'),
(17,'2','03:59:00','04:09:00','2021-03-09','free'),
(18,'2','04:09:00','04:19:00','2021-03-09','free'),
(19,'2','04:19:00','04:29:00','2021-03-09','free'),
(20,'2','04:29:00','04:39:00','2021-03-09','free'),
(21,'2','04:39:00','04:49:00','2021-03-09','free'),
(22,'2','04:49:00','04:59:00','2021-03-09','free'),
(23,'2','04:59:00','05:09:00','2021-03-09','free'),
(24,'2','05:09:00','05:19:00','2021-03-09','free'),
(25,'2','05:19:00','05:29:00','2021-03-09','free'),
(26,'2','05:29:00','05:39:00','2021-03-09','free'),
(27,'2','05:39:00','05:49:00','2021-03-09','free'),
(28,'2','05:49:00','05:59:00','2021-03-09','free'),
(29,'2','05:59:00','06:09:00','2021-03-09','free'),
(30,'2','06:09:00','06:19:00','2021-03-09','free'),
(31,'2','06:19:00','06:29:00','2021-03-09','free'),
(32,'2','06:29:00','06:39:00','2021-03-09','free'),
(33,'2','06:39:00','06:49:00','2021-03-09','free'),
(34,'2','06:49:00','06:59:00','2021-03-09','free'),
(35,'2','06:59:00','07:09:00','2021-03-09','free'),
(36,'2','07:09:00','07:19:00','2021-03-09','free'),
(37,'2','07:19:00','07:29:00','2021-03-09','free'),
(38,'2','07:29:00','07:39:00','2021-03-09','free'),
(39,'2','07:39:00','07:49:00','2021-03-09','free'),
(40,'2','07:49:00','07:59:00','2021-03-09','free'),
(41,'2','07:59:00','08:09:00','2021-03-09','free'),
(42,'2','08:09:00','08:19:00','2021-03-09','free'),
(43,'2','08:19:00','08:29:00','2021-03-09','free'),
(44,'2','08:29:00','08:39:00','2021-03-09','free'),
(45,'2','08:39:00','08:49:00','2021-03-09','free'),
(46,'2','08:49:00','08:59:00','2021-03-09','free'),
(47,'2','08:59:00','09:09:00','2021-03-09','free'),
(48,'2','09:09:00','09:19:00','2021-03-09','free'),
(49,'2','09:19:00','09:29:00','2021-03-09','free'),
(50,'2','09:29:00','09:39:00','2021-03-09','free'),
(51,'2','09:39:00','09:49:00','2021-03-09','free'),
(52,'2','09:49:00','09:59:00','2021-03-09','free'),
(53,'2','09:59:00','10:09:00','2021-03-09','free'),
(54,'2','10:09:00','10:19:00','2021-03-09','free'),
(55,'2','10:19:00','10:29:00','2021-03-09','free'),
(56,'2','10:29:00','10:39:00','2021-03-09','free'),
(58,'2','10:49:00','10:59:00','2021-03-09','free'),
(59,'2','10:51:00','11:01:00','2021-03-10','free'),
(60,'2','11:01:00','11:11:00','2021-03-10','free');

/*Table structure for table `store` */

DROP TABLE IF EXISTS `store`;

CREATE TABLE `store` (
  `store_id` int(11) NOT NULL AUTO_INCREMENT,
  `store_name` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`store_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `store` */

insert  into `store`(`store_id`,`store_name`,`post`,`pin`,`place`,`phone`,`email`,`login_id`,`status`) values 
(1,'KRBakery','Manjeri','676121','Manjeri',9887766543,'kr@gmail.com',2,'approved'),
(2,'MK stationary','Manjeri','676121','Manjeri',9988776655,'mk@gmail.com',3,'rejected'),
(3,'AK bookstall','Manjeri','676121','Manjeri',9765434567,'ak@gmail.com',4,'approved'),
(6,'Am stores','malappuram','676768','kondotty',8769858574,'am@gmail.com',16,'approved');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) DEFAULT NULL,
  `age` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `photo` varchar(200) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`user_name`,`age`,`gender`,`address`,`photo`,`login_id`,`phone`,`email`) values 
(1,'Neeraj M','27/9/2000','male','Manjeri','/static/user_images/20210308-155153.jpg',5,7356020202,'nee@gmail.com'),
(2,'Shahabaspk','12/12/1999','male','Malappuram','/static/user_images/20210308-155259.jpg',6,9443525824,'sha@gmail.com');

/*Table structure for table `visiting_history` */

DROP TABLE IF EXISTS `visiting_history`;

CREATE TABLE `visiting_history` (
  `visit_history_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` varchar(20) DEFAULT NULL,
  `space_slot_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`visit_history_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `visiting_history` */

insert  into `visiting_history`(`visit_history_id`,`user_id`,`date`,`time`,`space_slot_id`) values 
(1,'5','2021-03-08','16:07:16',1),
(2,'5','2021-03-08','16:17:03',1),
(3,'5','2021-03-08','16:07:16',1),
(4,'5','2021-03-08','16:07:16',1),
(5,'5','2021-03-08','16:07:16',1),
(6,'5','2021-03-08','16:17:03',1),
(7,'5','2021-03-08','16:07:16',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
