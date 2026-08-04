import io
import zipfile
from pathlib import Path


from app.models.team import Team
from app.exporters.excel_exporter import ExcelExporter
from app.exporters.json_exporter import JsonExporter
from app.exporters.yaml_exporter import YamlExporter


class ZipExporter:

    def __init__(self):
        self.excel_exporter = ExcelExporter()
        self.yaml_exporter = YamlExporter()
        self.json_exporter = JsonExporter()

    def create_zip(self, team: Team) -> io.BytesIO:
        safe_name = team.name.lower().replace(" ", "_")

        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as z:
            root = f"{safe_name}"

            z.writestr(f"{root}/team_overview.json", self.json_exporter.export_bytes(team))
            z.writestr(f"{root}/team_overview.yaml", self.yaml_exporter.export_bytes(team))

            z.writestr(f"{root}/squad/players.json", self.json_exporter.export_bytes(team.players))
            z.writestr(f"{root}/squad/players.yaml", self.yaml_exporter.export_bytes(team.players))
            z.writestr(f"{root}/squad/squad_roster.xlsx", self.excel_exporter.export_bytes(team))

            z.writestr(f"{root}/club_identity/identity.json", self.json_exporter.export_bytes(team.identity))
            z.writestr(f"{root}/club_identity/history.json", self.json_exporter.export_bytes(team.history))
            z.writestr(f"{root}/club_identity/fan_culture.json", self.json_exporter.export_bytes(team.fans))

            z.writestr(f"{root}/management_and_venue/manager.json", self.json_exporter.export_bytes(team.manager))
            z.writestr(f"{root}/management_and_venue/stadium.json", self.json_exporter.export_bytes(team.stadium))

            if team.jerseys:
                z.writestr(f"{root}/assets/jerseys.json", self.json_exporter.export_bytes(team.jerseys))

        buffer.seek(0)
        return buffer

    def export(self, team: Team, output_path: str = "exports/team_package.zip") -> str:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        buffer = self.create_zip(team)
        path.write_bytes(buffer.getvalue())
        return str(path)