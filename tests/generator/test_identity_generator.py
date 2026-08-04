from app.generators.identity_generator import IdentityGenerator
from app.services.random_service import RandomService
from app.models.team import ClubIdentity
from app.data.colors import COLORS
from app.data.fans import NICKNAMES, MOTTOS, MASCOTS

def test_identity_generator_returns_identity():
    generator = IdentityGenerator(RandomService(seed=42))
    identity = generator.generate(country="England")

    assert isinstance(identity, ClubIdentity)
    assert 1870 <= identity.founded <= 2025
    assert identity.nickname in NICKNAMES
    assert identity.motto in MOTTOS
    assert identity.primary_color in COLORS
    assert identity.secondary_color in COLORS
    assert identity.primary_color != identity.secondary_color
    assert identity.mascot in MASCOTS