from mimesis.locales import Locale


WORLD_DATA = {
    "England": {
        "locale": Locale.EN,
        "nationality": "English",
        "chance": 40,
        "capacity_range": (15000, 90000),
        "leagues": {
            "Premier League": {
                "tier": "tier_1",
                "budget": (50_000_000, 650_000_000),
                "overall": (70, 94),
                "capacity": (25_000, 75_000),
            },
            "Championship": {
                "tier": "tier_2",
                "budget": (10_000_000, 80_000_000),
                "overall": (64, 78),
                "capacity": (15_000, 40_000),
            },
        },
    },
    "Spain": {
        "locale": Locale.ES,
        "nationality": "Spanish",
        "chance": 40,
        "capacity_range": (10000, 99000),
        "leagues": {
            "La Liga": {
                "tier": "tier_1",
                "budget": (30_000_000, 500_000_000),
                "overall": (68, 93),
                "capacity": (15_000, 80_000),
            },
            "Segunda División": {
                "tier": "tier_2",
                "budget": (5_000_000, 40_000_000),
                "overall": (63, 76),
                "capacity": (8_000, 30_000),
            },
        },
    },
    "Germany": {
        "locale": Locale.DE,
        "nationality": "German",
        "chance": 30,
        "capacity_range": (15000, 81000),
        "leagues": {
            "Bundesliga": {
                "tier": "tier_1",
                "budget": (25_000_000, 450_000_000),
                "overall": (68, 92),
                "capacity": (20_000, 80_000),
            },
            "2. Bundesliga": {
                "tier": "tier_2",
                "budget": (5_000_000, 40_000_000),
                "overall": (63, 76),
                "capacity": (10_000, 50_000),
            },
        },
    },
    "France": {
        "locale": Locale.FR,
        "nationality": "French",
        "chance": 28,
        "capacity_range": (10000, 80000),
        "leagues": {
            "Ligue 1": {
                "tier": "tier_1",
                "budget": (20_000_000, 500_000_000),
                "overall": (67, 92),
                "capacity": (15_000, 65_000),
            },
            "Ligue 2": {
                "tier": "tier_2",
                "budget": (4_000_000, 30_000_000),
                "overall": (62, 75),
                "capacity": (5_000, 25_000),
            },
        },
    },
    "Italy": {
        "locale": Locale.IT,
        "nationality": "Italian",
        "chance": 25,
        "capacity_range": (10000, 80000),
        "leagues": {
            "Serie A": {
                "tier": "tier_1",
                "budget": (25_000_000, 400_000_000),
                "overall": (68, 92),
                "capacity": (15_000, 75_000),
            },
            "Serie B": {
                "tier": "tier_2",
                "budget": (4_000_000, 35_000_000),
                "overall": (62, 75),
                "capacity": (6_000, 30_000),
            },
        },
    },
    "Brazil": {
        "locale": Locale.PT_BR,
        "nationality": "Brazilian",
        "chance": 20,
        "capacity_range": (15000, 78000),
        "leagues": {
            "Série A": {
                "tier": "tier_1",
                "budget": (10_000_000, 70_000_000),
                "overall": (65, 80),
                "capacity": (15_000, 60_000),
            },
            "Série B": {
                "tier": "tier_2",
                "budget": (3_000_000, 25_000_000),
                "overall": (61, 74),
                "capacity": (5_000, 25_000),
            },
        },
    },
    "Russia": {
        "locale": Locale.RU,
        "nationality": "Russian",
        "chance": 15,
        "capacity_range": (10000, 61000),
        "leagues": {
            "Premier League": {
                "tier": "tier_1",
                "budget": (5_000_000, 50_000_000),
                "overall": (63, 76),
                "capacity": (8_000, 35_000),
            },
            "First League": {
                "tier": "tier_2",
                "budget": (5_000_000, 50_000_000),
                "overall": (63, 76),
                "capacity": (8_000, 35_000),
            },
        },
    },

    "Portugal": {
        "locale": Locale.PT,
        "nationality": "Portuguese",
        "chance": 24,
        "capacity_range": (8000, 65000),
        "leagues": {
            "Primeira Liga": {
                "tier": "tier_1",
                "budget": (10_000_000, 150_000_000),
                "overall": (66, 88),
                "capacity": (10_000, 65_000),
            },
            "Liga Portugal 2": {
                "tier": "tier_2",
                "budget": (2_000_000, 15_000_000),
                "overall": (60, 73),
                "capacity": (5_000, 20_000),
            },
        },
    },
    "Argentina": {
        "locale": Locale.ES,  
        "nationality": "Argentine",
        "chance": 20,
        "capacity_range": (10000, 80000),
        "leagues": {
            "Liga Profesional": {
                "tier": "tier_1",
                "budget": (8_000_000, 100_000_000),
                "overall": (65, 85),
                "capacity": (15_000, 80_000),
            },
            "Primera Nacional": {
                "tier": "tier_2",
                "budget": (2_000_000, 15_000_000),
                "overall": (60, 74),
                "capacity": (8_000, 30_000),
            },
        },
    },
    "Netherlands": {
        "locale": Locale.NL,
        "nationality": "Dutch",
        "chance": 15,
        "capacity_range": (8000, 55000),
        "leagues": {
            "Eredivisie": {
                "tier": "tier_1",
                "budget": (12_000_000, 150_000_000),
                "overall": (67, 88),
                "capacity": (10_000, 55_000),
            },
            "Eerste Divisie": {
                "tier": "tier_2",
                "budget": (2_000_000, 15_000_000),
                "overall": (60, 73),
                "capacity": (5_000, 20_000),
            },
        },
    },
}



COUNTRY_TO_LOCALE = {country: data["locale"] for country, data in WORLD_DATA.items()}

COUNTRY_TO_NATIONALITY = {country: data["nationality"] for country, data in WORLD_DATA.items()}

COUNTRY_TO_CAPACITY = {country: data["capacity_range"] for country, data in WORLD_DATA.items()}

COUNTRY_TO_LEAGUES = {country: list(data["leagues"].keys()) for country, data in WORLD_DATA.items()}

COUNTRY_TO_CHANCE = {
    country: data["chance"]
    for country, data in WORLD_DATA.items()
}

LEAGUE_TIERS = {
    league_name: {
        "budget": league_data["budget"],
        "overall": league_data["overall"],
        "capacity": league_data["capacity"],
    }
    for country_data in WORLD_DATA.values()
    for league_name, league_data in country_data["leagues"].items()
}

DEFAULT_TIER = {
    "budget": (5_000_000, 50_000_000), 
    "overall": (60, 80),
    "capacity": (8_000, 40_000)
}

LEAGUE_NATIONALITY_MODIFIERS = {
    "England": {
        "Premier League": {
            "English": 2.2,
        },
        "Championship": {
            "English": 4.3,
        },
    },

    "Spain": {
        "La Liga": {
            "Spanish": 2.2,
        },
        "Segunda División": {
            "Spanish": 3.3,
        },
    },

    "Germany": {
        "Bundesliga": {
            "German": 2.2,
        },
        "2. Bundesliga": {
            "German": 3.3,
        },
    },

    "France": {
        "Ligue 1": {
            "French": 2.2,
        },
        "Ligue 2": {
            "French": 3.3,
        },
    },

    "Italy": {
        "Serie A": {
            "Italian": 2.2,
        },
        "Serie B": {
            "Italian": 3.3,
        },
    },

    "Brazil": {
        "Série A": {
            "Brazilian": 2.3,
        },
        "Série B": {
            "Brazilian": 3.4,
        },
    },

    "Russia": {
        "Premier League": {
            "Russian": 2.0,
        },
        "First League": {
            "Russian": 3.3,
        },
    },

    "Portugal": {
        "Primeira Liga": {
            "Portuguese": 2.4,
        },
        "Liga Portugal 2": {
            "Portuguese": 3.6,
        },
    },

    "Argentina": {
        "Liga Profesional": {
            "Argentine": 2.3,
        },
        "Primera Nacional": {
            "Argentine": 3.5,
        },
    },

    "Netherlands": {
        "Eredivisie": {
            "Dutch": 2.3,
        },
        "Eerste Divisie": {
            "Dutch": 3.5,
        },
    },
}