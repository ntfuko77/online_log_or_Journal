-- https://dbdiagram.io/d/690a58d16735e111703da731

-- Tables
create table if not exists category(
category_id INT PRIMARY KEY AUTO_INCREMENT,
category_name CHAR(10) NOT NULL UNIQUE
);
create table if not exists author(
author_id INT primary KEY auto_increment,
author_name VARCHAR(50) NOT NULL
);
create table if not exists people(
people_id INT PRIMARY KEY AUTO_INCREMENT,
people_name VARCHAR(50) NOT NULL,
author_id INT,
foreign key (author_id) references author(author_id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE IF NOT EXISTS tag(
tag_name VARCHAR(50) UNIQUE,
tag_id INT PRIMARY KEY AUTO_INCREMENT,
valence INT CHECK (valence IN (0,1,-1)),
parent_tag_id INT,
category_id INT,
foreign key (parent_tag_id) references tag(tag_id) ON UPDATE CASCADE ON DELETE SET NULL,
foreign key (category_id) references category(category_id) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS entity(
entity_id INT PRIMARY KEY AUTO_INCREMENT,
content TEXT NOT NULL,
create_at timestamp default current_timestamp,
start_time timestamp default current_timestamp,
author_id INT,
related_people_id INT,
activity VARCHAR(20),
location VARCHAR(20),
foreign key (author_id) references author(author_id) ON DELETE CASCADE ON UPDATE CASCADE,
foreign key (related_people_id) references people(people_id) ON DELETE SET NULL ON UPDATE CASCADE
);

create table IF NOT EXISTS entity_tag_link(
linking_id INT PRIMARY KEY auto_increment,
entity_id INT NOT NULL,
tag_id INT NOT NULL,
is_primary BOOL NOT NULL,
duration INT,
focus VARCHAR(50),
specific_trigger TEXT,
updated_at timestamp default current_timestamp on update current_timestamp,
unique(tag_id,entity_id)
);