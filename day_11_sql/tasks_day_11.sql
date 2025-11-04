


-- TASK 1: use SELECT:

SELECT * FROM sqltsk.sony;

--------------------------------------------------------------------------------------
-- TASK 1.1: Variasion of selects

SELECT
	name,
	publisher,
	developer,
	total_sales
FROM sqltsk.sony 
WHERE last_update IS NOT NULL;

--------------------------------------------------------------------------------------
-- TASK 2 : custom insert

INSERT INTO sqltsk.sony (name,publisher) VALUES ('FZ','OP'),('as','aw');

SELECT * FROM sqltsk.sony WHERE name = 'FZ';

--------------------------------------------------------------------------------------
-- TASK 3 : update record

UPDATE sqltsk.sony SET developer = 'OPZ' WHERE name = 'FZ';

SELECT * FROM sqltsk.sony WHERE name = 'FZ';
--------------------------------------------------------------------------------------
-- TASK 4 : delete record in the table

DELETE FROM sqltsk.sony WHERE name = 'FZ';

SELECT * FROM sqltsk.sony WHERE name = 'FZ';