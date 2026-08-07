dataset = [
    ("Cat",0.95),
    ("Dog",0.82),
    ("Bird",0.99)
]

sorted_dataset = sorted(
    dataset,
    key = lambda data:data[1]
)

print(sorted_dataset)