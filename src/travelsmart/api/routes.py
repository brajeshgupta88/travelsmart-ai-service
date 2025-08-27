from fastapi import APIRouter, HTTPException
from travelsmart.schemas.travel import TravelRequest, TravelResponse
from travelsmart.services.orchestrator import run_workflow

router = APIRouter()

@router.post("/plan_trip", response_model=TravelResponse)
async def plan_trip(req: TravelRequest):
    req_dict = req.dict()
    req_dict["currency"] = req.currency
    try:
        result = await run_workflow(req_dict)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
