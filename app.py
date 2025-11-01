def add(a, b):
    return a + b

def lambda_handler(event, context):
    a = event.get("a")
    b = event.get("b")
    return {"result": add(a, b)}