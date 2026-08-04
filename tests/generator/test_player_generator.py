from app.generators.player_generator import PlayerGenerator
from app.services.random_service import RandomService
from app.services.nationality_service import NationalityService
from app.data.countries import COUNTRY_TO_NATIONALITY
from app.models.player import Player


def build_generator():
    return PlayerGenerator(
        random_service=RandomService(seed=42),
        nationality_service=NationalityService(COUNTRY_TO_NATIONALITY),
    )


def test_player_generator_basic_generation():
    generator = build_generator()
    player = generator.generate(country="England", position="ST")

    assert isinstance(player, Player)
    assert player.name
    assert player.position == "ST"
    assert player.nationality == "English"


def test_player_age_in_range():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert 17 <= player.age <= 35


def test_player_overall_in_range():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert 60 <= player.overall <= 94


def test_player_potential_in_range():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert player.overall <= player.potential <= 99


def test_player_market_value_in_range():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert 100000 <= player.market_value <= 180000000


def test_player_preferred_foot_valid():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert player.preferred_foot in ["Left", "Right", "Both"]


def test_player_height_is_present_and_reasonable():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert 150 <= player.height_cm <= 220


def test_player_weight_is_present_and_reasonable():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")
    assert 45 <= player.weight_kg <= 130


def test_player_attributes_are_in_range():
    generator = build_generator()
    player = generator.generate(country="England", position="CM")

    assert 20 <= player.pace <= 99
    assert 20 <= player.shooting <= 99
    assert 20 <= player.passing <= 99
    assert 20 <= player.defending <= 99
    assert 20 <= player.physical <= 99
    assert 20 <= player.dribbling <= 99
    assert 20 <= player.goalkeeping <= 99
    assert 20 <= player.aggression <= 99
    assert 20 <= player.stamina <= 99
    assert 20 <= player.strength <= 99
    assert 20 <= player.jumping <= 99
    assert 20 <= player.heading <= 99