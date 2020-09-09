data = [
    ["Edward", 123],
    ["Doug", 123123],
    ["Edward", 2432],
    ["Edward", 2432],
    ["Umair", 345],
    ["Edward", 2432]
]
results = {}
for candidate, votes in data:
    if candidate in results:
        results[candidate] += votes
    else:
        results[candidate] = votes

    print(50 * "=")
    print(results)
print(50 * "=")
