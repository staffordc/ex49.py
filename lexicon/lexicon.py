# stuff = input('> ')
# words = stuff.split()


def scan(words):
    results = []
    direction_north = ('direction', 'north')
    direction_east = ('direction', 'east')
    direction_west = ('direction', 'west')
    direction_south = ('direction', 'south')
    splitwords = words.split()
    for word in splitwords:
        results.append(('direction', word))
    return results

    # def go_direction():
    # once the direction is recieved we can have them go to the room in that direction

    # def stop
