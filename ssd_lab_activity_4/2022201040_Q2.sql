CREATE DEFINER=`root`@`localhost` PROCEDURE `people_in_city`(IN city_name VARCHAR(30))
BEGIN
SELECT CUST_NAME FROM customer WHERE WORKING_AREA=city_name;
END