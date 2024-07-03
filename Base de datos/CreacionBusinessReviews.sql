-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema BusinessReviewsDB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BusinessReviewsDB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BusinessReviewsDB` DEFAULT CHARACTER SET utf8 ;
USE `BusinessReviewsDB` ;

-- -----------------------------------------------------
-- Table `BusinessReviewsDB`.`Business`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BusinessReviewsDB`.`Business` (
  `Business_id` VARCHAR(100) NOT NULL,
  `Name` VARCHAR(45) NULL,
  `Address` VARCHAR(45) NULL,
  `Latitude` FLOAT NULL,
  `Longitude` FLOAT NULL,
  `Rating` FLOAT NULL,
  `Review_count` INT NULL,
  PRIMARY KEY (`Business_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BusinessReviewsDB`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BusinessReviewsDB`.`Users` (
  `User_id` VARCHAR(100) NOT NULL,
  `Name` VARCHAR(50) NULL,
  PRIMARY KEY (`User_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BusinessReviewsDB`.`Reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BusinessReviewsDB`.`Reviews` (
  `Review_id` VARCHAR(22) NULL,
  `Business_id` VARCHAR(100) NOT NULL,
  `User_id` VARCHAR(100) NOT NULL,
  `Rating` FLOAT NULL,
  `Text` VARCHAR(250) NULL,
  `Date` DATE NULL,
  PRIMARY KEY (`Review_id`, `Business_id`, `User_id`),
  INDEX `fk_Reviews_Business_idx` (`Business_id` ASC) VISIBLE,
  INDEX `fk_Reviews_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Reviews_Business`
    FOREIGN KEY (`Business_id`)
    REFERENCES `BusinessReviewsDB`.`Business` (`Business_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Reviews_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `BusinessReviewsDB`.`Users` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BusinessReviewsDB`.`Categories`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BusinessReviewsDB`.`Categories` (
  `Category_id` INT NOT NULL,
  `Category` VARCHAR(45) NULL,
  PRIMARY KEY (`Category_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BusinessReviewsDB`.`Business_Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BusinessReviewsDB`.`Business_Category` (
  `Business_Category_Id` INT NOT NULL,
  `Business_id` VARCHAR(100) NOT NULL,
  `Category_id` INT NOT NULL,
  PRIMARY KEY (`Business_Category_Id`, `Business_id`, `Category_id`),
  INDEX `fk_Business_Category_Business1_idx` (`Business_id` ASC) VISIBLE,
  INDEX `fk_Business_Category_Categories1_idx` (`Category_id` ASC) VISIBLE,
  CONSTRAINT `fk_Business_Category_Business1`
    FOREIGN KEY (`Business_id`)
    REFERENCES `BusinessReviewsDB`.`Business` (`Business_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Business_Category_Categories1`
    FOREIGN KEY (`Category_id`)
    REFERENCES `BusinessReviewsDB`.`Categories` (`Category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BusinessReviewsDB`.`Tips`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BusinessReviewsDB`.`Tips` (
  `Tip_id` INT NOT NULL,
  `Business_Business_id` VARCHAR(100) NOT NULL,
  `User_id` VARCHAR(100) NOT NULL,
  `Text` VARCHAR(150) NULL,
  `Date` DATETIME NULL,
  `Compliment_count` INT NULL,
  PRIMARY KEY (`Tip_id`, `Business_Business_id`, `User_id`),
  INDEX `fk_Tips_Business1_idx` (`Business_Business_id` ASC) VISIBLE,
  INDEX `fk_Tips_Users1_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Tips_Business1`
    FOREIGN KEY (`Business_Business_id`)
    REFERENCES `BusinessReviewsDB`.`Business` (`Business_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Tips_Users1`
    FOREIGN KEY (`User_id`)
    REFERENCES `BusinessReviewsDB`.`Users` (`User_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
