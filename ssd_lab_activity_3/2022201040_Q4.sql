SELECT d.Dnumber AS "Dept. Id", d.Dname AS "Dept. Name",  COUNT(Dlocation) AS "Number of Locations" 
FROM DEPARTMENT d INNER JOIN DEPT_LOCATIONS dl 
ON d.Dnumber=dl.Dnumber WHERE d.Mgr_ssn IN
(SELECT Essn FROM (SELECT Essn, COUNT(Sex) AS c
FROM DEPENDENT
WHERE SEX="F"
GROUP BY Essn) AS cnt
WHERE c >= 2)
GROUP BY d.Dnumber, d.Dname;