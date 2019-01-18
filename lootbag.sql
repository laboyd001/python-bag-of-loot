-- ********************************************
-- Building Tables
-- ********************************************

-- Sometimes needed when you want to delete rows from a table while preserving the table
DELETE FROM children;
DELETE FROM gifts;


-- Makes sure the CASCADE works
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS children;
DROP TABLE IF EXISTS gifts;

-- ***********************************************
-- create children table
-- ***********************************************

CREATE TABLE 'children' (
    'childid' integer NOT NULL PRIMARY KEY autoincrement,
    'name' TEXT NOT NULL,
    'receiving' BIT NOT NULL
);

-- ***********************************************
-- create gifts table
-- ***********************************************

CREATE TABLE 'gifts' (
    'giftid' integer NOT NULL PRIMARY KEY autoincrement,
    'name' TEXT NOT NULL,
    'delivered' BIT NOT NULL,
    'childid' integer not null,
    foreign key ('childid')
    references 'children' ('childid')
    ON DELETE CASCADE
);