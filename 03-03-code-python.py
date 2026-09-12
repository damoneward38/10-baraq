# Add these lines to baraq-backend/main.py

from routes.chazah_integration import router as chazah_router

app.include_router(
    chazah_router,
    prefix="/api/chazah",
    tags=["CHAZAH Integration"]
)