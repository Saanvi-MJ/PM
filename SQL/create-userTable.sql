CREATE TABLE IF NOT EXISTS userTable (
    first_name VARCHAR(255) NOT NULL,
    master_user_name VARCHAR(255) PRIMARY KEY,
    hashed_password VARCHAR(255) NOT NULL UNIQUE,
    unique_key VARCHAR(255) NOT NULL UNIQUE
);