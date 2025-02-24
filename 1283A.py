def minutes_before_new_year(t, test_cases):
    results = []
    total_minutes_in_day = 1440

    for h, m in test_cases:
        elapsed_minutes = h * 60 + m
        remaining_minutes = total_minutes_in_day - elapsed_minutes
        results.append(remaining_minutes)

    return results

t = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(t)]
results = minutes_before_new_year(t, test_cases)

# Output each result
for result in results:
    print(result)
