import config
import player
import math
import species
import operator



class Population:

    def __init__(self, size):
        self.players = []
        self.generation = 1
        self.species = []
        self.size = size
        for i in range(0, self.size):
            self.players.append(player.Player())


    def update_live_players(self):
        for p in self.players:
            if p.alive:
                p.look()
                p.think()
                p.draw(config.window)
                p.update(config.ground)

    def natural_selection(self):
        print('SPECIATE')
        self.speciate()

        print('CALCULATE FITNESS')
        self.calculate_fitness()

        print('SORT BY FITNESS')
        self.sort_species_by_fitness()

        print('CHILDREN FOR NEXT GEN')
        self.next_gen()

    def speciate(self):
        for s in self.species:
            s.players = []

        for p in self.players:
            add_to_species = False
            for s in self.species:
                if s.similarity(p.brain):
                    s.add_to_species(p)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(p))
    
    def calculate_fitness(self):
        s

    #return true if all players are dead
    def extinct(self):
        extinct = True
        for p in self.players:
            if p.alive:
                extinct = False
        return extinct
