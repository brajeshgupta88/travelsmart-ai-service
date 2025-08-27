import asyncio
from typing import Dict, Any

async def fetch_activities(state: Dict[str, Any]) -> Dict[str, Any]:
    await asyncio.sleep(0.01)
    state.setdefault("activities", []).append({
        "price": 90.0,
        "start": "2025-11-06T02:00:00Z",
        "name": "Snorkeling Tour",
        "end": "2025-11-06T06:00:00Z",
        "location": "Nusa Penida",
        "id": "a1",
        "type": "activity"
    })
    return state
