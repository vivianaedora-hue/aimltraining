create database ProductSalesDb
use ProductSalesDb

create table Products
(ProductId nvarchar(50) primary key,
ProductName nvarchar(50) not null,
Category nvarchar(50),
UnitPrice decimal (10,2)
)

create table Sales
(SalesId nvarchar(10) primary key,
ProductId nvarchar(50) not null foreign key references Products,
Quantity int not null,
TotalAmount decimal(12,2),
SalesDate Date
)
insert into Products values ('P-001','Laptop','Electronics',12000)
insert into Products values
('P-002','Washing Machine','Electronics',12000),
('P-003','Nothing-3a','Electronics',1800),
('P-004','Office Chair','Furniture',500.50),
('P-005','Office Desk','Electronics',700.25),
('P-006','Headphone','Electronics',150),
('P-007','Touch screen','Electronics',2000),
('P-010','Iphone-17','Mobile',5800)
select * from Products
--drop table Sales
--create table Sales
--(SalesId nvarchar(10) primary key,
--ProductId nvarchar(50) not null foreign key references Products,
--Quantity int not null,
--TotalAmount decimal (12,2),
--SalesDate date
--)
insert into Sales(SalesId,ProductId,Quantity,TotalAmount,SalesDate)
values
('Sid-001','P-001',2,2400,'2025-11-17')
--
insert into Sales(SalesId,ProductId,Quantity,TotalAmount,SalesDate)
values
('Sid-002','P-002',3,4500,'2025-11-17'),
('Sid-003','P-003',2,3600,'2025-10-17'),
('Sid-004','P-004',1,500.50,'2025-10-17'),
('Sid-005','P-005',1,700.25,'2025-11-17'),
('Sid-006','P-006',2,300,'2025-09-17'),
('Sid-007','P-007',3,6000,'2025-09-10'),
('Sid-008','P-010',2,1160,'2025-09-10')
select * from Sales
select s.SalesId,s.SalesDate,p.ProductId,p.ProductName,s.Quantity,p.UnitPrice,s.TotalAmount
 from Sales s,Products p 
 where p.ProductId=s.ProductId



