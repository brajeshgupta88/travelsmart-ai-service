import asyncio
from typing import Dict, Any

async def fetch_flights(state: Dict[str, Any]) -> Dict[str, Any]:
    await asyncio.sleep(0.01)
    state.setdefault("flights", []).append({
        "price": 520.0,
        "meta": {"number": "GA123", "airline": "GA"},
        "start": f"{state['start_date']}T08:35:00Z",
        "end": f"{state['start_date']}T12:15:00Z",
        "from": state["source"],
        "id": "f1",
        "to": state["destination"],
        "type": "flight"
    })
    return state
