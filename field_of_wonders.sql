-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://github.com/pgadmin-org/pgadmin4/issues/new/choose if you find any bugs, including reproduction steps.
BEGIN;


ALTER TABLE IF EXISTS public.discounts DROP CONSTRAINT IF EXISTS discounts_categorie_id_fkey;

ALTER TABLE IF EXISTS public.games DROP CONSTRAINT IF EXISTS games_user_id_fkey;

ALTER TABLE IF EXISTS public.games DROP CONSTRAINT IF EXISTS games_word_id_fkey;

ALTER TABLE IF EXISTS public.games_rounds DROP CONSTRAINT IF EXISTS games_rounds_game_id_fkey;

ALTER TABLE IF EXISTS public.games_rounds DROP CONSTRAINT IF EXISTS games_rounds_round_id_fkey;

ALTER TABLE IF EXISTS public.letters_round DROP CONSTRAINT IF EXISTS letters_round_letter_fkey;

ALTER TABLE IF EXISTS public.letters_round DROP CONSTRAINT IF EXISTS letters_round_round_id_fkey;

ALTER TABLE IF EXISTS public.prises DROP CONSTRAINT IF EXISTS prises_categorie_id_fkey;

ALTER TABLE IF EXISTS public.users_discounts DROP CONSTRAINT IF EXISTS users_discounts_discount_id_fkey;

ALTER TABLE IF EXISTS public.users_discounts DROP CONSTRAINT IF EXISTS users_discounts_user_id_fkey;

ALTER TABLE IF EXISTS public.users_prises DROP CONSTRAINT IF EXISTS users_prises_prise_id_fkey;

ALTER TABLE IF EXISTS public.users_prises DROP CONSTRAINT IF EXISTS users_prises_user_id_fkey;



DROP TABLE IF EXISTS public.categories;

CREATE TABLE IF NOT EXISTS public.categories
(
    categorie_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    categorie_name character(30) COLLATE pg_catalog."default" NOT NULL,
    is_instore boolean NOT NULL DEFAULT true,
    CONSTRAINT categories_pkey PRIMARY KEY (categorie_id)
);

DROP TABLE IF EXISTS public.discounts;

CREATE TABLE IF NOT EXISTS public.discounts
(
    discount_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    discount_description character(50) COLLATE pg_catalog."default" NOT NULL,
    discount_calue smallint NOT NULL,
    "prise _in_scores" smallint NOT NULL,
    categorie_id integer NOT NULL,
    to_show boolean NOT NULL DEFAULT true,
    CONSTRAINT discounts_pkey PRIMARY KEY (discount_id)
);

DROP TABLE IF EXISTS public.games;

CREATE TABLE IF NOT EXISTS public.games
(
    game_id integer NOT NULL,
    word_id integer NOT NULL,
    user_id integer NOT NULL,
    CONSTRAINT games_pkey PRIMARY KEY (game_id)
);

DROP TABLE IF EXISTS public.games_rounds;

CREATE TABLE IF NOT EXISTS public.games_rounds
(
    game_id integer NOT NULL,
    round_id integer NOT NULL
);

DROP TABLE IF EXISTS public.letters;

CREATE TABLE IF NOT EXISTS public.letters
(
    letter "char" NOT NULL,
    is_called boolean NOT NULL DEFAULT false,
    CONSTRAINT letters_pkey PRIMARY KEY (letter)
);

DROP TABLE IF EXISTS public.letters_round;

CREATE TABLE IF NOT EXISTS public.letters_round
(
    letter "char" NOT NULL,
    round_id integer NOT NULL
);

DROP TABLE IF EXISTS public.prises;

CREATE TABLE IF NOT EXISTS public.prises
(
    prise_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    prise_description character(50) COLLATE pg_catalog."default" NOT NULL,
    categorie_id integer NOT NULL,
    CONSTRAINT prises_pkey PRIMARY KEY (prise_id)
);

DROP TABLE IF EXISTS public.rounds;

CREATE TABLE IF NOT EXISTS public.rounds
(
    round_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    round_score_id smallint NOT NULL,
    is_word_guessed boolean NOT NULL DEFAULT false,
    prise_id integer,
    is_prise_accepted boolean NOT NULL DEFAULT false,
    CONSTRAINT rounds_pkey PRIMARY KEY (round_id)
);

DROP TABLE IF EXISTS public.scores;

CREATE TABLE IF NOT EXISTS public.scores
(
    score_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    score smallint NOT NULL,
    CONSTRAINT scores_pkey PRIMARY KEY (score_id)
);

DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    user_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    user_name character(30) COLLATE pg_catalog."default" NOT NULL,
    users_score_to_spend integer,
    CONSTRAINT users_pkey PRIMARY KEY (user_id)
);

DROP TABLE IF EXISTS public.users_discounts;

CREATE TABLE IF NOT EXISTS public.users_discounts
(
    user_id integer NOT NULL,
    discount_id integer NOT NULL
);

DROP TABLE IF EXISTS public.users_prises;

CREATE TABLE IF NOT EXISTS public.users_prises
(
    user_id integer NOT NULL,
    prise_id integer NOT NULL,
    CONSTRAINT users_prises_pkey PRIMARY KEY (user_id)
        INCLUDE(user_id)
);

DROP TABLE IF EXISTS public.words;

CREATE TABLE IF NOT EXISTS public.words
(
    word_id integer NOT NULL,
    word character(30) COLLATE pg_catalog."default" NOT NULL,
    description character(100) COLLATE pg_catalog."default" NOT NULL,
    difficulty smallint NOT NULL DEFAULT 100,
    CONSTRAINT words_pkey PRIMARY KEY (word_id),
    CONSTRAINT words_word_key UNIQUE (word)
);

ALTER TABLE IF EXISTS public.discounts
    ADD CONSTRAINT discounts_categorie_id_fkey FOREIGN KEY (categorie_id)
    REFERENCES public.categories (categorie_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;


ALTER TABLE IF EXISTS public.games
    ADD CONSTRAINT games_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.games
    ADD CONSTRAINT games_word_id_fkey FOREIGN KEY (word_id)
    REFERENCES public.words (word_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.games_rounds
    ADD CONSTRAINT games_rounds_game_id_fkey FOREIGN KEY (game_id)
    REFERENCES public.games (game_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.games_rounds
    ADD CONSTRAINT games_rounds_round_id_fkey FOREIGN KEY (round_id)
    REFERENCES public.rounds (round_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.letters_round
    ADD CONSTRAINT letters_round_letter_fkey FOREIGN KEY (letter)
    REFERENCES public.letters (letter) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.letters_round
    ADD CONSTRAINT letters_round_round_id_fkey FOREIGN KEY (round_id)
    REFERENCES public.rounds (round_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.prises
    ADD CONSTRAINT prises_categorie_id_fkey FOREIGN KEY (categorie_id)
    REFERENCES public.categories (categorie_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.users_discounts
    ADD CONSTRAINT users_discounts_discount_id_fkey FOREIGN KEY (discount_id)
    REFERENCES public.discounts (discount_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.users_discounts
    ADD CONSTRAINT users_discounts_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.users_prises
    ADD CONSTRAINT users_prises_prise_id_fkey FOREIGN KEY (prise_id)
    REFERENCES public.prises (prise_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.users_prises
    ADD CONSTRAINT users_prises_user_id_fkey FOREIGN KEY (user_id)
    REFERENCES public.users (user_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;
CREATE INDEX IF NOT EXISTS users_prises_pkey
    ON public.users_prises(user_id);

END;