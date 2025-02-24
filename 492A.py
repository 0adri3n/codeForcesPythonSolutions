def max_pyramid_height(n):
    total_cubes_used = 0
    level = 0
    
    while True:
        level += 1
        cubes_for_current_level = (level * (level + 1)) // 2
        if total_cubes_used + cubes_for_current_level > n:
            break
        total_cubes_used += cubes_for_current_level
    
    return level - 1

n = int(input())
print(max_pyramid_height(n))
