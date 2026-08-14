CREATE TABLE  IF NOT EXISTS contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '1', 'anonyme', 'noname', 'anonymous@email.fr', '+2653546434');
INSERT OR IGNORE INTO contacts (contact_id, first_name, last_name, email, phone)
VALUES( '2', 'anne onim', 'onim', 'anne.onim@email.com', '+86877779898');
create table if not exists user(
        id integer primary key autoincrement,
        email text,
            username text,
            phone text,
            password text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists city(
        id integer primary key autoincrement,
        name text,
            country_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists cafe_bar(
        id integer primary key autoincrement,
        name text,
            city_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists cafe_drinks(
        id integer primary key autoincrement,
        name text,
            user_id text,
            cafe_bar_id text,
            date text,
            time text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists musicgenre(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists celeb(
        id integer primary key autoincrement,
        name text,
            country_id text,
            musicgenre_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists sport(
        id integer primary key autoincrement,
        name text,
            season text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists sportpracticed(
        id integer primary key autoincrement,
        user_id text,
            sport_id text,
            city_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userwaypoints(
        id integer primary key autoincrement,
        sportpracticed_id text,
            user_id text,
            lat text,
            lon text,
            cafe_bar_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userhasholographiccompanion(
        id integer primary key autoincrement,
        celeb_id text,
            user_id text,
            waypoint_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists street(
        id integer primary key autoincrement,
        name text,
            city_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists flat(
        id integer primary key autoincrement,
        name_or_number text,
            street_id text,
            lat text,
            lon text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists flathasuser(
        id integer primary key autoincrement,
        user_id text,
            flat_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists flathasmusicgenre(
        id integer primary key autoincrement,
        flat_id text,
            musicgenre_id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists musicalinstrument(
        id integer primary key autoincrement,
        name text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists userplaysinstrument(
        id integer primary key autoincrement,
        musicallinstrument-id text,
            user-id text,
            flat-id text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
create table if not exists flathasshopsnearby(
        id integer primary key autoincrement,
        shopname text,
            lat text,
            lon text
      , created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP                );
