
def validate_task(data):
    if "title" not in data:
        return False, "Missing title"
    return True, None