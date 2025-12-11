-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : mysql
-- Généré le : jeu. 11 déc. 2025 à 10:55
-- Version du serveur : 8.2.0
-- Version de PHP : 8.0.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `library`
--

-- --------------------------------------------------------

--
-- Structure de la table `adherent`
--

CREATE TABLE `adherent` (
  `num_adherent` int NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL,
  `adresse` varchar(50) DEFAULT NULL,
  `date_adhesion` varchar(50) DEFAULT NULL,
  `id_user` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `adherent`
--

INSERT INTO `adherent` (`num_adherent`, `nom`, `prenom`, `adresse`, `date_adhesion`, `id_user`) VALUES
(1, 'Dupont', 'Alice', NULL, '2023-01-15', 2),
(2, 'Durand', 'Benoit', NULL, '2023-03-20', 3),
(3, 'Petit', 'Claire', NULL, '2024-02-10', 4);

-- --------------------------------------------------------

--
-- Structure de la table `auteur`
--

CREATE TABLE `auteur` (
  `id_auteur` int NOT NULL,
  `nom` varchar(50) DEFAULT NULL,
  `prenom` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `auteur`
--

INSERT INTO `auteur` (`id_auteur`, `nom`, `prenom`) VALUES
(10, 'Verne', 'Jules'),
(20, 'Hugo', 'Victor'),
(30, 'Rowling', 'J.K.');

-- --------------------------------------------------------

--
-- Structure de la table `ecrire`
--

CREATE TABLE `ecrire` (
  `isbn` varchar(100) NOT NULL,
  `id_auteur` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `ecrire`
--

INSERT INTO `ecrire` (`isbn`, `id_auteur`) VALUES
('ISBN1', 10),
('ISBN4', 10),
('ISBN3', 20),
('ISBN2', 30);

-- --------------------------------------------------------

--
-- Structure de la table `emprunt`
--

CREATE TABLE `emprunt` (
  `num_adherent` int NOT NULL,
  `num_inventaire` varchar(50) NOT NULL,
  `date_emprunt` date DEFAULT NULL,
  `date_retour_prevue` date DEFAULT NULL,
  `date_retour_effective` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `emprunt`
--

INSERT INTO `emprunt` (`num_adherent`, `num_inventaire`, `date_emprunt`, `date_retour_prevue`, `date_retour_effective`) VALUES
(1, 'E001', '2024-11-20', '2024-12-11', NULL),
(2, 'E003', '2024-10-01', '2024-10-22', '2024-10-20');

-- --------------------------------------------------------

--
-- Structure de la table `exemplaire`
--

CREATE TABLE `exemplaire` (
  `num_inventaire` varchar(50) NOT NULL,
  `type_usage` enum('vente','prêt') NOT NULL,
  `isbn` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `exemplaire`
--

INSERT INTO `exemplaire` (`num_inventaire`, `type_usage`, `isbn`) VALUES
('E001', 'prêt', 'ISBN1'),
('E002', 'vente', 'ISBN1'),
('E003', 'prêt', 'ISBN2'),
('E004', 'prêt', 'ISBN4');

-- --------------------------------------------------------

--
-- Structure de la table `livre`
--

CREATE TABLE `livre` (
  `isbn` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `resume` text,
  `titre` varchar(50) DEFAULT NULL,
  `annee_publication` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `livre`
--

INSERT INTO `livre` (`isbn`, `resume`, `titre`, `annee_publication`) VALUES
('ISBN1', '', 'Vingt mille lieues sous les mers', 1870),
('ISBN2', '', 'Harry Potter à l\'école des sorciers', 1997),
('ISBN3', '', 'Les Misérables', 1862),
('ISBN4', '', 'Voyage au centre de la Terre', 1864);

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id_user` int NOT NULL,
  `username` varchar(80) DEFAULT NULL,
  `email` varchar(120) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `role` enum('user','admin') DEFAULT NULL,
  `created_at` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id_user`, `username`, `email`, `password`, `role`, `created_at`) VALUES
(1, 'Patrick', 'patrick.croquet@afpa.fr', 'f46463712f38c3198c18624ddf71130c01d847b26335262d6bc7ab6dca72a30abc1452a69fcca4e5f47ac941e48840bf', 'admin', '2025-12-04'),
(2, 'Alice', 'alice.dupont@afpa.fr', 'f46463712f38c3198c18624ddf71130c01d847b26335262d6bc7ab6dca72a30abc1452a69fcca4e5f47ac941e48840bf', 'user', '2025-12-11'),
(3, 'Benoit', 'benoit.durand@afpa.fr', 'f46463712f38c3198c18624ddf71130c01d847b26335262d6bc7ab6dca72a30abc1452a69fcca4e5f47ac941e48840bf', 'user', '2025-12-11'),
(4, 'Claire', 'claire.petit@afpa.fr', 'f46463712f38c3198c18624ddf71130c01d847b26335262d6bc7ab6dca72a30abc1452a69fcca4e5f47ac941e48840bf', 'user', '2025-12-11');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `adherent`
--
ALTER TABLE `adherent`
  ADD PRIMARY KEY (`num_adherent`),
  ADD UNIQUE KEY `id_user` (`id_user`);

--
-- Index pour la table `auteur`
--
ALTER TABLE `auteur`
  ADD PRIMARY KEY (`id_auteur`);

--
-- Index pour la table `ecrire`
--
ALTER TABLE `ecrire`
  ADD PRIMARY KEY (`isbn`,`id_auteur`),
  ADD KEY `ecrire_ibfk_2` (`id_auteur`);

--
-- Index pour la table `emprunt`
--
ALTER TABLE `emprunt`
  ADD PRIMARY KEY (`num_adherent`,`num_inventaire`),
  ADD KEY `num_inventaire` (`num_inventaire`);

--
-- Index pour la table `exemplaire`
--
ALTER TABLE `exemplaire`
  ADD PRIMARY KEY (`num_inventaire`),
  ADD KEY `exemplaire_ibfk_1` (`isbn`);

--
-- Index pour la table `livre`
--
ALTER TABLE `livre`
  ADD PRIMARY KEY (`isbn`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `adherent`
--
ALTER TABLE `adherent`
  ADD CONSTRAINT `adherent_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`);

--
-- Contraintes pour la table `ecrire`
--
ALTER TABLE `ecrire`
  ADD CONSTRAINT `ecrire_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `livre` (`isbn`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  ADD CONSTRAINT `ecrire_ibfk_2` FOREIGN KEY (`id_auteur`) REFERENCES `auteur` (`id_auteur`) ON DELETE RESTRICT ON UPDATE RESTRICT;

--
-- Contraintes pour la table `emprunt`
--
ALTER TABLE `emprunt`
  ADD CONSTRAINT `emprunt_ibfk_1` FOREIGN KEY (`num_adherent`) REFERENCES `adherent` (`num_adherent`),
  ADD CONSTRAINT `emprunt_ibfk_2` FOREIGN KEY (`num_inventaire`) REFERENCES `exemplaire` (`num_inventaire`);

--
-- Contraintes pour la table `exemplaire`
--
ALTER TABLE `exemplaire`
  ADD CONSTRAINT `exemplaire_ibfk_1` FOREIGN KEY (`isbn`) REFERENCES `livre` (`isbn`) ON DELETE RESTRICT ON UPDATE RESTRICT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
