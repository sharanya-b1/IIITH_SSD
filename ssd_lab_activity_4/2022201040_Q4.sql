CREATE PROCEDURE `get_details` ()
BEGIN
DECLARE c_name VARCHAR(100);
DECLARE c_city VARCHAR(100);
DECLARE c_country VARCHAR(100);
DECLARE c_grade DECIMAL(12,0);
DECLARE get_info CURSOR FOR SELECT CUST_NAME, WORKING_AREA, CUST_COUNTRY, GRADE FROM customer
WHERE AGENT_CODE LIKE "A00%";
DECLARE CONTINUE HANDLER FOR NOT FOUND SET DONE=TRUE;
CREATE TABLE details(customer_name VARCHAR(100), working_area VARCHAR(100), customer_country VARCHAR(100), grade DECIMAL(12,0));
OPEN get_info;
work_loop : LOOP
	FETCH get_info INTO c_name, c_city, c_country, c_grade;
    IF DONE THEN
    LEAVE work_loop;
    END IF;
    INSERT INTO details VALUES(c_name, c_city, c_country, c_grade);
END LOOP;

SELECT * FROM details;
DROP TABLE details;
CLOSE get_info; 
END