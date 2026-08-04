from app.generators.stadium_generator import StadiumGenerator
from app.services.random_service import RandomService
from app.models.stadium import Stadium

def test_stadium_generator_returns_stadium():
    generator = StadiumGenerator(random_service=RandomService(seed=42))
    stadium = generator.generate(country="England")

    assert isinstance(stadium, Stadium)
    assert stadium.name
    assert stadium.city
    assert 8000 <= stadium.capacity <= 85000