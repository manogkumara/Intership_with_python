def convert_to_positive_coordinates(coordinates):
    if not coordinates:
        return []

    # Find the minimum x and y values
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)

    # Calculate the offsets
    x_offset = abs(min_x)
    y_offset = abs(min_y)

    # Add the offsets to all coordinates
    positive_coordinates = [(coord[0] + x_offset, coord[1] + y_offset) for coord in coordinates]

    return positive_coordinates

# Test the function with the provided input
input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coordinates = convert_to_positive_coordinates(input_coordinates)

print(output_coordinates)
