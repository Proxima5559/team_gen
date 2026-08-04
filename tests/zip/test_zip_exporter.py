import io
import json
import zipfile
import pytest
from pathlib import Path

from app.models.team import Team, ClubIdentity, History, FanCulture, Jersey
from app.models.manager import Manager
from app.models.stadium import Stadium
from app.models.player import Player
from app.data.formation import FormationType
from app.exporters.zip_exporter import ZipExporter


@pytest.fixture
def mock_team():
    return Team(
        name="FC Test",
        country="Testland",
        league="Test League",
        budget=50000000,
        formation=FormationType.FOUR_THREE_THREE if hasattr(FormationType, "FOUR_THREE_THREE") else "4-3-3",
        playing_style="Gegenpress",
        identity=ClubIdentity(
            founded=1900,
            nickname="The Testers",
            motto="Test Everything",
            primary_color="#FF0000",
            secondary_color="#0000FF",
            mascot="Testy the Dragon"
        ),
        history=History(
            founded=1900,
            milestones=["Won the Test Cup in 2020"]
        ),
        fans=FanCulture(
            supporter_name="Ultra Testers",
            atmosphere="Loud",
            average_attendance=45000,
            reputation="Friendly"
        ),
        manager=Manager(
            name="John Test",
            nationality="Testland",
            formation=FormationType.FOUR_THREE_THREE if hasattr(FormationType, "FOUR_THREE_THREE") else "4-3-3",
            style="Attacking"
        ),
        stadium=Stadium(
            name="Test Arena",
            city="Test City",
            capacity=50000
        ),
        players=[
            Player(
                name="Striker One",
                age=25,
                kit_number=9,
                nationality="Testland",
                position="ST",
                overall=85,
                potential=88,
                market_value=30000000,
                preferred_foot="Right",
                height_cm=185,
                weight_kg=78,
                pace=85, shooting=88, passing=70, dribbling=82, defending=35, physical=75,
                goalkeeping=20,
                aggression=70, stamina=80, strength=78, jumping=80, heading=75
            )
        ],
        jerseys=Jersey(
            home_primary="#FF0000", home_secondary="#FFFFFF",
            away_primary="#000000", away_secondary="#FF0000",
            third_primary="#YELLOW", third_secondary="#BLACK"
        )
    )

def test_zip_exporter_creates_file_and_valid_archive(tmp_path, mock_team):
    output_file = tmp_path / "exports" / "test_team.zip"
    exporter = ZipExporter()

    result_path = exporter.export(mock_team, output_path=str(output_file))

    assert Path(result_path).exists()
    assert output_file.exists()
    assert zipfile.is_zipfile(output_file)


def test_zip_exporter_folder_structure(tmp_path, mock_team):
    output_file = tmp_path / "test_team.zip"
    exporter = ZipExporter()
    exporter.export(mock_team, output_path=str(output_file))

    root = "fc_test"

    expected_files = {
        f"{root}/team_overview.json",
        f"{root}/team_overview.yaml",
        f"{root}/squad/players.json",
        f"{root}/squad/players.yaml",
        f"{root}/squad/squad_roster.xlsx",
        f"{root}/club_identity/identity.json",
        f"{root}/club_identity/history.json",
        f"{root}/club_identity/fan_culture.json",
        f"{root}/management_and_venue/manager.json",
        f"{root}/management_and_venue/stadium.json",
        f"{root}/assets/jerseys.json",
    }

    with zipfile.ZipFile(output_file, "r") as z:
        archive_files = set(z.namelist())
        assert expected_files.issubset(archive_files)


def test_zip_exporter_file_contents(tmp_path, mock_team):
    output_file = tmp_path / "test_team.zip"
    exporter = ZipExporter()
    exporter.export(mock_team, output_path=str(output_file))

    root = "fc_test"

    with zipfile.ZipFile(output_file, "r") as z:
        players_data_raw = z.read(f"{root}/squad/players.json")
        players_json = json.loads(players_data_raw)

        assert isinstance(players_json, list)
        assert len(players_json) == 1
        assert players_json[0]["name"] == "Striker One"
        assert players_json[0]["overall"] == 85

        stadium_data_raw = z.read(f"{root}/management_and_venue/stadium.json")
        stadium_json = json.loads(stadium_data_raw)

        assert stadium_json["name"] == "Test Arena"
        assert stadium_json["capacity"] == 50000