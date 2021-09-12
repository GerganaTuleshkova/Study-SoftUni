population_wealth = [int(x) for x in input().split(", ")]
minimum = int(input())
max_wealth = max(population_wealth)

if sum(population_wealth) / len(population_wealth) < minimum:
    print("No equal distribution possible")
else:
    while min(population_wealth) < minimum:
        for index in range(len(population_wealth)):
            individual = population_wealth[index]
            max_wealth = max(population_wealth)
            if individual < minimum and (max_wealth - minimum) >= (minimum - individual):
                population_wealth[index] += minimum - individual
                population_wealth[population_wealth.index(max_wealth)] -= minimum - individual
            elif individual < minimum and (max_wealth - minimum) > 0:
                population_wealth[index] += max_wealth - minimum
                population_wealth[population_wealth.index(max_wealth)] = minimum

    print(population_wealth)
