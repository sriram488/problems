def sort_colors(colors):
    start, current, end = 0, 0, len(colors) - 1

    while current <= end:
        if colors[current] == 0:
            # Swap with start position
            colors[start], colors[current] = colors[current], colors[start]
            current += 1
            start += 1
        elif colors[current] == 1:
            current += 1
        else:  # colors[current] == 2
            # Swap with end position
            colors[current], colors[end] = colors[end], colors[current]
            end -= 1
    return colors

# Test the function
if __name__ == "__main__":
    # Test case 1
    colors1 = [2, 0, 2, 1, 1, 0]
    print("Original:", colors1)
    result1 = sort_colors(colors1)
    print("Sorted:", result1)
    
    # Test case 2
    colors2 = [2, 0, 1]
    print("\nOriginal:", colors2)
    result2 = sort_colors(colors2)
    print("Sorted:", result2)
