CREATE TABLE logs
(
	session_id timestamp not null,
	player_name text,
	date_session_start timestamp not null,
	tag text not null,
	data text,
	date_created timestamp not null,
  CONSTRAINT logs_pkey PRIMARY KEY (session_id, player_name, tag, date_created)
)
