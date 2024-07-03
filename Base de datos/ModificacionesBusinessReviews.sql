use BusinessReviewsDB;
SET global local_infile = 1;

select * from Business;
ALTER TABLE Business
ADD COLUMN State VARCHAR(2);

ALTER TABLE BusinessReviewsDB.Tips
CHANGE COLUMN business_business_id Business_id VARCHAR(100);

DELETE FROM BusinessReviewsDB.Business_Category
WHERE Business_id = 'gmap_id';
DELETE FROM BusinessReviewsDB.Business
WHERE Business_id = 'gmap_id';
DELETE FROM BusinessReviewsDB.Reviews
WHERE Business_id = 'gmap_id';
DELETE FROM BusinessReviewsDB.Reviews
WHERE User_id = "user_id";
DELETE FROM BusinessReviewsDB.Tips
WHERE Business_id = 'gmap_id';
DELETE FROM BusinessReviewsDB.Categories
WHERE Category_id = "0";
UPDATE BusinessReviewsDB.Categories
SET Category = 'Without category'
WHERE Category_id = 1;
DELETE FROM BusinessReviewsDB.Users
WHERE User_id = "user_id";
select * from BusinessReviewsDB.Business_Category WHERE Business_id = 'gmap_id';

select * from BusinessReviewsDB.Business where Business_id = "gmap_id";
select * from BusinessReviewsDB.Reviews where Business_id = "gmap_id";
select * from BusinessReviewsDB.Tips;
select * from BusinessReviewsDB.Categories where Category_id = "1";
select * from BusinessReviewsDB.Users where User_id = "user_id";