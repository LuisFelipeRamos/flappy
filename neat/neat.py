import os
import neat
import pickle


def run(config_path: str) -> None:
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    population = neat.Population(config)


if __name__ == "__main__":
    local_dir: str = os.path.dirname(__file__)
    config_path: str = os.path.join(local_dir, "config.txt")
    run(config_path=config_path)
