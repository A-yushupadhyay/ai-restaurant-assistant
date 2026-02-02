from fastapi import APIRouter
from app.schemas.restaurant import Restaurant
from app.services.restaurant_store import restaurant_store
from app.schemas.menu import MenuItem

from fastapi import UploadFile, File
from app.services.menu_ocr import parse_menu_from_file

from fastapi import APIRouter, UploadFile, File
from app.services.s3_client import upload_menu_file


router = APIRouter()


@router.post("/restaurant")
def create_restaurant(restaurant: Restaurant):
    restaurant_store.add(restaurant)
    return {"status": "created", "restaurant_id": restaurant.id}


@router.post("/restaurant/{restaurant_id}/menu")
def upload_menu(restaurant_id: str, menu: list[MenuItem]):
    # For now: attach menu to restaurant context later
    return {
        "status": "menu uploaded",
        "restaurant_id": restaurant_id,
        "items": len(menu),
    }


@router.post("/restaurant/{restaurant_id}/menu/ocr")
async def upload_menu_ocr(
    restaurant_id: str,
    file: UploadFile = File(...)
):
    # menu_items = await parse_menu_from_file(file)
    file_bytes = await file.read()

    s3_path = upload_menu_file(
        file_bytes=file_bytes,
        filename=file.filename,
    )

    # 🔁 Reuse existing JSON menu upload behavior
    return {
        "status": "uploaded",
        "restaurant_id": restaurant_id,
        "file_location": s3_path,
    }