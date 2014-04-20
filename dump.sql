--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: chapter; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE chapter (
    id integer NOT NULL,
    video_id integer,
    title character varying(80),
    start_time integer,
    duration integer,
    "order" integer
);


ALTER TABLE public.chapter OWNER TO root;

--
-- Name: chapter_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE chapter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.chapter_id_seq OWNER TO root;

--
-- Name: chapter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE chapter_id_seq OWNED BY chapter.id;


--
-- Name: component; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE component (
    id integer NOT NULL,
    step_id integer,
    project_id integer,
    item_id integer,
    quantity integer,
    note character varying(255),
    required boolean
);


ALTER TABLE public.component OWNER TO root;

--
-- Name: component_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE component_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.component_id_seq OWNER TO root;

--
-- Name: component_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE component_id_seq OWNED BY component.id;


--
-- Name: item; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE item (
    id integer NOT NULL,
    name character varying(80),
    description character varying(255),
    note character varying(255)
);


ALTER TABLE public.item OWNER TO root;

--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO root;

--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE item_id_seq OWNED BY item.id;


--
-- Name: maker; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE maker (
    id integer NOT NULL,
    youtube_channel_url character varying(512),
    facebook_url character varying(512),
    twitter_handle character varying(40),
    email character varying(40),
    name character varying(80),
    alias character varying(80),
    description character varying(512),
    logo_url character varying(512),
    headshot_url character varying(512)
);


ALTER TABLE public.maker OWNER TO root;

--
-- Name: maker_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE maker_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.maker_id_seq OWNER TO root;

--
-- Name: maker_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE maker_id_seq OWNED BY maker.id;


--
-- Name: product; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE product (
    id integer NOT NULL,
    name character varying(80),
    description character varying(255),
    item_id integer,
    price double precision,
    shop_url character varying(512)
);


ALTER TABLE public.product OWNER TO root;

--
-- Name: product_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.product_id_seq OWNER TO root;

--
-- Name: product_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE product_id_seq OWNED BY product.id;


--
-- Name: project; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE project (
    id integer NOT NULL,
    title character varying(80),
    description character varying(512),
    maker_id integer,
    slug character varying(80)
);


ALTER TABLE public.project OWNER TO root;

--
-- Name: project_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE project_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.project_id_seq OWNER TO root;

--
-- Name: project_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE project_id_seq OWNED BY project.id;


--
-- Name: related_projects; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE related_projects (
    project_id integer,
    related_project_id integer
);


ALTER TABLE public.related_projects OWNER TO root;

--
-- Name: resource; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE resource (
    id integer NOT NULL,
    project_id integer,
    step_id integer,
    name character varying(80),
    path character varying(80)
);


ALTER TABLE public.resource OWNER TO root;

--
-- Name: resource_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE resource_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.resource_id_seq OWNER TO root;

--
-- Name: resource_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE resource_id_seq OWNED BY resource.id;


--
-- Name: step; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE step (
    id integer NOT NULL,
    title character varying(80),
    start_time integer,
    description character varying(255),
    "order" integer,
    project_id integer,
    chapter_id integer
);


ALTER TABLE public.step OWNER TO root;

--
-- Name: step_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE step_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.step_id_seq OWNER TO root;

--
-- Name: step_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE step_id_seq OWNED BY step.id;


--
-- Name: tag; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE tag (
    id integer NOT NULL,
    name character varying(80)
);


ALTER TABLE public.tag OWNER TO root;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE tag_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO root;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE tag_id_seq OWNED BY tag.id;


--
-- Name: tags; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE tags (
    tag_id integer,
    project_id integer
);


ALTER TABLE public.tags OWNER TO root;

--
-- Name: video; Type: TABLE; Schema: public; Owner: root; Tablespace: 
--

CREATE TABLE video (
    id integer NOT NULL,
    project_id integer,
    name character varying(80),
    host_guid character varying(80),
    path character varying(80)
);


ALTER TABLE public.video OWNER TO root;

--
-- Name: video_id_seq; Type: SEQUENCE; Schema: public; Owner: root
--

CREATE SEQUENCE video_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.video_id_seq OWNER TO root;

--
-- Name: video_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: root
--

ALTER SEQUENCE video_id_seq OWNED BY video.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY chapter ALTER COLUMN id SET DEFAULT nextval('chapter_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY component ALTER COLUMN id SET DEFAULT nextval('component_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY item ALTER COLUMN id SET DEFAULT nextval('item_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY maker ALTER COLUMN id SET DEFAULT nextval('maker_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY product ALTER COLUMN id SET DEFAULT nextval('product_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY project ALTER COLUMN id SET DEFAULT nextval('project_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY resource ALTER COLUMN id SET DEFAULT nextval('resource_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY step ALTER COLUMN id SET DEFAULT nextval('step_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY tag ALTER COLUMN id SET DEFAULT nextval('tag_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: root
--

ALTER TABLE ONLY video ALTER COLUMN id SET DEFAULT nextval('video_id_seq'::regclass);


--
-- Data for Name: chapter; Type: TABLE DATA; Schema: public; Owner: root
--

COPY chapter (id, video_id, title, start_time, duration, "order") FROM stdin;
\.


--
-- Name: chapter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('chapter_id_seq', 1, false);


--
-- Data for Name: component; Type: TABLE DATA; Schema: public; Owner: root
--

COPY component (id, step_id, project_id, item_id, quantity, note, required) FROM stdin;
\.


--
-- Name: component_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('component_id_seq', 1, false);


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: root
--

COPY item (id, name, description, note) FROM stdin;
\.


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('item_id_seq', 1, false);


--
-- Data for Name: maker; Type: TABLE DATA; Schema: public; Owner: root
--

COPY maker (id, youtube_channel_url, facebook_url, twitter_handle, email, name, alias, description, logo_url, headshot_url) FROM stdin;
\.


--
-- Name: maker_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('maker_id_seq', 1, false);


--
-- Data for Name: product; Type: TABLE DATA; Schema: public; Owner: root
--

COPY product (id, name, description, item_id, price, shop_url) FROM stdin;
\.


--
-- Name: product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('product_id_seq', 1, false);


--
-- Data for Name: project; Type: TABLE DATA; Schema: public; Owner: root
--

COPY project (id, title, description, maker_id, slug) FROM stdin;
1	$5 Makeshift Home Theater	Here's how to convert your Laptop, Smartphone, or Tablet into a makeshift projector. The picture isn't the greatest, but it's really really cheap, and can add a bit of creative fun to your next sports party!	\N	home-theater
2	Disposable Lighter Pyrotechnics	Whether you've got an itch for a mini-flamethrower, a shower of burning sparks, or a exploding ball of flames, these little fireworks-producing lighters may be the answer to your pyrotechnic cravings!	\N	disposable-lighter-pyrotechnics
3	DIY Electromagnetic Flashlight	Here's how to make a forever flashlight. I used mostly old parts I found laying around in broken electronics.	\N	electromagnetic-flahslight
4	DIY Emergency Fire Starter (Char Cloth)	I sacrificed my kids clothes and a can of tuna to make some high quality fire starter! Here's how to make a great batch of Char-Cloth to add to your emergency kit.	\N	emergency-fire-starter
5	Handheld Rocket Rifle	Here's how to take everyday sprinkler parts and convert them into a portable, hand-held rocket launcher! It's cheap to make, easy to use, and will send a paper rocket over 300 feet!	\N	handheld-rocket-rifle
6	Home-brew Bottle Rockets	In this project, we're making a simple, and safe, bottle rocket, out of common household materials.	\N	homebrew-bottle-rockets
7	Homemade Rocket Fuel	Today we're doing some kitchen chemistry using common household items. This is the type of cooking that gets me excited, because I'm experimenting with recipes for solid-state rocket fuel.	\N	roccket-fuel
8	Homemade Signal Flares	What do you get when you combine parts from an old battery pack with some common household ingredients? Mix them together and you get these .. A batch of super cheap, and easy to make, smoke flares.	\N	signal-flares
9	Homemade Spot Welder	Here is a step-by-step tutorial on how to make an 800 amp Spot Welder from common materials and for dirt cheap! Spot welders are used to fuse thin sheets of metal together and can cost hundreds of dollars to buy. In this video, we'll do it for practically nothing!	\N	spot-welder
10	Homemade Stick Welder	Did you know you can make an AC arc welder using parts from your microwave? I just finished mine, so join me in this video as we put its welding capabilities to the test!	\N	sitck-arc-welder
11	How to get 2000ºF Solar Power	Convert a junk TV into a 2000ºF solar cooker. Here's a technique for hacking a 4 foot mega magnifying lens out of your old TV, and some of the things you can do with it!	\N	junk-tv-solar-power
12	Lethal Electric Arcs	You can look, but don't touch! These arcs of plasma are lethal enough to kill on contact! In this project We're using an old Microwave Oven Transformer (MOT) to extract some traveling electric arcs.	\N	lethal-electric-arcs
13	Mousetrap Gun	Here's a way you can turn a mousetrap into a powerful handgun that shoots up to 40 feet! It launches projectiles with both power, and precision. Cheap, easy and affordable! Cost about $1.00	\N	mousetrap-gun
14	Ninja Tutrle Ooze	Hey, look at this! There's a broken canister of mutant ooze leaking down into the sewers! But don't worry because this sticky slime is non-toxic, and it's so easy to make, a 3 year old can do it!	\N	ninja-turtle-ooze
15	Paper Rockets That Fly 300 Feet	Here is how to make High Pressure Paper Rockets for your hand-held rocket launcher. They withstand over 135 PSI, shoot over 300 feet, are reusable, and only cost around 5¢ each!	\N	paper-rockets
16	PVC Pump	In this project you'll learn how to make a customizable PVC hand pump that will create vacuum suction, pump water, or compress air.	\N	pvc-pump
17	Rockin' Paper Plate Speaker	Here's how to make a real working paper plate speaker for under $1.00!	\N	paper-plate-speaker
18	Self Freezing Coca-Cola	Take any bottle of soda, and get it to freeze on command! This "super cool" trick works with cans of soda as well.	\N	self-freezing-soda
19	Solar Cooking Frame	Here's a way to frame your Solar Scorcher (Fresnel Lens) in under an hour, and for less than $8!! This design for a custom "Scorcher Frame" is easy to use, and incredibly cheap to make!	\N	solar-deathray
20	The 3 Penny Battery	Is there energy hidden inside your pocket change? Convert pennies into make-shift batteries that can drive small current devices like LED's and calculators.	\N	three-penny-battery
21	The Candy Cannon	Be the coolest person on the block by making it rain candy!! This is how to up-cycle sprinkler parts into a high power Candy Cannon that will launch candy 100 feet in the air!!! It's cheap to make, and a huge hit at birthday parties.	\N	candy-cannon
22	The Electric Deck of Cards	Here's how to make a deck of cards that will pump out a shocking 330 volts of electricity. Stuart Edge used it in his "Electric Shock Kissing Prank" to show the ladies how a man can really put the sparks in a kiss.	\N	electric-deck-of-cards
23	The Metal Melter	Here's a microwave oven transformer that's been modified into a dangerous little device. Now it can pump out 800 amps of electrical current, so let's use it to melt some metal!	\N	metal-metler
24	Water Balloon Shotgun	Bring out the big guns! Have you ever seen a water balloon shotgun? Here's how to make a High Powered Water Balloon Shooter that will fire 17 balloons at once!	\N	water-balloon-shotgun
\.


--
-- Name: project_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('project_id_seq', 24, true);


--
-- Data for Name: related_projects; Type: TABLE DATA; Schema: public; Owner: root
--

COPY related_projects (project_id, related_project_id) FROM stdin;
\.


--
-- Data for Name: resource; Type: TABLE DATA; Schema: public; Owner: root
--

COPY resource (id, project_id, step_id, name, path) FROM stdin;
\.


--
-- Name: resource_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('resource_id_seq', 1, false);


--
-- Data for Name: step; Type: TABLE DATA; Schema: public; Owner: root
--

COPY step (id, title, start_time, description, "order", project_id, chapter_id) FROM stdin;
\.


--
-- Name: step_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('step_id_seq', 1, false);


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: root
--

COPY tag (id, name) FROM stdin;
1	projectile
2	prank
3	electricity
4	melting
5	fire
6	electromagnetic
7	Arduino
8	explosive
9	solar
10	messy
11	PVC
12	sound
13	edible
14	soda
15	paper
16	liquid
17	computer
18	lighter
19	flashlight
20	LED
21	dangerous
22	indoor
23	outdoor
24	battery
25	coins
26	welder
27	emergency
28	scavenger
29	freezing
30	balloon
31	sparks
32	napkin
33	rocket
34	romantic
35	burning
36	circuit
37	chemistry
38	laptop
39	smartphone
40	tablet
41	lens
42	party
43	smoke
44	magnets
45	hacking
46	powertools
47	woodworking
48	lethal
49	tool
50	paint
51	hydraulic
52	party trick
53	playing cards
54	destruction
55	\N
56	\N
\.


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('tag_id_seq', 1, false);


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: root
--

COPY tags (tag_id, project_id) FROM stdin;
38	1
39	1
40	1
41	1
42	1
5	2
21	2
8	2
31	2
35	2
36	2
35	8
28	8
37	8
3	3
11	3
44	3
20	3
27	3
45	3
27	4
28	4
35	4
5	4
28	5
11	5
33	5
1	5
36	5
37	5
36	6
33	6
1	6
37	7
38	7
33	7
35	7
43	7
28	9
47	9
46	9
36	9
26	9
41	11
28	11
9	11
45	11
47	11
28	12
36	12
21	12
31	12
48	12
1	13
47	13
21	13
37	14
10	14
2	14
1	15
23	15
11	15
49	16
30	16
11	16
46	16
50	16
51	16
16	16
12	17
28	17
6	17
44	17
14	18
16	18
13	18
52	18
37	18
46	19
35	19
47	19
49	19
9	19
10	19
37	20
6	20
25	20
20	20
24	20
11	21
10	21
8	21
23	21
36	21
42	21
52	22
34	22
36	22
53	22
2	22
28	23
21	23
36	23
4	23
31	23
48	23
35	23
10	23
54	23
30	24
23	24
10	24
1	24
16	24
8	24
\.


--
-- Data for Name: video; Type: TABLE DATA; Schema: public; Owner: root
--

COPY video (id, project_id, name, host_guid, path) FROM stdin;
1	1	$5 Makeshift Home Theater	QP3BYh5yn20	https://www.youtube.com/watch?v=QP3BYh5yn20
2	2	Disposable Lighter Pyrotechnics	itMj9kShqvc	https://www.youtube.com/watch?v=itMj9kShqvc
3	3	DIY Electromagnetic Flashlight	tHg51GOzCXU	https://www.youtube.com/watch?v=tHg51GOzCXU
4	4	DIY Emergency Fire Starter (Char Cloth)	8Makaciz3Xc	https://www.youtube.com/watch?v=8Makaciz3Xc
5	5	Handheld Rocket Rifle	7Z-L4GliAts	https://www.youtube.com/watch?v=7Z-L4GliAts
6	6	Home-brew Bottle Rockets	6LrDLl_NpCs	https://www.youtube.com/watch?v=6LrDLl_NpCs
7	7	Homemade Rocket Fuel	yUYxk-y-tU8	https://www.youtube.com/watch?v=yUYxk-y-tU8
8	8	Homemade Signal Flares	gNrXrah6ohU	https://www.youtube.com/watch?v=gNrXrah6ohU
9	9	Homemade Spot Welder	vrlvqib94xQ	https://www.youtube.com/watch?v=vrlvqib94xQ
10	10	Homemade Stick Welder	nTDx3sN2dhU	https://www.youtube.com/watch?v=nTDx3sN2dhU
11	11	How to get 2000ºF Solar Power	XFw7U7V1Hok	https://www.youtube.com/watch?v=XFw7U7V1Hok
12	12	Lethal Electric Arcs	X8f-mxV9JXI	https://www.youtube.com/watch?v=X8f-mxV9JXI
13	13	Mousetrap Gun	RNcpJwu0I5I	https://www.youtube.com/watch?v=RNcpJwu0I5I
14	14	Ninja Tutrle Ooze	Ayx49u7kG64	https://www.youtube.com/watch?v=Ayx49u7kG64
15	15	Paper Rockets That Fly 300 Feet	uyZBH6n2XU8	https://www.youtube.com/watch?v=uyZBH6n2XU8
16	16	PVC Pump	vaho7JSVS1I	https://www.youtube.com/watch?v=vaho7JSVS1I
17	17	Rockin' Paper Plate Speaker	Awef78YtWmc	https://www.youtube.com/watch?v=Awef78YtWmc
18	18	Self Freezing Coca-Cola	5T68TvdoSbI	https://www.youtube.com/watch?v=5T68TvdoSbI
19	19	Solar Cooking Frame	Kj7aS7ToNWs	https://www.youtube.com/watch?v=Kj7aS7ToNWs
20	20	The 3 Penny Battery	rIdPfDHeROI	https://www.youtube.com/watch?v=rIdPfDHeROI
21	21	The Candy Cannon	VgZhQJQnnqA	https://www.youtube.com/watch?v=VgZhQJQnnqA
22	22	The Electric Deck of Cards	EivcZcgVjxI	https://www.youtube.com/watch?v=EivcZcgVjxI
23	23	The Metal Melter	GCrqLlz8Ee0	https://www.youtube.com/watch?v=GCrqLlz8Ee0
24	24	Water Balloon Shotgun	_NaQBvfEGMU	https://www.youtube.com/watch?v=_NaQBvfEGMU
\.


--
-- Name: video_id_seq; Type: SEQUENCE SET; Schema: public; Owner: root
--

SELECT pg_catalog.setval('video_id_seq', 24, true);


--
-- Name: chapter_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY chapter
    ADD CONSTRAINT chapter_pkey PRIMARY KEY (id);


--
-- Name: chapter_title_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY chapter
    ADD CONSTRAINT chapter_title_key UNIQUE (title);


--
-- Name: component_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY component
    ADD CONSTRAINT component_pkey PRIMARY KEY (id);


--
-- Name: item_name_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_name_key UNIQUE (name);


--
-- Name: item_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- Name: maker_alias_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY maker
    ADD CONSTRAINT maker_alias_key UNIQUE (alias);


--
-- Name: maker_name_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY maker
    ADD CONSTRAINT maker_name_key UNIQUE (name);


--
-- Name: maker_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY maker
    ADD CONSTRAINT maker_pkey PRIMARY KEY (id);


--
-- Name: product_name_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_name_key UNIQUE (name);


--
-- Name: product_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_pkey PRIMARY KEY (id);


--
-- Name: project_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY project
    ADD CONSTRAINT project_pkey PRIMARY KEY (id);


--
-- Name: project_slug_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY project
    ADD CONSTRAINT project_slug_key UNIQUE (slug);


--
-- Name: project_title_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY project
    ADD CONSTRAINT project_title_key UNIQUE (title);


--
-- Name: resource_path_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resource_path_key UNIQUE (path);


--
-- Name: resource_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resource_pkey PRIMARY KEY (id);


--
-- Name: step_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY step
    ADD CONSTRAINT step_pkey PRIMARY KEY (id);


--
-- Name: step_title_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY step
    ADD CONSTRAINT step_title_key UNIQUE (title);


--
-- Name: tag_name_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY tag
    ADD CONSTRAINT tag_name_key UNIQUE (name);


--
-- Name: tag_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (id);


--
-- Name: video_host_guid_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY video
    ADD CONSTRAINT video_host_guid_key UNIQUE (host_guid);


--
-- Name: video_name_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY video
    ADD CONSTRAINT video_name_key UNIQUE (name);


--
-- Name: video_path_key; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY video
    ADD CONSTRAINT video_path_key UNIQUE (path);


--
-- Name: video_pkey; Type: CONSTRAINT; Schema: public; Owner: root; Tablespace: 
--

ALTER TABLE ONLY video
    ADD CONSTRAINT video_pkey PRIMARY KEY (id);


--
-- Name: chapter_video_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY chapter
    ADD CONSTRAINT chapter_video_id_fkey FOREIGN KEY (video_id) REFERENCES video(id);


--
-- Name: component_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY component
    ADD CONSTRAINT component_item_id_fkey FOREIGN KEY (item_id) REFERENCES item(id);


--
-- Name: component_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY component
    ADD CONSTRAINT component_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: component_step_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY component
    ADD CONSTRAINT component_step_id_fkey FOREIGN KEY (step_id) REFERENCES step(id);


--
-- Name: product_item_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY product
    ADD CONSTRAINT product_item_id_fkey FOREIGN KEY (item_id) REFERENCES item(id);


--
-- Name: project_maker_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY project
    ADD CONSTRAINT project_maker_id_fkey FOREIGN KEY (maker_id) REFERENCES maker(id);


--
-- Name: related_projects_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY related_projects
    ADD CONSTRAINT related_projects_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: related_projects_related_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY related_projects
    ADD CONSTRAINT related_projects_related_project_id_fkey FOREIGN KEY (related_project_id) REFERENCES project(id);


--
-- Name: resource_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resource_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: resource_step_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY resource
    ADD CONSTRAINT resource_step_id_fkey FOREIGN KEY (step_id) REFERENCES step(id);


--
-- Name: step_chapter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY step
    ADD CONSTRAINT step_chapter_id_fkey FOREIGN KEY (chapter_id) REFERENCES chapter(id);


--
-- Name: step_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY step
    ADD CONSTRAINT step_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: tags_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY tags
    ADD CONSTRAINT tags_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: tags_tag_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY tags
    ADD CONSTRAINT tags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES tag(id);


--
-- Name: video_project_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: root
--

ALTER TABLE ONLY video
    ADD CONSTRAINT video_project_id_fkey FOREIGN KEY (project_id) REFERENCES project(id);


--
-- Name: public; Type: ACL; Schema: -; Owner: dodeca
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM dodeca;
GRANT ALL ON SCHEMA public TO dodeca;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

