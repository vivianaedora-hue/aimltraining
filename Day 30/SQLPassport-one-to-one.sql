create database PassportDb
use PassportDb

CREATE TABLE Person (
    PersonId INT PRIMARY KEY,
    FullName nVARCHAR(100) NOT NULL,
    DOB DATE NOT NULL,
    Nationality nVARCHAR(50) NOT NULL
)

CREATE TABLE Passports (
    PassportId nvarchar(15) primary key,
    PersonId INT NOT NULL unique foreign key references Person,   -- Will link to Person table
    PassportNumber nVARCHAR(50) NOT NULL UNIQUE ,
    IssueDate DATE NOT NULL,
    ExpiryDate DATE NOT NULL)

INSERT INTO Person (PersonId, FullName, DOB, Nationality)
VALUES
(1, 'John Smith', '1990-05-20', 'Canadian'),
(2, 'Amina Rahman', '1985-09-12', 'Malaysian'),
(3, 'Carlos Martinez', '1992-03-10', 'Mexican'),
(4, 'Sarah Johnson', '1998-07-25', 'American'),
(5, 'Priya Sharma', '1995-01-15', 'Indian'),
(6, 'Li Wei', '1988-11-03', 'Chinese')
SELECT * FROM PERSON

INSERT INTO Passports VALUES

(101, 1, 'C1234567', '2020-01-01', '2030-01-01'),
(102, 2, 'M8844221', '2019-06-15', '2029-06-15'),
(103, 3, 'MX5566778', '2021-03-20', '2031-03-20'),
(104, 4, 'US9988776', '2022-07-10', '2032-07-10'),
(105, 5, 'IN5544332', '2018-12-05', '2028-12-05'),
(106, 6, 'CN2233445', '2020-11-01', '2030-11-01')
select * from Passports

select pr.PersonId,pr.FullName,pr.DOB,pr.Nationality,
pp.PassportNumber,pp.ExpiryDate,pp.IssueDate from Passports pp join Person pr  
on pp.PersonId=pr.PersonId