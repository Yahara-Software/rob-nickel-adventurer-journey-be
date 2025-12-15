# Takes in path, returns distance ver
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
            #print(f"Moved {current_number} steps {char} to {position}")
            current_number = 0
        elif char.isdigit():
            current_number = current_number * 10 + int(char)
        else:
            raise ValueError(f"Invalid character: {char}")
    return position

def main():
    path = "15F6B6B5L16R8B16F20L6F13F11R"
    print(f"Current position: {path_distance(path)}")

if __name__ == "__main__":
    main()