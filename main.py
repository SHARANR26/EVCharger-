from fastapi import FastAPI
import geocoder
import requests

app = FastAPI()

@app.get("/sample")
async def sample_endpoint():
    return {"message": "This is a sample endpoint"}

@app.get("/api-request")
async def api_request():
    # Sample API request to an external service (e.g., JSONPlaceholder API)
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

@app.get("/current-location")
async def get_current_location():
    # Get location based on the IP address
    g = geocoder.ip('me')
    location_info = {
        "city": g.city,
        "state": g.state,
        "country": g.country,
        "latitude": g.latlng[0] if g.latlng else None,
        "longitude": g.latlng[1] if g.latlng else None
    }
    return location_info

@app.get("/replay-location")
async def replay_location():
    # Retrieve the current location and return it
    location = get_current_location()
    return location
