SELECT fname FROM fnames ORDER BY RAND() LIMIT 1 INTO @firstname;
SELECT * FROM letters ORDER BY RAND() LIMIT 1 INTO @minit;
SELECT lname FROM lnames ORDER BY RAND() LIMIT 1 INTO @lastname;
SELECT CONCAT(@firstname,' ',@minit,' ',@lastname);
