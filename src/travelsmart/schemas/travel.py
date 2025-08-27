from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class TravelRequest(BaseModel):
    source: str
    destination: str
    start_date: str
    end_date: str
    currency: str = "USD"

class ItineraryItem(BaseModel):
    id: str
    type: str
    price: float
    start: Optional[str] = None
    end: Optional[str] = None
    name: Optional[str] = None
    from_: Optional[str] = Field(None, alias="from")
    to: Optional[str] = None
    meta: Optional[Dict[str, Any]] = None
    address: Optional[str] = None
    location: Optional[str] = None

class Itinerary(BaseModel):
    alternatives: Dict[str, Any]
    currency: str
    totals: Dict[str, float]
    items: List[ItineraryItem]

class TravelResponse(BaseModel):
    itinerary: Itinerary
    status: str
