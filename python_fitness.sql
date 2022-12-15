-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema python_fitness
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `python_fitness` ;

-- -----------------------------------------------------
-- Schema python_fitness
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `python_fitness` DEFAULT CHARACTER SET utf8mb3 ;
USE `python_fitness` ;

-- -----------------------------------------------------
-- Table `python_fitness`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `python_fitness`.`users` ;

CREATE TABLE IF NOT EXISTS `python_fitness`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(200) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `python_fitness`.`records`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `python_fitness`.`records` ;

CREATE TABLE IF NOT EXISTS `python_fitness`.`records` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NULL DEFAULT NULL,
  `food` VARCHAR(100) NULL DEFAULT NULL,
  `meal` VARCHAR(45) NULL DEFAULT NULL,
  `calories_cal` INT NULL DEFAULT NULL,
  `carbs_g` INT NULL DEFAULT NULL,
  `fat_g` INT NULL DEFAULT NULL,
  `protein_g` INT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_records_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_records_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `python_fitness`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 18
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
