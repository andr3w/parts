CREATE DATABASE parts;
CREATE user parts;
USE parts;
GRANT ALL ON parts.* to parts;
CREATE TABLE parts(
    code VARCHAR(20) PRIMARY KEY,
    description VARCHAR(100)
);
INSERT INTO parts VALUES('PU002210', 'Label "Do not stand" 50mmx50mm');
INSERT INTO parts VALUES('AS000110', 'GTL Bearing Strip Wide');
