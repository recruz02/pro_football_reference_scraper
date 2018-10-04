-- Drop table

-- DROP TABLE public.nflplayer

CREATE TABLE public.nflplayer (
	nflplayerid uuid NULL DEFAULT uuid_generate_v4(),
	first_name varchar(100) NULL,
	last_name varchar(100) NULL,
	player_position varchar(10) NULL,
	player_height varchar(10) NULL,
	player_weight varchar(10) NULL,
	birthdate date NULL,
	birthplace varchar(100) NULL,
	college varchar(200) NULL,
	"timestamp" varchar(100) NULL DEFAULT now(),
	pro_football_reference_url varchar(2000) NULL
)
WITH (
	OIDS=FALSE
) ;
