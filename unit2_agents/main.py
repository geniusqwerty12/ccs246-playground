from agent import Agent
from environment import Environment

def main():
    agent = Agent()
    environment = Environment()

    while True:
        perception = agent.perceive(environment)
        action = agent.decide()
        environment.update(action)


if __name__ == "__main__":
    main()