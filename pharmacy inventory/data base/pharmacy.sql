-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 16, 2021 at 07:38 PM
-- Server version: 8.0.18
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy`
--

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_name` varchar(250) COLLATE utf8mb4_general_ci NOT NULL,
  `branch_name` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `count` varchar(250) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_name`, `branch_name`, `count`) VALUES
('panadol', 'Ahmed Oraby', '15'),
('panadol extra ', 'Mohandessin', '40'),
('panadol cold and flu', 'Ahmed Oraby ', '30'),
('panadol cold and flu', 'Mohandessin', '70'),
('vitamin c', 'Mohandessin', '50'),
('vitamin c', 'Ahmed Oraby', '10'),
('panadol', 'EL-Tagamoa5', '50'),
('panadol extra', 'EL-Tagamoa5', '20'),
('scaro gel', 'EL-Tagamoa5', '80'),
('vitamin c', 'EL-Tagamoa5', '40'),
('panadol extra', 'Qasr ELNil.ST', '12'),
('scaro gel', 'Qasr ELNil.ST', '50'),
('panadol cold and flu', 'Qasr ELNil.ST', '70');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
