def productEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item["description"]
    }


def show_all_products(query) -> list:
    return [productEntity(item) for item in query]