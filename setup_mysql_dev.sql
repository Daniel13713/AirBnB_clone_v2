-- Prepares Mysql server for the proyect
-- Create: Database, user with privileges
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS performance_schema;
SET GLOBAL validate_password_policy = LOW;
CREATE USER IF NOT EXISTS 'hbnb_dev' @'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev' @'localhost';
USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev' @'localhost';
FLUSH PRIVILEGES;