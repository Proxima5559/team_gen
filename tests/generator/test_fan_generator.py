from app.generators.fan_generator import FanGenerator
from app.services.random_service import RandomService
from app.models.team import FanCulture

def test_fan_generator_returns_fan_culture():
    generator = FanGenerator(RandomService(seed=42))
    fans = generator.generate(club_name="FC Test", stadium_capacity=40000)

    assert isinstance(fans, FanCulture)
    assert fans.supporter_name
    assert fans.atmosphere
    assert fans.reputation
    assert fans.average_attendance >= 20000
    assert fans.average_attendance <= 40000

def test_fan_attendance_is_within_expected_range():
    capacity = 50000
    generator = FanGenerator(RandomService(seed=42))
    fans = generator.generate(club_name="FC Test", stadium_capacity=capacity)

    assert int(capacity * 0.50) <= fans.average_attendance <= capacity