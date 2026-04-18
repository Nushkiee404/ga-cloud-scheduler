import random

# sample tasks (execution times)
tasks = [10, 5, 8, 6, 12, 7, 3, 9, 4, 11]

def fitness(schedule):
    return sum(schedule)  # minimize total time (makespan approx)

def generate_population(size):
    population = []
    for _ in range(size):
        individual = random.sample(tasks, len(tasks))
        population.append(individual)
    return population

population = generate_population(5)

for i, individual in enumerate(population):
    print(f"Individual {i}: {individual}, Fitness: {fitness(individual)}")
