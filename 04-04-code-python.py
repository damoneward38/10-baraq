# Add these lines to chazah-backend/main.py

from routes.baraq_bridge import router as baraq_bridge_router

app.include_router(
    baraq_bridge_router,
    prefix="/api/baraq",
    tags=["BARAQ Bridge"]
)