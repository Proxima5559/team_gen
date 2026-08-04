from pathlib import Path
import orjson
from app.models.team import Team


class JsonExporter:

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
            
        try:
            return orjson.dumps(payload, option=orjson.OPT_INDENT_2)
        except Exception:
            import json
            return json.dumps(payload, default=str, indent=2).encode("utf-8")

    def export(self, team: Team, output_path: str = "exports/team.json") -> str:
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(self.export_bytes(team))
        return str(path)