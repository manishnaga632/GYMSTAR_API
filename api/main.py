from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import auth, subscription, users, membership_plans, slider, trainers , static_manager, admin_profile, classes, contact
from api.database.connection import engine
from api.database.base import Base

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Include authentication-related routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Include user-related routes
app.include_router(users.router, prefix="/users", tags=["Users"])

app.include_router(membership_plans.router, prefix="/membership_plans", tags=["membership_plans"])

app.include_router(subscription.router, prefix="/subscription", tags=["subscription"])

app.include_router(slider.router, prefix="/slider", tags=["slider"])

app.include_router(trainers.router, prefix="/trainers", tags=["trainers"])

app.include_router(static_manager.router, prefix="/static_manager", tags=["static_manager"])

app.include_router(admin_profile.router, prefix="/admin_profile", tags=["admin_profile"])

app.include_router(classes.router, prefix="/classes", tags=["classes"])

app.include_router(contact.router, prefix="/contact", tags=["contact"])


# ✅ Add Health Check Route (root "/")
@app.get("/")
def health_check():
    return {"status": "ok"}












# git add .
# git commit -m "Add python-dateutil for subscription date handling"
# git push origin main


