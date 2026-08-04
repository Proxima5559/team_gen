from pathlib import Path
import yaml
from app.models.team import Team


class YamlExporter:

    def export_bytes(self, data_obj) -> bytes:
        if isinstance(data_obj, list):
            payload = [
                item.model_dump(mode="json") if hasattr(item, "model_dump") else item 
                for item in data_obj
            ]
        elif hasattr(data_obj, "model_dump"):
            payload = data_obj.model_dump(mode="json")
        else:
            payload = data_obj

        yaml_str = yaml.dump(payload, sort_keys=False, allow_unicode=True)
        return yaml_str.encode("utf-8")

    def export(self, team: Team, output_path: str = "exports/team.yaml") -> str:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(self.export_bytes(team))
        return str(path)