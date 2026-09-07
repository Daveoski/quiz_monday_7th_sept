from typing import Annotated
from fastapi import FastAPI, Header, Cookie, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="This is My quiz VIP Registration Desk")
class StaffHeaders(BaseModel):
    x_union_pass: Annotated[
        str,
        Header()
    ]
    x_client_version: Annotated[str, Header()] = "1.0"
class StaffCreate(BaseModel):
    username: str = Field(examples=["daveoski_vip"])
    full_name: str | None = Field(default=None, examples=["Okechukwu David"])
    password: str = Field(min_length=8, examples=["VIPpass2026"])
    station: str = Field(examples=["Lagos VIP Desk"])
class StaffResponse(BaseModel):
    username: str
    full_name: str | None = None
    station: str
class DeskCookies(BaseModel): session_id: Annotated[str,Cookie()]
language: Annotated[str, Cookie()] = "en"
@app.post("/staff", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
async def register_staff(
    headers: Annotated[StaffHeaders, Header()],
    staff: StaffCreate
) -> StaffCreate:
    if headers.x_union_pass != "UNION-2026-VIP":
        raise HTTPException(status_code=401, detail="Wrong pass.")
    return staff

@app.get("/desk/greeting")
async def desk_greeting(
    cookies: Annotated[DeskCookies, Cookie()]
) -> dict:
    if cookies.language == "en":
        greeting = "Welcome back!"
    elif cookies.language == "pidgin":
        greeting = "How far, you don come again!"
    else:
        greeting = "Welcome!"
    return {
        "greeting": greeting,
        "session_id": cookies.session_id
    }