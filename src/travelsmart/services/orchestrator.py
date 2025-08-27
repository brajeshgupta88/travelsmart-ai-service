import asyncio
from typing import Dict, Any
from travelsmart.services.agents.flight_agent import fetch_flights
from travelsmart.services.agents.hotel_agent import fetch_hotels
from travelsmart.services.agents.activity_agent import fetch_activities

async def prepare_itinerary(state: Dict[str, Any]) -> Dict[str, Any]:
    items = []
    total_price = 0.0
    for f in state.get("flights", []):
        items.append(f); total_price += f["price"]
    for h in state.get("hotels", []):
        items.append(h); total_price += h["price"]
    for a in state.get("activities", []):
        items.append(a); total_price += a["price"]

    response = {
        "itinerary": {
            "alternatives": {},
            "currency": state.get("currency", "USD"),
            "totals": {"price": total_price},
            "items": items
        },
        "status": "complete"
    }
    return response

async def run_workflow(req: Dict[str, Any]) -> Dict[str, Any]:
    state = dict(req)
    # run flights and hotels in parallel, then activities
    await asyncio.gather(fetch_flights(state), fetch_hotels(state))
    await fetch_activities(state)
    return await prepare_itinerary(state)
