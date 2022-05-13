-- Prepares Mysql server for the proyect
-- Create: Database, user with privileges
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
SET GLOBAL validate_password_policy = LOW;
CREATE USER IF NOT EXISTS 'hbnb_test' @'localhost' IDENTIFIED BY 'hbnb_test_pwd';
USE hbnb_test_db;
GRANT ALL PRIVILEGES ON hbnb_test_db TO 'hbnb_test' @'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_test' @'localhost';
FLUSH PRIVILEGES;