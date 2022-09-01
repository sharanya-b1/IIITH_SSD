CREATE DEFINER=`root`@`localhost` PROCEDURE `add_two_nums`(IN num1 INT, IN num2 INT, OUT output INT)
BEGIN
SELECT num1+num2 INTO output;
END