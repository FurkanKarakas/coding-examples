"""https://leetcode.com/problems/car-fleet/description/

Important things to note:

* The last car will always form a fleet.
* The 2nd-to-last can check if its arrival time is before the arrival time of the last car.
If it is the case, then it doesn't form a new fleet and the 3rd-to-last-car can just compare itself to the
arrival time of the last car (the variable won't be modified by the 2nd-to-last car,
i.e. the first fleet will arrive at the same time).
"""


def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    # Sort the cars by their positions
    position_indices = [i for i in range(len(position))]
    position_indices.sort(key=lambda i: position[i])
    position.sort()
    speed = [speed[i] for i in position_indices]

    prev_time_of_arrival = -float("inf")
    result = 0
    for i in range(len(position)-1, -1, -1):
        current_position = position[i]
        current_speed = speed[i]
        distance_to_target = target-current_position
        time_of_arrival = distance_to_target/current_speed

        if time_of_arrival > prev_time_of_arrival:
            # This creates a new convoy
            result += 1
            prev_time_of_arrival = time_of_arrival
    return result


if __name__ == "__main__":
    target, position, speed = 12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]
    print(carFleet(target, position, speed))
