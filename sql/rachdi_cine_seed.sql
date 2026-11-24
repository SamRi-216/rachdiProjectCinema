-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: mysql-rachdi-sami.alwaysdata.net
-- Generation Time: Nov 24, 2026 at 10:23 AM
-- Server version: 10.11.18-MariaDB
-- PHP Version: 8.4.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
SET FOREIGN_KEY_CHECKS=0;


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rachdi-sami_salle_cinema`
--

--
-- Dumping data for table `afficheur`
--

INSERT INTO `afficheur` (`id`, `modele`, `definition`, `couleur`, `defilement`) VALUES
(1, 'mc_crypt_590996', '7x80', 1, 1);

--
-- Dumping data for table `capteur`
--

INSERT INTO `capteur` (`id`, `id_salle`, `numero_capteur`, `date_time`) VALUES
(1, 1, 107, '0000-00-00 00:00:00'),
(2, 1, 207, '0000-00-00 00:00:00'),
(3, 2, 202, '0000-00-00 00:00:00'),
(4, 3, 103, '0000-00-00 00:00:00'),
(5, 2, 307, '0000-00-00 00:00:00');

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`id`, `titre`, `duree`, `interdit_-16_ans`, `langue`, `resume`, `affiche`) VALUES
(1, 'Smile 2', '02:12:00', 1, 'VO', 'À l’aube d’une nouvelle tournée mondiale, la star de la pop Skye Riley se met à vivre des événements aussi terrifiants qu’inexplicables. Submergée par la pression de la célébrité et devant un quotidien qui bascule de plus en plus dans l’horreur, Skye est forcée de se confronter à son passé obscur pour tenter de reprendre le contrôle de sa vie avant qu’il ne soit trop tard.', 'affiche-smile.jpg'),
(2, 'Croquette, le chat merveilleux', '01:28:00', 0, 'VF', 'C\'est bien connu, les chats ont plusieurs vies. Croquette vient de gâcher celle de trop et il ferait tout pour retrouver Rose, sa maîtresse adorée. On lui accorde une dernière chance, cependant une règle a changé. Croquette peut revenir, mais à un détail près : désormais transformé en cheval, chien, perroquet ou poisson, l\'aventure ne fait que commencer.', 'affiche-croquette.jpg'),
(3, 'Lee Miller', '01:56:00', 0, 'VF', 'L\'incroyable vie de Lee Miller, ex-modèle pour Vogue et muse de Man Ray devenue l\'une des premières femmes photographes de guerre. Partie sur le front et prête à tout pour témoigner des horreurs de la Seconde Guerre, elle a, par son courage et son refus des conventions, changé la façon de voir le monde.', 'affiche-leemiller.png'),
(4, 'L\'Odyssée', '02:52:00', 0, 'VOSTR', 'L’Odyssée est une épopée mythique tournée à travers le monde qui suit le retour d\'Ulysse vers Ithaque. Pour la première fois, la saga fondatrice d\'Homère est portée sur les écrans de manière spectaculaire avec la toute dernière technologie IMAX.\r\n', 'affiche-odyssee.jpg');

--
-- Dumping data for table `mesure`
--

INSERT INTO `mesure` (`id`, `temperature`, `humidite`, `CO2`, `horodatage`, `id_capteur`) VALUES
(1, 23.00, 75.00, 22000.00, '2026-09-04', 2),
(2, 28.00, 79.00, 25600.00, '2026-09-05', 2),
(3, 27.00, 70.00, 23580.00, '2026-09-06', 1),
(4, 22.00, 78.00, 30251.00, '2026-09-07', 1),
(5, 25.00, 56.00, 34500.00, '2026-09-08', 3),
(6, 26.00, 58.00, 25700.00, '2026-09-09', 4),
(7, 27.00, 67.00, 28560.00, '2026-09-10', 2),
(8, 25.00, 69.00, 31560.00, '2026-09-11', 3),
(9, 24.00, 54.00, 35180.00, '2026-09-12', 1),
(10, 25.00, 78.00, 25600.00, '2026-09-13', 1),
(11, 25.00, 56.00, 22000.00, '2026-09-14', 2),
(12, 26.00, 79.00, 30251.00, '2026-09-15', 4),
(13, 26.00, 78.00, 23580.00, '2026-09-09', 2),
(14, 26.00, 56.00, 25600.00, '2026-09-11', 3),
(15, 28.00, 78.00, 30251.00, '2026-09-08', 3),
(27, 22.02, 51.38, 1344.10, '2026-09-11', 4),
(28, 26.02, 87.61, 1470.92, '2026-09-11', 3),
(29, 27.17, 45.97, 2204.01, '2026-09-11', 1),
(30, 21.60, 84.44, 2079.42, '2026-09-11', 5),
(31, 24.09, 34.49, 2843.64, '2026-09-11', 2),
(32, 24.18, 63.86, 1175.45, '2026-09-11', 2),
(33, 17.16, 74.26, 2793.49, '2026-09-11', 1),
(34, 20.85, 40.27, 2467.09, '2026-09-11', 1),
(35, 17.17, 36.24, 1880.51, '2026-09-11', 2),
(36, 21.10, 11.29, 2874.01, '2026-09-11', 2),
(37, 28.86, 91.62, 2540.15, '2026-09-11', 4),
(38, 15.07, 64.61, 1591.09, '2026-09-11', 2),
(39, 19.01, 45.67, 2648.50, '2026-09-11', 5),
(40, 19.15, 29.25, 651.55, '2026-09-11', 2),
(41, 16.62, 48.75, 2294.80, '2026-09-11', 3),
(42, 22.51, 37.87, 588.10, '2026-09-11', 4),
(43, 15.21, 72.86, 838.46, '2026-09-11', 2),
(44, 26.86, 43.62, 1273.49, '2026-09-11', 3),
(45, 20.84, 80.80, 1818.99, '2026-09-11', 4),
(46, 17.01, 16.27, 2816.37, '2026-09-11', 4),
(47, 22.40, 84.82, 1698.27, '2026-09-11', 2),
(48, 19.47, 30.77, 1732.35, '2026-09-11', 3),
(49, 22.17, 47.36, 1706.02, '2026-09-11', 3),
(50, 15.82, 89.59, 947.76, '2026-09-11', 4),
(51, 21.77, 24.80, 2987.70, '2026-09-11', 4),
(52, 23.01, 38.79, 1268.15, '2026-09-11', 5),
(53, 19.27, 38.70, 2792.10, '2026-09-11', 5),
(54, 15.07, 88.42, 331.23, '2026-09-11', 3),
(55, 22.90, 31.35, 1990.84, '2026-09-11', 2),
(56, 15.23, 27.30, 2715.11, '2026-09-11', 1),
(57, 19.11, 19.71, 2876.18, '2026-09-18', 3),
(58, 22.39, 40.04, 1745.82, '2026-09-18', 2),
(59, 15.16, 15.76, 979.39, '2026-09-18', 3),
(60, 28.11, 43.82, 1041.90, '2026-09-18', 3),
(61, 15.64, 11.66, 1143.77, '2026-09-18', 5),
(62, 26.86, 48.20, 2494.44, '2026-09-18', 1),
(63, 27.94, 82.55, 1365.05, '2026-09-18', 2),
(64, 22.13, 11.49, 636.42, '2026-09-18', 2),
(65, 25.10, 23.59, 1918.39, '2026-09-18', 3),
(66, 28.98, 47.17, 632.03, '2026-09-18', 2),
(67, 26.37, 70.76, 2518.57, '2026-09-18', 2),
(68, 26.63, 70.43, 1513.83, '2026-09-18', 3),
(69, 22.91, 25.01, 1878.83, '2026-09-18', 2),
(70, 20.26, 10.49, 1536.61, '2026-09-18', 4),
(71, 23.42, 13.57, 383.29, '2026-09-18', 4),
(75, 20.90, 21.26, 2529.38, '2026-09-18', 2),
(76, 28.44, 32.93, 1829.37, '2026-09-18', 2),
(77, 24.56, 54.61, 1923.54, '2026-09-18', 2),
(78, 15.95, 11.56, 1421.10, '2026-09-18', 2);

--
-- Dumping data for table `salle`
--

INSERT INTO `salle` (`id`, `numero_salle`, `nb_de_fauteuils`, `place_fauteuils_roulants`, `taille_ecran`, `amenagement_service_propose`, `technologie`, `id_afficheur`) VALUES
(1, 7, 0, 0, '', '', '', 1),
(2, 9, 0, 0, '', '', '', 1),
(3, 5, 0, 0, '', '', '', 1);

--
-- Dumping data for table `seance`
--

INSERT INTO `seance` (`id`, `horaire`, `id_film`, `id_salle`) VALUES
(1, '2026-10-17 14:00:00', 2, 2),
(2, '2026-10-21 00:00:00', 1, 3),
(3, '2026-11-03 00:00:00', 3, 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
