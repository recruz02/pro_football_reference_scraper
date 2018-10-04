-- Drop table

-- DROP TABLE public.nflplayer_passing_stats

CREATE TABLE public.nflplayer_passing_stats (
	passing_stat_id serial NOT NULL,
	nflplayerid uuid NULL,
	player_year int4 NULL,
	age int4 NULL,
	team varchar(10) NULL,
	player_position varchar(10) NULL,
	player_number int4 NULL,
	games_played int4 NULL,
	games_started int4 NULL,
	qb_record varchar(20) NULL,
	completions int4 NULL,
	attempts int4 NULL,
	completion_percentage numeric(4,1) NULL,
	yards int4 NULL,
	touchdowns int4 NULL,
	touchdown_percentage numeric(4,1) NULL,
	interceptions int4 NULL,
	interception_percentage numeric(4,1) NULL,
	longest_completion int4 NULL,
	yards_per_attempt numeric(4,1) NULL,
	adjusted_yards_per_attempt numeric(4,1) NULL,
	yards_per_completion numeric(4,1) NULL,
	yards_per_game numeric(4,1) NULL,
	qb_rating numeric(4,1) NULL,
	qb_rating_espn numeric(4,1) NULL,
	sacked int4 NULL,
	sacked_yards int4 NULL,
	net_yards_per_pass numeric(4,2) NULL,
	adjusted_net_yards_per_pass numeric(4,2) NULL,
	sacked_percentage numeric(4,1) NULL,
	fourth_quarter_comebacks int4 NULL,
	game_winning_drives int4 NULL,
	approximate_value int4 NULL
)
WITH (
	OIDS=FALSE
) ;
