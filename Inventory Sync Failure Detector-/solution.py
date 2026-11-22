from typing import List, Dict

def detect_sync_failures(
    warehouse: Dict[str, int],
    online_store: Dict[str, int]
) -> Listfailures = []

    all_products = set(warehouse.keys()) | set(online_store.keys())

    for product in all_products:
        warehouse_stock = warehouse.get(product, 0)
        online_stock = online_store.get(product, 0)

        if warehouse_stock != online_stock:
            failures.append({
                "product": product,
                "warehouse_stock": warehouse_stock,
                "online_stock": online_stock,
                "difference": warehouse_stock - online_stock
            })

    return failures


# Example
warehouse = {
    "P101": 50,
    "P102": 30,
    "P103": 20
}

online_store = {
    "P101": 50,
    "P102": 25,
    "P104": 10
}

result = detect_sync_failures(warehouse, online_store)

for item in result:
    print(item)
