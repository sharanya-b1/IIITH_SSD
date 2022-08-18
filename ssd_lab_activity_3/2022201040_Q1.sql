SELECT  concat(e.Fname," ",e.Minit," ",e.Lname)AS "Full Name", Mgr_ssn AS "ssn", Dnumber AS "Dept. Id", Dname AS "Dept. Name"
FROM DEPARTMENT d JOIN EMPLOYEE e ON e.ssn=d.Mgr_ssn WHERE d.Mgr_ssn IN 
(SELECT Mgr_ssn FROM DEPARTMENT WHERE Dnumber IN 
(SELECT Dno FROM EMPLOYEE e JOIN WORKS_ON w ON e.ssn=w.Essn WHERE w.Hours < 40));
