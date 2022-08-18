SELECT Essn AS "Manager ssn" , COUNT(DISTINCT(Pno)) AS "Number of projects" FROM WORKS_ON 
WHERE Essn IN (SELECT Mgr_ssn FROM DEPARTMENT WHERE Dnumber IN 
(SELECT Dnum FROM PROJECT WHERE Pname="ProductY"));