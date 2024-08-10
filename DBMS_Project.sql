CREATE DATABASE DbProject;

USE DbProject;

-- User Table
CREATE TABLE Users (
    User_id INT PRIMARY KEY,
    Username VARCHAR(30),
    Password VARCHAR(30),
    isAdmin BOOL,
    isVerified BOOL,
    Email VARCHAR(30)
);

-- Category Table
CREATE TABLE Category (
    Category_id INT PRIMARY KEY,
    Name VARCHAR(30)
);

-- Sub-Category Table
CREATE TABLE Sub_Category (
    Sub_Category_id INT PRIMARY KEY,
    Name VARCHAR(30),
    Category_id INT,
    FOREIGN KEY (Category_id) REFERENCES Category(Category_id)
);

-- Order Table
CREATE TABLE Orders (
    Order_id INT PRIMARY KEY,
    User_id INT,
    Order_Date DATE,
    Price DECIMAL(10, 2),
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

-- Order_Product Junction Table
CREATE TABLE Order_Product (
    Order_id INT,
    Product_id INT,
    PRIMARY KEY (Order_id, Product_id),
    FOREIGN KEY (Order_id) REFERENCES Orders(Order_id),
    FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);

-- Product Table
CREATE TABLE Product (
    Product_id INT PRIMARY KEY,
    Sub_Category_id INT,
    Brand_id INT,
    Rating INT,
    Quantity INT,
    Name VARCHAR(30),	
    Price DECIMAL(10, 2),
    FOREIGN KEY (Sub_Category_id) REFERENCES Sub_Category(Sub_Category_id),
    FOREIGN KEY (Brand_id) REFERENCES Brand(Brand_id)
);

-- Payment Table
CREATE TABLE Payment (
    Payment_id INT PRIMARY KEY,
    Order_id INT,
    Price DECIMAL(10, 2),
    isCompleted BOOL,
    FOREIGN KEY (Order_id) REFERENCES Orders(Order_id)
);

-- Address Table
CREATE TABLE Address (
    Address_id INT PRIMARY KEY,
    City VARCHAR(50),
    Country VARCHAR(50),
    Postal_Code INT,
    Street VARCHAR(50)
);

-- Shipment Table
CREATE TABLE Shipment (
    Shipment_id INT PRIMARY KEY,
    Order_id INT,
    Date DATE,
    isCompleted BOOL,
    FOREIGN KEY (Order_id) REFERENCES Orders(Order_id)
);


-- Shipment_Address Junction Table
CREATE TABLE Shipment_Address (
    Shipment_id INT,
    Address_id INT,
    PRIMARY KEY (Shipment_id, Address_id),
    FOREIGN KEY (Shipment_id) REFERENCES Shipment(Shipment_id),
    FOREIGN KEY (Address_id) REFERENCES Address(Address_id)
);

-- Cart Table
CREATE TABLE Cart (
    Cart_id INT PRIMARY KEY,
    User_id INT,
    Total_Price DECIMAL(10, 2),
    isCheckedOut BOOL,
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

-- Cart_Product Junction Table
CREATE TABLE Cart_Product (
    Cart_id INT,
    Product_id INT,
    PRIMARY KEY (Cart_id, Product_id),
    FOREIGN KEY (Cart_id) REFERENCES Cart(Cart_id),
    FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);

-- Vendor Table
CREATE TABLE Vendor (
    Vendor_id INT PRIMARY KEY,
    Name VARCHAR(30)
);

-- Feedback Table
CREATE TABLE Feedback (
    Feedback_id INT PRIMARY KEY,
    Product_id INT,
    User_id INT,
    Description VARCHAR(50),
    FOREIGN KEY (Product_id) REFERENCES Product(Product_id),
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

-- Brand Table
CREATE TABLE Brand (
    Brand_id INT PRIMARY KEY,
    Name VARCHAR(30)
);

-- Store Table
CREATE TABLE Store (
    Store_id INT PRIMARY KEY,
    Vendor_id INT,
    Capacity INT,
    FOREIGN KEY (Vendor_id) REFERENCES Vendor(Vendor_id)
);

-- Rating Table
CREATE TABLE Rating (
    Rating_id INT PRIMARY KEY,
    Product_id INT,
    User_id INT,
    Rate INT,
    FOREIGN KEY (Product_id) REFERENCES Product(Product_id),
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

-- Coupon Table
CREATE TABLE Coupon (
    Coupon_Code VARCHAR(20) PRIMARY KEY,
    Discount DECIMAL(10, 2),
    Valid_till DATE,
    Copies INT,
    Product_id INT,
    FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);

-- Wishlist Table
CREATE TABLE Wishlist (
    Wishlist_id INT PRIMARY KEY,
    User_id INT,
    FOREIGN KEY (User_id) REFERENCES Users(User_id)
);

-- Sales_Product Junction Table
CREATE TABLE Sales_Product (
    Sales_id INT,
    Product_id INT,
    PRIMARY KEY (Sales_id, Product_id),
    FOREIGN KEY (Sales_id) REFERENCES Sales(Sales_id),
    FOREIGN KEY (Product_id) REFERENCES Product(Product_id)
);

-- Analytics Table
CREATE TABLE Analytics (
    Analytics_id INT PRIMARY KEY,
    Store_id INT,
    Time_Period DATE,
    FOREIGN KEY (Store_id) REFERENCES Store(Store_id)
);

CREATE TABLE Analytics_Sales (
    Analytics_id INT,
    Sales_id INT,
    PRIMARY KEY (Analytics_id, Sales_id),
    FOREIGN KEY (Analytics_id) REFERENCES Analytics(Analytics_id),
    FOREIGN KEY (Sales_id) REFERENCES Sales(Sales_id)
);

-- Sales Table
CREATE TABLE Sales (
    Sales_id INT PRIMARY KEY,
    Sale_Amount DECIMAL(10, 2),
    Time_Period DATE
);



-- Insert 10 rows into the Users table
INSERT INTO Users (User_id, Username, Password, isAdmin, isVerified, Email)
VALUES
    (1, 'user1', 'password1', false, true, 'user1@example.com'),
    (2, 'user2', 'password2', false, true, 'user2@example.com'),
    (3, 'user3', 'password3', false, true, 'user3@example.com'),
    (4, 'user4', 'password4', false, true, 'user4@example.com'),
    (5, 'user5', 'password5', false, true, 'user5@example.com'),
    (6, 'user6', 'password6', false, true, 'user6@example.com'),
    (7, 'user7', 'password7', false, true, 'user7@example.com'),
    (8, 'user8', 'password8', false, true, 'user8@example.com'),
    (9, 'user9', 'password9', false, true, 'user9@example.com'),
    (10, 'user10', 'password10', false, true, 'user10@example.com');

-- Insert 10 rows into the Category table
INSERT INTO Category (Category_id, Name)
VALUES
    (1, 'Electronics'),
    (2, 'Fashion'),
    (3, 'Home'),
    (4, 'Sports'),
    (5, 'Beauty'),
    (6, 'Food'),
    (7, 'Travel'),
    (8, 'Baby'),
    (9, 'Pet'),
    (10, 'Outdoor');

-- Insert 10 rows into the Sub_Category table
INSERT INTO Sub_Category (Sub_Category_id, Name, Category_id)
VALUES
    (1, 'Smartphones', 1),
    (2, 'Laptops', 1),
    (3, 'T-Shirts', 2),
    (4, 'Jeans', 2),
    (5, 'Furniture', 3),
    (6, 'Soccer', 4),
    (7, 'Makeup', 5),
    (8, 'Coffee', 6),
    (9, 'Strollers', 8),
    (10, 'Toys', 9);

-- Insert 10 rows into the Orders table
INSERT INTO Orders (Order_id, User_id, Order_Date, Price)
VALUES
    (1, 1, '2022-01-01', 100.00),
    (2, 2, '2022-01-15', 200.00),
    (3, 3, '2022-02-01', 300.00),
    (4, 4, '2022-03-01', 400.00),
    (5, 5, '2022-04-01', 500.00),
    (6, 6, '2022-05-01', 600.00),
    (7, 7, '2022-06-01', 700.00),
    (8, 8, '2022-07-01', 800.00),
    (9, 9, '2022-08-01', 900.00),
    (10, 10, '2022-09-01', 1000.00);
    
-- Insert 10 rows into the Order_product table
INSERT INTO Order_product (Order_id, Product_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Insert 10 rows into the Product table
INSERT INTO Product (Product_id, Sub_Category_id, Brand_id, Rating, Quantity, Name, Price)
VALUES
    (1, 1, 1, 4, 10, 'Product A', 100.00),
    (2, 2, 2, 4, 10, 'Product B', 200.00),
    (3, 3, 3, 4, 10, 'Product C', 300.00),
    (4, 4, 4, 4, 10, 'Product D', 400.00),
    (5, 5, 5, 4, 10, 'Product E', 500.00),
    (6, 6, 6, 4, 10, 'Product F', 600.00),
    (7, 7, 7, 4, 10, 'Product G', 700.00),
    (8, 8, 8, 4, 10, 'Product H', 800.00),
    (9, 9, 9, 4, 10, 'Product I', 900.00),
    (10, 10, 10, 4, 10, 'Product J', 1000.00);

-- Insert 10 rows into the Payment table
INSERT INTO Payment (Payment_id, Order_id, Price, isCompleted)
VALUES
    (1, 1, 100.00, true),
    (2, 2, 200.00, true),
    (3, 3, 300.00, true),
    (4, 4, 400.00, true),
    (5, 5, 500.00, true),
    (6, 6, 600.00, true);
    
-- Insert 10 rows into the Address table
INSERT INTO Address (Address_id, City, Country, Postal_Code, Street)
VALUES
    (1, 'New York', 'USA', 10001, '123 Main St'),
    (2, 'Los Angeles', 'USA', 90001, '456 Elm St'),
    (3, 'Chicago', 'USA', 60601, '789 Oak St'),
    (4, 'Houston', 'USA', 77001, '321 Maple St'),
    (5, 'Phoenix', 'USA', 85001, '901 Palm St'),
    (6, 'Philadelphia', 'USA', 19101, '654 Spruce St'),
    (7, 'San Antonio', 'USA', 78201, '567 Alamo St'),
    (8, 'San Diego', 'USA', 92101, '234 Beach St'),
    (9, 'Dallas', 'USA', 75201, '8900 Dallas St'),
    (10, 'San Jose', 'USA', 95101, '567 Silicon St');
    
-- Insert 10 rows into the Shipment table
INSERT INTO Shipment (Shipment_id, Order_id, Date, isCompleted)
VALUES
    (1, 1, '2022-01-02', true),
    (2, 2, '2022-01-16', true),
    (3, 3, '2022-02-02', true),
    (4, 4, '2022-03-02', true),
    (5, 5, '2022-04-02', true),
    (6, 6, '2022-05-02', true),
    (7, 7, '2022-06-02', true),
    (8, 8, '2022-07-02', true),
    (9, 9, '2022-08-02', true),
    (10, 10, '2022-09-02', true);


-- Insert 10 rows into the Shipment_Address table
INSERT INTO Shipment_Address (Shipment_id, Address_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Insert 10 rows into the Cart table
INSERT INTO Cart (Cart_id, User_id, Total_Price, isCheckedOut)
VALUES
    (1, 1, 100.00, false),
    (2, 2, 200.00, false),
    (3, 3, 300.00, false),
    (4, 4, 400.00, false),
    (5, 5, 500.00, false),
    (6, 6, 600.00, false),
    (7, 7, 700.00, false),
    (8, 8, 800.00, false),
    (9, 9, 900.00, false),
    (10, 10, 1000.00, false);

-- Insert 10 rows into the Cart_Product table
INSERT INTO Cart_Product (Cart_id, Product_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Insert 10 rows into the Vendor table
INSERT INTO Vendor (Vendor_id, Name)
VALUES
    (1, 'Vendor A'),
    (2, 'Vendor B'),
    (3, 'Vendor C'),
    (4, 'Vendor D'),
    (5, 'Vendor E'),
    (6, 'Vendor F'),
    (7, 'Vendor G'),
    (8, 'Vendor H'),
    (9, 'Vendor I'),
    (10, 'Vendor J');

-- Insert 10 rows into the Feedback table
INSERT INTO Feedback (Feedback_id, Product_id, User_id, Description)
VALUES
    (1, 1, 1, 'Great product!'),
    (2, 2, 2, 'Good product.'),
    (3, 3, 3, 'Excellent product!'),
    (4, 4, 4, 'Average product.'),
    (5, 5, 5, 'Poor product.'),
    (6, 6, 6, 'Great product!'),
    (7, 7, 7, 'Good product.'),
    (8, 8, 8, 'Excellent product!'),
    (9, 9, 9, 'Average product.'),
    (10, 10, 10, 'Poor product.');

-- Insert 10 rows into the Brand table
INSERT INTO Brand (Brand_id, Name)
VALUES
    (1, 'Brand A'),
    (2, 'Brand B'),
    (3, 'Brand C'),
    (4, 'Brand D'),
    (5, 'Brand E'),
    (6, 'Brand F'),
    (7, 'Brand G'),
    (8, 'Brand H'),
    (9, 'Brand I'),
    (10, 'Brand J');

-- Insert 10 rows into the Store table
INSERT INTO Store (Store_id, Vendor_id, Capacity)
VALUES
    (1, 1, 100),
    (2, 2, 200),
    (3, 3, 300),
    (4, 4, 400),
    (5, 5, 500),
    (6, 6, 600),
    (7, 7, 700),
    (8, 8, 800),
    (9, 9, 900),
    (10, 10, 1000);
    
-- Insert 10 rows into the Rating table
INSERT INTO Rating (Rating_id, Product_id, User_id, Rate)
VALUES
    (1, 1, 1, 5),
    (2, 2, 2, 4),
    (3, 3, 3, 5),
    (4, 4, 4, 4),
    (5, 5, 5, 5),
    (6, 6, 6, 4),
    (7, 7, 7, 5),
    (8, 8, 8, 4),
    (9, 9, 9, 5),
    (10, 10, 10, 5);

-- Insert 10 rows into the Coupon table
INSERT INTO Coupon (Coupon_Code, Discount, Valid_till, Copies, Product_id)
VALUES
    ('COUPON1', 10.00, '2022-12-31', 10, 1),
    ('COUPON2', 20.00, '2022-12-31', 10, 2),
    ('COUPON3', 30.00, '2022-12-31', 10, 3),
    ('COUPON4', 40.00, '2022-12-31', 10, 4),
    ('COUPON5', 50.00, '2022-12-31', 10, 5),
    ('COUPON6', 60.00, '2022-12-31', 10, 6),
    ('COUPON7', 70.00, '2022-12-31', 10, 7),
    ('COUPON8', 80.00, '2022-12-31', 10, 8),
    ('COUPON9', 90.00, '2022-12-31', 10, 9),
    ('COUPON10', 100.00, '2022-12-31', 10, 10);

-- Insert 10 rows into the Wishlist table
INSERT INTO Wishlist (Wishlist_id, User_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Insert 10 rows into the Sales_Product table
INSERT INTO Sales_Product (Sales_id, Product_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Insert 10 rows into the Analytics table
INSERT INTO Analytics (Analytics_id, Store_id, Time_Period)
VALUES
    (1, 1, '2022-01-01'),
    (2, 2, '2022-01-15'),
    (3, 3, '2022-02-01'),
    (4, 4, '2022-03-01'),
    (5, 5, '2022-04-01'),
    (6, 6, '2022-05-01'),
    (7, 7, '2022-06-01'),
    (8, 8, '2022-07-01'),
    (9, 9, '2022-08-01'),
    (10, 10, '2022-09-01');

-- Insert 10 rows into the Analytics_Sales table
INSERT INTO Analytics_Sales (Analytics_id, Sales_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 9),
    (10, 10);

-- Insert 10 rows into the Sales table
INSERT INTO Sales (Sales_id, Sale_Amount, Time_Period)
VALUES
    (1, 100.00, '2022-01-01'),
    (2, 200.00, '2022-01-15'),
    (3, 300.00, '2022-02-01'),
    (4, 400.00, '2022-03-01'),
    (5, 500.00, '2022-04-01'),
    (6, 600.00, '2022-05-01'),
    (7, 700.00, '2022-06-01'),
    (8, 800.00, '2022-07-01'),
    (9, 900.00, '2022-08-01'),
    (10, 1000.00, '2022-09-01');
    
USE DbProject;
-- Select
SELECT Product_id, Price
FROM Product;

SELECT Order_date, Price
FROM Orders;

SELECT Username, Email
FROM Users;

-- Where
SELECT *
FROM Orders
WHERE Price > 100;

SELECT *
FROM Product
WHERE Price < 500;

SELECT *
FROM Users
WHERE Email = 'user5@example.com';

-- Single Row Function queries
SELECT MAX(Price)
FROM Product;

SELECT MIN(Price)
FROM Orders;

SELECT AVG(Rating)
FROM Product;

-- JOINING queries
SELECT *
FROM Orders
JOIN Users
ON Orders.user_id = users.user_id;

SELECT *
FROM Product
LEFT JOIN Order_product
ON Product.Product_id = Order_product.Product_id;

SELECT *
FROM Order_product
JOIN Orders
ON Order_product.Order_id = Orders.Order_id;


-- SUBQUERY queries
SELECT *
FROM Orders
WHERE Price > (
  SELECT AVG(Price)
  FROM Orders
);

SELECT *
FROM Product
WHERE Price > (
  SELECT MIN(Price)
  FROM Product
  WHERE sub_Category_id = 1
);

SELECT *
FROM Users
WHERE User_id IN (
  SELECT User_id
  FROM Orders
  WHERE Price > 100
);

-- GROUP FUNCTION queries
SELECT User_id, SUM(Price)
FROM Orders
GROUP BY User_id;

SELECT Sub_category_id, AVG(Price)
FROM Product
GROUP BY Sub_category_id;

SELECT Order_date, SUM(Price)
FROM Orders
GROUP BY Order_date;

-- Create the Admin user
CREATE USER 'admin_user'@'localhost' IDENTIFIED BY 'admin_password';

-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO 'admin_user'@'localhost';

-- Create the Moderator user
CREATE USER 'moderator_user'@'localhost' IDENTIFIED BY 'moderator_password';

-- Grant privileges
GRANT SELECT, INSERT, UPDATE, DELETE ON dbProject.* TO 'moderator_user'@'localhost';

-- Create the Sales Representative user
CREATE USER 'sales_user'@'localhost' IDENTIFIED BY 'sales_password';

-- Grant privileges
GRANT SELECT, INSERT, UPDATE ON dbproject.orders TO 'sales_user'@'localhost';

-- Create the Customer Service Representative user
CREATE USER 'cs_user'@'localhost' IDENTIFIED BY 'cs_password';

-- Grant privileges
GRANT SELECT, UPDATE ON dbproject.users TO 'cs_user'@'localhost';

-- Create the Inventory Manager user
CREATE USER 'inventory_user'@'localhost' IDENTIFIED BY 'inventory_password';

-- Grant privileges
GRANT SELECT, UPDATE ON dbproject.product TO 'inventory_user'@'localhost';

-- Create the Accountant user
CREATE USER 'accountant_user'@'localhost' IDENTIFIED BY 'accountant_password';

-- Grant privileges
GRANT SELECT ON dbproject.sales TO 'accountant_user'@'localhost';
GRANT SELECT ON dbproject.analytics TO 'accountant_user'@'localhost';
GRANT SELECT ON dbproject.analytics_sales  TO 'accountant_user'@'localhost';















