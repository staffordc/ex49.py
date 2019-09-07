stuff = input('> ')


def scan(words):
    results = []
    directions = {'north', 'east', 'west', 'south'}
    verbs = {'go', 'kill', 'eat'}
    stops = {'the', 'in', 'of', 'from', 'at', 'it'}
    nouns = {'door', 'bear', 'princess', 'cabinet'}

    words = convert_lower(words)

    splitwords = words.split()

    for word in splitwords:
        if word in directions:
            results.append(('direction', word))
        elif word in verbs:
            results.append(('verb', word))
        elif word in stops:
            results.append(('stop', word))
        elif word in nouns:
            results.append(('noun', word))
        elif word.isdigit():
            numb = convert_numbers(word)
            results.append(('number', numb))
        else:
            results.append(('error', word))
    return results


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


def convert_lower(a):
    try:
        return a.lower()
    except ValueError:
        return None

    # def go_direction():
    # once the direction is recieved we can have them go to the room in that direction

    # def stop
