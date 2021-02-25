-- phpMyAdmin SQL Dump
-- version 3.2.0.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Waktu pembuatan: 17. September 2019 jam 14:38
-- Versi Server: 5.1.37
-- Versi PHP: 5.3.0

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `percobaan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `ID` varchar(10) NOT NULL,
  `UserName` varchar(10) NOT NULL,
  `Password` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`ID`, `UserName`, `Password`) VALUES
('1', 'abi', 'dine'),
('2', '123', '123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `petshop`
--

CREATE TABLE IF NOT EXISTS `petshop` (
  `Kode_Pemilik` varchar(20) NOT NULL,
  `Nama_Pemilik` varchar(25) NOT NULL,
  `Kelas_Pelayanan` varchar(10) NOT NULL,
  `Nama_Hewan` varchar(15) NOT NULL,
  `Jenis_Hewan` varchar(10) NOT NULL,
  `Status_Hewan` varchar(25) NOT NULL,
  `Alamat` varchar(50) NOT NULL,
  PRIMARY KEY (`Kode_Pemilik`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `petshop`
--

INSERT INTO `petshop` (`Kode_Pemilik`, `Nama_Pemilik`, `Kelas_Pelayanan`, `Nama_Hewan`, `Jenis_Hewan`, `Status_Hewan`, `Alamat`) VALUES
('Reg01Ag', 'Edo', 'Reguler', 'lolox', 'Anjing', 'Sudah makan', 'bekasi'),
('VIP02BR', 'ABI', 'VIP', 'CHOPPER', 'Kelinci', 'SUDAH MANDI', 'JAKARTA'),
('PI123', 'BBB', 'VIP', 'AAA', 'Kucing', 'TERIMA KASIH', 'JKT'),
('PI456', 'TEST', 'Reguler', 'TEST', 'Kelinci', 'TEST', 'DPK');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
