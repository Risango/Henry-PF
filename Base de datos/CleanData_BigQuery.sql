SELECT * FROM EXTERNAL_QUERY("vocal-framework-427422-q6.us.reviews_bd", "SELECT * FROM Reviews;");
SELECT * FROM EXTERNAL_QUERY("vocal-framework-427422-q6.us.reviews_bd", "SELECT * FROM Business;");
SELECT * FROM EXTERNAL_QUERY("vocal-framework-427422-q6.us.reviews_bd", "SELECT * FROM Tips;");
SELECT * FROM EXTERNAL_QUERY("vocal-framework-427422-q6.us.reviews_bd", "SELECT * FROM Business_Category;");
SELECT * FROM EXTERNAL_QUERY("vocal-framework-427422-q6.us.reviews_bd", "SELECT * FROM Users;");
SELECT * FROM EXTERNAL_QUERY("vocal-framework-427422-q6.us.reviews_bd", "SELECT * FROM Categories;");


CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.business` AS
SELECT *
FROM EXTERNAL_QUERY(
  "vocal-framework-427422-q6.us.reviews_bd",
  """
  SELECT * FROM Business;
  """
);

CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.reviews` AS
SELECT *
FROM EXTERNAL_QUERY(
  "vocal-framework-427422-q6.us.reviews_bd",
  """
  SELECT * FROM Reviews;
  """
);

CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.categories` AS
SELECT *
FROM EXTERNAL_QUERY(
  "vocal-framework-427422-q6.us.reviews_bd",
  """
  SELECT * FROM Categories;
  """
);

CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.business_category` AS
SELECT *
FROM EXTERNAL_QUERY(
  "vocal-framework-427422-q6.us.reviews_bd",
  """
  SELECT * FROM Business_Category;
  """
);

CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.tips` AS
SELECT *
FROM EXTERNAL_QUERY(
  "vocal-framework-427422-q6.us.reviews_bd",
  """
  SELECT * FROM Tips;
  """
);

CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.users` AS
SELECT *
FROM EXTERNAL_QUERY(
  "vocal-framework-427422-q6.us.reviews_bd",
  """
  SELECT * FROM Users;
  """
);

SELECT * FROM `vocal-framework-427422-q6.Business_Reviews.business` LIMIT 1000;
SELECT * FROM `vocal-framework-427422-q6.Business_Reviews.business_category` LIMIT 1000;
SELECT * FROM `vocal-framework-427422-q6.Business_Reviews.categories` LIMIT 1000;
SELECT * FROM `vocal-framework-427422-q6.Business_Reviews.reviews` LIMIT 1000;
SELECT * FROM `vocal-framework-427422-q6.Business_Reviews.tips` LIMIT 1000;
SELECT * FROM `vocal-framework-427422-q6.Business_Reviews.users` LIMIT 1000;

DELETE
FROM `vocal-framework-427422-q6.Business_Reviews.categories` where Category_id >= 4414;

DELETE
FROM `vocal-framework-427422-q6.Business_Reviews.categories` where Category_id >= 4414;

CREATE OR REPLACE TABLE `vocal-framework-427422-q6.Business_Reviews.categories`
AS
SELECT DISTINCT *
FROM `vocal-framework-427422-q6.Business_Reviews.categories`;
