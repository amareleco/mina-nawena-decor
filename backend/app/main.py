import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.database.init_db import init_db
from app.modules.user.routes import router as user_router
from app.modules.category.routes import router as category_router
from app.modules.product.routes import router as product_router
from app.modules.supplier.routes import router as supplier_router
from app.modules.client.routes import router as client_router
from app.modules.event.routes import router as event_router
from app.modules.event_item.routes import router as event_item_router
from app.modules.movement.routes import router as movement_router
from app.modules.dashboard.routes import router as dashboard_router
from app.modules.report_product.routes import router as report_product_router
from app.modules.report_movement.routes import router as report_movement_router
from app.modules.report_event.routes import router as report_event_router
from app.modules.report_stock.routes import router as report_stock_router
from app.modules.login.routes import router as login_router

from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mina nawe Decor"
)

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Captura erros não tratados e retorna com CORS headers"""
    return JSONResponse(
        status_code=500,
        content={"detail": f"Internal server error: {str(exc)}"},
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://amareleco.github.io/mina-nawena-decor/",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()


# Routers
app.include_router(
    user_router
),
app.include_router(
    category_router
),
app.include_router(
    product_router
),
app.include_router(
    supplier_router
),
app.include_router(
    client_router
),
app.include_router(
    event_router
),
app.include_router(
    event_item_router
),
app.include_router(
    movement_router
)
app.include_router(
    dashboard_router
),

app.include_router(
    report_product_router
),
app.include_router(
    report_movement_router
),
app.include_router(
    report_event_router
),
app.include_router(
    report_stock_router
),

app.include_router(
    login_router,
    prefix=settings.API_V1_STR
)


@app.get("/")
def root():

    return {
        "message": "Decor System API running"
    }

   
# ... seu código do FastAPI anterior ...

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)