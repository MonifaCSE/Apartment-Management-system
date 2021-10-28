-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 08, 2021 at 05:44 PM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `apartment management system`
--

-- --------------------------------------------------------

--
-- Table structure for table `apartment_details`
--

CREATE TABLE `apartment_details` (
  `Apartment_no` int(50) NOT NULL,
  `Apartment_name` varchar(260) NOT NULL,
  `Location` varchar(266) NOT NULL,
  `Number_of_room` int(50) NOT NULL,
  `Floor` varchar(50) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `Details` varchar(266) NOT NULL,
  `Description` varchar(266) NOT NULL,
  `Cost` int(50) NOT NULL,
  `image1` varchar(266) NOT NULL,
  `image2` varchar(266) NOT NULL,
  `image3` varchar(266) NOT NULL,
  `Available` varchar(266) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `apartment_details`
--

INSERT INTO `apartment_details` (`Apartment_no`, `Apartment_name`, `Location`, `Number_of_room`, `Floor`, `Type`, `Details`, `Description`, `Cost`, `image1`, `image2`, `image3`, `Available`) VALUES
(10, 'Sunshine City', 'Khulshiww', 1, '15', 'House', '4Bed,1Hall,1Kitchen of 1600sqft', 'Easy access to the main road,near to the bus stand', 20000, 'b1.jpg', 'h1.jpg', 'k1.jpg', 'Yes'),
(12, 'Rima Villa', 'Jamal Khan', 1, '15', 'Flat', '3Bed,1Hall,1Kitchen of 2100sqft', 'Near to the shopping mall', 17000, 'b2.jpg', 'h2.jpg', 'k2.jpg', 'No'),
(15, 'Jolly place', 'Chawkbazar', 6, '5th', 'Flat', '4Bed,1Hall,1K of 1600sqft', 'Mosque,event hall near the apartment', 18000, 'b3.jpg', 'h3.jpg', 'k3.jpg', 'No');

-- --------------------------------------------------------

--
-- Table structure for table `image`
--

CREATE TABLE `image` (
  `id` int(50) NOT NULL,
  `Apartment_no` int(50) NOT NULL,
  `image1` varchar(266) NOT NULL,
  `data` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `image`
--

INSERT INTO `image` (`id`, `Apartment_no`, `image1`, `data`) VALUES
(1, 2, 'k3.jpg', 0x4d456578616d322e706e67),
(2, 1, 'k2.jpg', 0x343434342e706e67),
(4, 1, 'Ap_no-15_Exterior.jpg', 0x41705f6e6f2d31305f4b69746368656e2e6a7067);

-- --------------------------------------------------------

--
-- Table structure for table `rent_info`
--

CREATE TABLE `rent_info` (
  `Rent_id` int(11) NOT NULL,
  `Tenant_ID` int(11) NOT NULL,
  `Tenant_name` varchar(266) NOT NULL,
  `Apartment_no` int(50) NOT NULL,
  `Paid_Date` date NOT NULL,
  `Paid_amount` varchar(50) NOT NULL,
  `Transection_no` varchar(266) NOT NULL,
  `Month` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rent_info`
--

INSERT INTO `rent_info` (`Rent_id`, `Tenant_ID`, `Tenant_name`, `Apartment_no`, `Paid_Date`, `Paid_amount`, `Transection_no`, `Month`) VALUES
(6, 3, 'Ria Khan', 12, '2020-09-14', '20000', '27634852527565', '2020-08'),
(8, 5, 'Nurul Alam', 10, '2020-10-02', '17000', '0987625', '2020-08'),
(9, 3, 'Ria Khan', 12, '2020-10-26', '20000', '23456789', '2020-09'),
(10, 14, 'Nita Hossain', 12, '2020-11-28', '17000', '09876254324567', '2020-09');

-- --------------------------------------------------------

--
-- Table structure for table `rent_request`
--

CREATE TABLE `rent_request` (
  `Request_id` int(11) NOT NULL,
  `Tenant_ID` int(11) NOT NULL,
  `Tenant_name` varchar(266) NOT NULL,
  `Apartment_no` int(50) NOT NULL,
  `Paid_Date` date NOT NULL,
  `Paid_amount` varchar(50) NOT NULL,
  `Transection_no` varchar(266) NOT NULL,
  `Month` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `rent_request`
--

INSERT INTO `rent_request` (`Request_id`, `Tenant_ID`, `Tenant_name`, `Apartment_no`, `Paid_Date`, `Paid_amount`, `Transection_no`, `Month`) VALUES
(1, 3, 'Ria Khan', 12, '2020-11-28', '20000', '27625233', '2020-10'),
(2, 14, 'Nita Hossain', 15, '2020-11-28', '17000', '733618', '2020-11');

-- --------------------------------------------------------

--
-- Table structure for table `request_details`
--

CREATE TABLE `request_details` (
  `Request_ID` int(11) NOT NULL,
  `Name` varchar(266) NOT NULL,
  `Apartment_no` int(50) NOT NULL,
  `Address` varchar(266) NOT NULL,
  `Email` varchar(260) NOT NULL,
  `Phone_number` varchar(266) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `request_details`
--

INSERT INTO `request_details` (`Request_ID`, `Name`, `Apartment_no`, `Address`, `Email`, `Phone_number`) VALUES
(1, 'Nurul Alam', 10, 'Bahaddarhat', 'nurul@gmail.com', '+8801791662434');

-- --------------------------------------------------------

--
-- Table structure for table `tenant_details`
--

CREATE TABLE `tenant_details` (
  `Tenant_ID` int(11) NOT NULL,
  `Tenant_name` varchar(266) NOT NULL,
  `Apartment_no` int(50) NOT NULL,
  `Address` varchar(266) NOT NULL,
  `Email` varchar(260) NOT NULL,
  `Phone_number` varchar(266) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tenant_details`
--

INSERT INTO `tenant_details` (`Tenant_ID`, `Tenant_name`, `Apartment_no`, `Address`, `Email`, `Phone_number`) VALUES
(3, 'Ria Khan', 12, 'Bahaddarhat', 'ria@gmail.com', '+8801528632222'),
(14, 'Nita Hossain', 15, 'Nasirabad', 'nita@gmail.com', '+8801867622863'),
(15, 'Safa Marua', 10, 'Chawkbazar', 'safa@gmail.com', '+8801734916624');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `fullname` varchar(266) NOT NULL,
  `username` varchar(266) NOT NULL,
  `email` varchar(266) NOT NULL,
  `address` varchar(260) NOT NULL,
  `password` varchar(266) NOT NULL,
  `user_type` varchar(266) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `fullname`, `username`, `email`, `address`, `password`, `user_type`) VALUES
(1, 'Monifa Sultana', 'monicse', 'monifasultana5637@gmail.com', 'Chawkbazar', '41', 'Admin'),
(2, 'Afrida Yesmin Fariha', 'fariha', 'fariha@gmail.com', 'Chawkbazar', '52', 'Admin'),
(3, 'Sumaiya Khan', 'sumi', 'sumikhan5838@gmail.com', 'Feni', '58', 'User'),
(4, 'Israt Jahan Tuhin', 'israt', 'israt@gmail.com', 'Chawkbazar', '75', 'Admin'),
(5, 'Safa Marua', 'safa', 'safa@gmail.com', 'Khulshi', '150', 'User'),
(6, 'Nita Hossain', 'nita', 'nita@gmail.com', 'Nasirabad', '90', 'User'),
(7, 'Ripa Alam', 'ripa', 'ripa@gmail.com', 'Bahaddarhat', '#980', 'User'),
(8, 'Mariam Sultana', 'mariam', 'mnvccgh@gmail.com', 'Chawkbazar', '17', 'Admin'),
(9, 'Monifa Sultana', 'moni', 'moni@gmail.com', ' kjhfd', 'C183241', 'Admin'),
(10, 'Nowrin', 'nowrin', 'no@gmail.com', 'Nasirabad', '2wed', 'User'),
(11, 'Nurul Alam', 'alam', 'nurul@gmail.com', 'Bahaddarhat', '15', 'User'),
(12, 'Anika Sultana', 'anika', 'anika@gmail.com', 'sksh', '7678', 'User'),
(13, 'Brishty Akter', 'brishty', 'bddd@gmail.com', 'fgshdfsfd', '378yd', 'User'),
(14, 'Moni Khan', 'moni', 'mo@gmail.com', 'hhhxqsg', '8dwhd', 'User'),
(15, 'Marjan Sultana', 'marj', 'marj@gmail.com', 'skkbs', '89h2u', 'User'),
(16, 'Lopa Dash', 'lopa', 'lo@gmail.com', 'oiwoiyi', '9eu', 'User'),
(17, 'Nilufa Akter', 'nilufa', 'nilu@gmail.com', 'Nasirabad', '2038', 'Admin'),
(18, 'Israt moontaha', 'moon', 'moon@gmail.com', 'qowudgqwhd', '2u9u', 'User');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apartment_details`
--
ALTER TABLE `apartment_details`
  ADD PRIMARY KEY (`Apartment_no`);

--
-- Indexes for table `image`
--
ALTER TABLE `image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `rent_info`
--
ALTER TABLE `rent_info`
  ADD PRIMARY KEY (`Rent_id`),
  ADD KEY `Test1` (`Tenant_ID`),
  ADD KEY `Apartment_no` (`Apartment_no`);

--
-- Indexes for table `rent_request`
--
ALTER TABLE `rent_request`
  ADD PRIMARY KEY (`Request_id`),
  ADD KEY `Test1` (`Tenant_ID`),
  ADD KEY `Apartment_no` (`Apartment_no`);

--
-- Indexes for table `request_details`
--
ALTER TABLE `request_details`
  ADD PRIMARY KEY (`Request_ID`),
  ADD KEY `Test3` (`Apartment_no`);

--
-- Indexes for table `tenant_details`
--
ALTER TABLE `tenant_details`
  ADD PRIMARY KEY (`Tenant_ID`),
  ADD KEY `Test3` (`Apartment_no`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `apartment_details`
--
ALTER TABLE `apartment_details`
  MODIFY `Apartment_no` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `image`
--
ALTER TABLE `image`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `rent_info`
--
ALTER TABLE `rent_info`
  MODIFY `Rent_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `rent_request`
--
ALTER TABLE `rent_request`
  MODIFY `Request_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `request_details`
--
ALTER TABLE `request_details`
  MODIFY `Request_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `tenant_details`
--
ALTER TABLE `tenant_details`
  MODIFY `Tenant_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `rent_info`
--
ALTER TABLE `rent_info`
  ADD CONSTRAINT `rent_info_ibfk_1` FOREIGN KEY (`Apartment_no`) REFERENCES `apartment_details` (`Apartment_no`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tenant_details`
--
ALTER TABLE `tenant_details`
  ADD CONSTRAINT `Test3` FOREIGN KEY (`Apartment_no`) REFERENCES `apartment_details` (`Apartment_no`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
