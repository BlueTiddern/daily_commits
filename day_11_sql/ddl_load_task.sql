
/*

This is the T-SQL script to create Database 
Load the table from a csv

*/

-- creating a database of it does not exist

IF NOT EXISTS (

	SELECT 1 FROM sys.databases WHERE name = 'TaskDB'

)
BEGIN
	CREATE DATABASE TaskDB;
	PRINT 'DataBase Created';
END
ELSE
BEGIN
	PRINT 'DB is already created and ready to use';
END;
GO

USE TaskDB;
GO

-- Checking if the schema is created and creating the schema

IF NOT EXISTS (
	
	SELECT 1 FROM sys.schemas WHERE name = 'sqltsk'

)
BEGIN
	EXEC('CREATE SCHEMA  sqltsk');
	PRINT 'Schema is created';
END
ELSE
BEGIN
	PRINT 'The schema is already created and ready to use';
END;
GO

-- checking if the table exist and creating it

IF OBJECT_ID('sqltsk.sony', 'U') IS NOT NULL

BEGIN
	DROP TABLE sqltsk.sony;
	PRINT 'Table dropped';
END
ELSE
BEGIN
	PRINT 'Creating the table....';
END;
GO

-- Creating the table

CREATE TABLE sqltsk.sony (

name NVARCHAR(50),
publisher NVARCHAR(50),
developer NVARCHAR(50),
total_sales	INT,
NA_sales INT,
japan_sales	INT,
release_date DATE,
last_update	DATE,
rating	FLOAT,
ratings_count INT,
metacritic INT,
genres NVARCHAR(50)

);
GO

PRINT 'Table is created...'

-- Creating procedure to add data to the created table

PRINT 'Running the stored procedure to load the data into the table';
GO

EXEC sqltsk.load_sony;
GO

CREATE OR ALTER PROCEDURE sqltsk.load_sony AS

BEGIN

	DECLARE @start_time DATETIME, @end_time DATETIME, @sony_start_time DATETIME, @sony_end_time DATETIME;

	
	BEGIN TRY

		-- Total execution time
		SET @sony_start_time = GETDATE();
		
		PRINT '===================================================';
		PRINT 'DAILY TASK SONY DATA LOAD';
		PRINT '===================================================';

		PRINT '---------------------------------------------------';
		PRINT 'SONY TABLE DATA LOAD';
		PRINT '---------------------------------------------------';

		SET @start_time = GETDATE();
		-- Truncate table schema

		PRINT '>>> Truncate table schema';

		TRUNCATE TABLE sqltsk.sony;

		-- Bulk insert into the table 

		PRINT '>>> Bulk insert into the table';

		BULK INSERT sqltsk.sony
		FROM 'C:\Users\8897p\OneDrive\Desktop\Special_problems_AI_ethics\ProjectFindIt\python\daily_tsk\build_fest\day_11_sql\sony_data1.csv'
		WITH (
			FIRSTROW = 2,
			FIELDTERMINATOR = ',',
			ROWTERMINATOR = '\n',
			TABLOCK -- OPTIMIZATION FOR SPEED, FOR MINIMAL LOGGING AND STOPPING OTHER OPERATIONS WHILE INSERT
		);

		SET @end_time = GETDATE();

		PRINT '>>> Data loaded in cust_info table in:' + CAST(DATEDIFF(second, @end_time, @start_time) AS NVARCHAR) + 'seconds';
		PRINT '---------------------------------------------------';

		PRINT '===================================================';
		PRINT 'TASK SONY DATA LOAD ENDS';
		PRINT '     - Total load duration: ' + CAST(DATEDIFF(second, @sony_start_time, @sony_end_time) AS NVARCHAR) + 'seconds';
		PRINT '===================================================';

		END TRY
	BEGIN CATCH
		PRINT '===================================================';
		PRINT'ERROR OCCURED WHILE LOADING DATA TABLE';
		PRINT 'Error Message' + ERROR_MESSAGE();
		PRINT 'Error Number' + CAST(ERROR_NUMBER() AS NVARCHAR);
		PRINT 'Error State' + CAST(ERROR_STATE() AS NVARCHAR);
		PRINT '===================================================';
	END CATCH


END;




