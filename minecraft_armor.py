import numpy as np
import matplotlib.pyplot as plt


def damage_taken(damage, defense, toughness):
    toughness_factor = defense - damage / (2 + (toughness / 4))
    damage_mult = min(20, max(defense / 5, toughness_factor)) / 25
    return damage * (1 - damage_mult)


armors = {
    'none': (0, 0),
    'iron': (15, 0),
    'diamond': (20, 2 * 4),
    'netherite': (20, 2 * 3)
}


def plot_armor(armor, color):
    damages = np.arange(0, 100, 0.1)
    damages_taken = list(map(lambda x: damage_taken(x, *armors[armor.lower()]), damages))
    plt.plot(damages, damages_taken, color=color, label=armor)


def plot():

    plot_armor('None', 'red')
    plot_armor('Iron', 'gray')
    plot_armor('Diamond', 'blue')
    plot_armor('Netherite', 'black')

    plt.legend()

    plt.xlabel('Damage Taken')
    plt.ylabel('Damage Received')

    plt.savefig('compare_armor.png')


if __name__ == '__main__':
    plot()
