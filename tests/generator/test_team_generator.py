from app.generators.team_generator import TeamGenerator
from app.generators.manager_generator import ManagerGenerator
from app.generators.player_generator import PlayerGenerator
from app.generators.stadium_generator import StadiumGenerator
from app.generators.history_generator import HistoryGenerator
from app.generators.identity_generator import IdentityGenerator
from app.generators.fan_generator import FanGenerator
from app.generators.jersey_generator import JerseyGenerator
from app.services.formation_service import FormationService
from app.services.nationality_service import NationalityService
from app.services.random_service import RandomService
from app.data.countries import COUNTRY_TO_NATIONALITY
from app.api.schemas import TeamRequest
from app.models.team import Team

def build_team_generator(seed=42):
    random_service = RandomService(seed=seed)
    nationality_service = NationalityService(COUNTRY_TO_NATIONALITY)

    return TeamGenerator(
        random_service=random_service,
        formation_service=FormationService(),
        manager_generator=ManagerGenerator(random_service, nationality_service),
        player_generator=PlayerGenerator(random_service, nationality_service),
        stadium_generator=StadiumGenerator(random_service),
        history_generator=HistoryGenerator(random_service),
        identity_generator=IdentityGenerator(random_service),
        fan_generator=FanGenerator(random_service),
        jersey_generator=JerseyGenerator(random_service),
    )

def test_team_generator_returns_complete_team():
    generator = build_team_generator()
    request = TeamRequest(
        club_name="FC Test",
        country="England",
        league="Premier League",
        budget=50000000,
        formation="4-3-3",
        playing_style="Possession",
    )

    team = generator.generate(request)

    assert isinstance(team, Team)
    assert team.name == "FC Test"
    assert team.country == "England"
    assert team.league == "Premier League"
    assert team.budget == 50000000
    assert team.formation == "4-3-3"
    assert team.playing_style == "Possession"

    assert team.manager is not None
    assert team.stadium is not None
    assert team.identity is not None
    assert team.history is not None
    assert team.fans is not None
    assert team.jerseys is not None

    assert 1870 <= team.identity.founded <= 2025
    assert team.identity.nickname
    assert team.identity.motto
    assert team.identity.mascot
    assert team.identity.primary_color
    assert team.identity.secondary_color
    assert team.identity.primary_color != team.identity.secondary_color

    assert len(team.history.milestones) >= 1
    assert team.rival is None if hasattr(team, "rival") else True

    assert team.fans.average_attendance >= 0
    assert team.fans.supporter_name
    assert team.fans.atmosphere
    assert team.fans.reputation

    assert len(team.players) == 11
    for player in team.players:
        assert player.position
        assert player.name