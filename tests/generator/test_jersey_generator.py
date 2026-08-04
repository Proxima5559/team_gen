from app.generators.jersey_generator import JerseyGenerator
from app.services.random_service import RandomService
from app.models.team import Jersey
from app.data.colors import COLORS

def test_jersey_generator_returns_jersey():
    generator = JerseyGenerator(RandomService(seed=42))
    jersey = generator.generate(primary_color="Black", secondary_color="Gold")

    assert isinstance(jersey, Jersey)
    assert jersey.home_primary == "Black"
    assert jersey.home_secondary == "Gold"
    assert jersey.away_primary in COLORS
    assert jersey.away_secondary in COLORS
    assert jersey.third_primary in COLORS
    assert jersey.third_secondary in COLORS

def test_jersey_colors_do_not_repeat_home_colors():
    generator = JerseyGenerator(RandomService(seed=42))
    jersey = generator.generate(primary_color="Black", secondary_color="Gold")

    away_colors = {jersey.away_primary, jersey.away_secondary}
    third_colors = {jersey.third_primary, jersey.third_secondary}

    assert "Black" not in away_colors
    assert "Gold" not in away_colors
    assert "Black" not in third_colors
    assert "Gold" not in third_colors
    assert jersey.away_primary != jersey.away_secondary
    assert jersey.third_primary != jersey.third_secondary