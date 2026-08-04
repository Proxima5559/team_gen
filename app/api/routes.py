import json

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.api.schemas import TeamRequest
from app.dependencies.dependencies import get_team_generator
from app.exporters.zip_exporter import ZipExporter
from app.generators.team_generator import TeamGenerator
from app.models.team import Team

router = APIRouter(prefix="/teams", tags=["Teams"])

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@router.get("/generate", response_class=HTMLResponse)
def generate_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="pages/footbal_gen/generate.html",
        context={"request": request}
    )


@router.post("/generate", response_class=HTMLResponse)
def generate_team(
    request: Request,
    team_request: TeamRequest | None = None,
    generator: TeamGenerator = Depends(get_team_generator),
):
    try:
        payload = team_request or TeamRequest()
        
        if payload.seed is not None:
            generator.random.seed(payload.seed)
        
        team = generator.generate(payload)
        
        return templates.TemplateResponse(
            request=request,
            name="pages/footbal_gen/partials/team_result.html",
            context={"request": request, "team": team}
        )
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/update", response_model=Team)
def update_team(team: Team):
    try:
        return team
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid update payload")


@router.post("/export")
async def export_team(request: Request):
    try:
        body_bytes = await request.body()
        
        if isinstance(body_bytes, bytes):
            body_data = json.loads(body_bytes.decode("utf-8"))
        else:
            body_data = body_bytes

        if isinstance(body_data, str):
            body_data = json.loads(body_data)

        team = Team(**body_data)
        
        exporter = ZipExporter()
        zip_buffer = exporter.create_zip(team)
        zip_buffer.seek(0)
        
        safe_name = team.name.replace(" ", "_")
        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={"Content-Disposition": f'attachment; filename="{safe_name}.zip"'}
        )
        
    except Exception as e:
        print(f"--- UNEXPECTED ERROR: {e} ---")
        raise HTTPException(status_code=500, detail=str(e))