create database PersonsDb
use PersonsDb

-- =============================
-- 1. Create Person Table
-- =============================
CREATE TABLE Person (
    PersonId INT PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    DOB DATE,
    Nationality VARCHAR(50)
);


-- =============================
-- 2. Create Passport Table
-- =============================
CREATE TABLE Passport (
    PassportId INT PRIMARY KEY,
    PersonId INT NOT NULL,   -- Will link to Person table
    PassportNumber VARCHAR(50) UNIQUE NOT NULL,
    IssueDate DATE,
    ExpiryDate DATE,

    -- Enforce 1-to-1 Relationship:
    -- Each PersonId appears only ONCE in Passport
    CONSTRAINT UQ_Passport_Person UNIQUE (PersonId),

    -- Foreign Key (Person must exist first)
    CONSTRAINT FK_Passport_Person FOREIGN KEY (PersonId)
        REFERENCES Person(PersonId)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

INSERT INTO Person (PersonId, FullName, DOB, Nationality)
VALUES
(1, 'John Smith', '1990-05-20', 'Canadian'),
(2, 'Amina Rahman', '1985-09-12', 'Malaysian'),
(3, 'Carlos Martinez', '1992-03-10', 'Mexican'),
(4, 'Sarah Johnson', '1998-07-25', 'American'),
(5, 'Priya Sharma', '1995-01-15', 'Indian'),
(6, 'Li Wei', '1988-11-03', 'Chinese')

INSERT INTO Passport (PassportId, PersonId, PassportNumber, IssueDate, ExpiryDate)
VALUES
(101, 1, 'C1234567', '2020-01-01', '2030-01-01'),
(102, 2, 'M8844221', '2019-06-15', '2029-06-15'),
(103, 3, 'MX5566778', '2021-03-20', '2031-03-20'),
(104, 4, 'US9988776', '2022-07-10', '2032-07-10'),
(105, 5, 'IN5544332', '2018-12-05', '2028-12-05'),
(106, 6, 'CN2233445', '2020-11-01', '2030-11-01')

SELECT p.FullName, s.PassportNumber
FROM Person p
JOIN Passport s ON p.PersonId = s.PersonId;
