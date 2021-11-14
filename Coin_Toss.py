### Script to simulate a large number of coin tosses using multiprocessing ###
from tqdm import trange
from random import randint
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count
import os


def coingame(flips: int) -> list:
    heads = tails = 0
    for i in trange(flips, desc=f'Game Progress'):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
        
    return [heads, tails]
    
    
def main():
    # Determining the number of games and flips per game
    num_games = 10
    num_flips = 1000000
    total_num = [num_flips] * num_games

    # Using multiprocessing to run all games at the same time
    with Pool() as pool:
        res = pool.map(coingame, total_num)
    
    # Consolidating the results from all games
    heads = tails = 0
    for l in res:
        heads += int(l[0])
        tails += int(l[1])
    
    # Printing the results and showing the distribution with a pie graph
    print(f"Heads: {heads:,}, Tails: {tails:,}, Total: {heads + tails:,}")
    plt.pie([heads, tails], labels=['Heads', 'Tails'], autopct='%1.1f%%')
    plt.title('Heads/Tails')
    plt.axis('equal')
    plt.show()
    
    
if __name__ == '__main__':
    main()
    