import math, sys

# Takes in path, returns end position [Left/Right, Front/Back]
def path_distance(path: str) -> [int, int]:
    current_number = 0
    position = [0, 0]
    for char in path:
        if char in ['F', 'B', 'R', 'L']:
            if char == 'F': #Forward
                position[1] += current_number
            elif char == 'B':#Backward
                position[1] -= current_number
            elif char == 'R':#Right
                position[0] += current_number
            elif char == 'L':#Left
                position[0] -= current_number
            current_number = 0
        elif char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            raise ValueError(f"Invalid character: {char}")
    return position

def euclidean_distance(position: [int, int]) -> int:
    return math.sqrt(position[0]**2 + position[1]**2)

def main(path: str="15F6B6B5L16R8B16F20L6F13F11R"):
    distance = euclidean_distance(path_distance(path))
    print(f"Distance: {distance}")
    return distance

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = sys.argv[1]
        main(path)
    else:
        main()