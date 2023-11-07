-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 06, 2023 at 08:48 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pos-bu`
--

-- --------------------------------------------------------

--
-- Table structure for table `cashier`
--

DROP TABLE IF EXISTS `cashier`;
CREATE TABLE IF NOT EXISTS `cashier` (
  `id` varchar(9) NOT NULL,
  `name` varchar(54) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cashier`
--

INSERT INTO `cashier` (`id`, `name`) VALUES
('C001', 'Alex'),
('C002', 'Andre'),
('C003', 'Angel');

-- --------------------------------------------------------

--
-- Table structure for table `date`
--

DROP TABLE IF EXISTS `date`;
CREATE TABLE IF NOT EXISTS `date` (
  `id` varchar(9) NOT NULL,
  `date` varchar(54) NOT NULL,
  `full_date` varchar(54) NOT NULL,
  `day_name` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `day_of_week` int NOT NULL,
  `day_of_month` int NOT NULL,
  `day_of_year` int NOT NULL,
  `month` int NOT NULL,
  `year` int NOT NULL,
  `isHoliday` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `date`
--

INSERT INTO `date` (`id`, `date`, `full_date`, `day_name`, `day_of_week`, `day_of_month`, `day_of_year`, `month`, `year`, `isHoliday`) VALUES
('c2dbe7af-', '2023-11-06', '2023-11-06', 'Monday', 2, 6, 310, 11, 2023, 1),
('e57b23db-', '2023-11-05', '2023-11-05', 'Sunday', 1, 5, 309, 11, 2023, 1),
('f8c7d374-', '2023-11-01', '2023-11-01', 'Wednesday', 4, 1, 305, 11, 2023, 1);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` varchar(9) NOT NULL,
  `name` varchar(54) NOT NULL,
  `qty` int NOT NULL,
  `price` int NOT NULL,
  `discount` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `name`, `qty`, `price`, `discount`) VALUES
('P001', 'odol', 45, 13000, 5),
('P002', 'ice cream', 18, 5000, 0),
('P003', 'sikat gigi', 45, 27000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `store`
--

DROP TABLE IF EXISTS `store`;
CREATE TABLE IF NOT EXISTS `store` (
  `id` varchar(9) NOT NULL,
  `name` varchar(54) NOT NULL,
  `address` varchar(180) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `phone` varchar(54) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store`
--

INSERT INTO `store` (`id`, `name`, `address`, `phone`) VALUES
('S001', 'Angkasa Pura POS', 'Jl. Industri Raya No.Kav. 1, RW.10, Gn. Sahari Sel., Kec. Kemayoran, Jkt Utara, Daerah Khusus Ibukota Jakarta 10720', '256.489.9068'),
('S002', 'Karawaci POS', 'Grii Karawaci, Jl. Boulevard Gajah Mada No.1900, RT.001/RW.009, Panunggangan Bar., Kec. Cibodas, Kota Tangerang, Banten 15138', '223.489.9321');

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `id` varchar(9) NOT NULL,
  `cashier_id` varchar(9) NOT NULL,
  `store_id` varchar(9) NOT NULL,
  `date_id` varchar(9) NOT NULL,
  `regards` varchar(54) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cashier_id` (`cashier_id`),
  KEY `store_id` (`store_id`),
  KEY `date_id` (`date_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `cashier_id`, `store_id`, `date_id`, `regards`) VALUES
('T001', 'C001', 'S002', 'e57b23db-', 'Terima Kasih!'),
('T002', 'C002', 'S001', 'c2dbe7af-', 'Terima Kasih!'),
('T003', 'C002', 'S001', 'f8c7d374-', 'Terima Kasih!'),
('T004', 'C001', 'S001', 'e57b23db-', 'Terima Kasih!'),
('T005', 'C002', 'S001', 'c2dbe7af-', 'Terima Kasih!');

-- --------------------------------------------------------

--
-- Table structure for table `transaction_details`
--

DROP TABLE IF EXISTS `transaction_details`;
CREATE TABLE IF NOT EXISTS `transaction_details` (
  `id` varchar(9) NOT NULL,
  `transaction_id` varchar(9) NOT NULL,
  `product_id` varchar(9) NOT NULL,
  `qty` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `transaction_id` (`transaction_id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transaction_details`
--

INSERT INTO `transaction_details` (`id`, `transaction_id`, `product_id`, `qty`) VALUES
('TD001', 'T001', 'P001', 21),
('TD002', 'T002', 'P002', 18),
('TD003', 'T001', 'P003', 2),
('TD004', 'T002', 'P002', 5),
('TD005', 'T004', 'P001', 12),
('TD006', 'T005', 'P002', 4),
('TD007', 'T003', 'P003', 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`cashier_id`) REFERENCES `cashier` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`store_id`) REFERENCES `store` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transaction_ibfk_3` FOREIGN KEY (`date_id`) REFERENCES `date` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transaction_details`
--
ALTER TABLE `transaction_details`
  ADD CONSTRAINT `transaction_details_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transaction_details_ibfk_2` FOREIGN KEY (`transaction_id`) REFERENCES `transaction` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
