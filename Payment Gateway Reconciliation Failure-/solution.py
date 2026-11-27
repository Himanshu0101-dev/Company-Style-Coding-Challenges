def find_missing_transactions(gateway, database):
    db_set = set(database)

    missing = []

    for transaction in gateway:
        if transaction not in db_set:
            missing.append(transaction)

    return missing


gateway = [101,102,103,104,105,106]
database = [101,103,104,106]

print(find_missing_transactions(gateway, database))
