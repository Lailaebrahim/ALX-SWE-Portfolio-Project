-- Create the new user
CREATE USER 'TestPersonalBlog'@'localhost' IDENTIFIED BY 'TestPersonalBlogPwd';

-- Create the new database
CREATE DATABASE TestPersonalBlogDB;

-- Grant all privileges on the new database to the new user
GRANT ALL PRIVILEGES ON TestPersonalBlogDB.* TO 'TestPersonalBlog'@'localhost';

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;