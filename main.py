orders = [
    {"id": 1, "customer": "Alice", "amount": 250, "status": "paid"},
    {"id": 2, "customer": "Bob", "amount": 80, "status": "pending"},
    {"id": 3, "customer": "Alice", "amount": 120, "status": "paid"},
    {"id": 4, "customer": "Carol", "amount": 300, "status": "paid"},
    {"id": 5, "customer": "Bob", "amount": 45, "status": "cancelled"},
]
# Get a set of all unique customer names.
# Get a list of order ids where status == "paid".
# Build a dict mapping customer -> total amount spent, but only counting "paid" orders.
# (This one's trickier — you'll need to think about how to sum per customer without a plain loop.
# Hint: you can nest a comprehension inside a dict comprehension, using the set from #1.)
# Give it a shot.
name_set = {x["customer"] for x in orders}
paid_order_ids = {x["id"] for x in orders if x["status"] == "paid"}
dic = {x: sum([a["amount"] for a in orders if a["status"] == "paid" and a["customer"] == x]) for x in name_set}
print(name_set, paid_order_ids, dic)
