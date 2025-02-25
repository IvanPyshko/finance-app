from fastapi import FastAPI
from routes import journal_routes, acct_routes, category_routes, comment_routes

app = FastAPI()

app.include_router(journal_routes.router, prefix="/journal", tags=["journal"])
app.include_router(acct_routes.router, prefix="/acct", tags=["accounts"])
app.include_router(category_routes.router, prefix="/category", tags=["categories"])
app.include_router(comment_routes.router, prefix= "/comment", tags = ["comments"])


@app.get("/")
def root():
    return {"message": "Accounting System is running"}
