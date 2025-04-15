def feedAnimals(animals, food):
    count = 0
    animals = sorted(animals)
    food = sorted(food)
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            return count
    return count