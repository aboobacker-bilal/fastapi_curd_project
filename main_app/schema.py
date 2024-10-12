def individual_data(item):
    return {
        "id": str(item["_id"]),
        "name": item.get("name", ""),
        "email": item.get("email", ""),
        "item_name": item.get("item_name", ""),
        "quantity": item.get("quantity", 0),
        "expiry_date": item.get("expiry_date", None),
        "insert_date": item.get("insert_date", None)
    }


def all_task(items):
    return [individual_data(item) for item in items]


def individual_record(record):
    return {
        "id": str(record["_id"]),
        "email": record["email"],
        "location": record["location"],
        "insert_date": record.get("insert_date", None)
    }


def all_records(records):
    return [individual_record(rec) for rec in records]
