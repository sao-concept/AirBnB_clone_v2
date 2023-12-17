-- Step 1: Create a test database for the Airbnb clone
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Step 2: Create a user and grant privileges for the test database
-- Note: Replace 'hbnb_test' and 'hbnb_test_pwd' with your desired username and password
GRANT ALL ON hbnb_test_db.*
TO 'hbnb_test'@'localhost'
IDENTIFIED BY 'hbnb_test_pwd';

-- Step 3: Grant SELECT privileges on the performance_schema for the test user
GRANT SELECT ON performance_schema.*
TO 'hbnb_test'@'localhost';

-- Note: Adjust the privileges and database/user details as needed for your specific requirements.
