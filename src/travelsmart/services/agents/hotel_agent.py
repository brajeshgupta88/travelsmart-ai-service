import asyncio
from typing import Dict, Any

async def fetch_hotels(state: Dict[str, Any]) -> Dict[str, Any]:
    await asyncio.sleep(0.01)
    state.setdefault("hotels", []).append({
        "address": "Beach Road",
        "price": 780.0,
        "meta": {"nights": 7},
        "start": f"{state['start_date']}T14:00:00Z",
        "name": "Beachside Resort",
        "end": f"{state['end_date']}T11:00:00Z",
        "id": "h1",
        "type": "hotel"
    })
    return state
