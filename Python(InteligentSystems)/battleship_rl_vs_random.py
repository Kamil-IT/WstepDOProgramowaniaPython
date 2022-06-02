import random

import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, IntegerLookup, Layer
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent, NAFAgent, CEMAgent, SARSAAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory, EpisodeParameterMemory
import gym_battleship



def random_game():
    random_choice = [0 for i in range(0, 100)]

    for episode in range(1, 1000):
        state = env.reset()
        done = False
        score = 0

        # Board generator
        state = env.reset()
        generated = env.unwrapped.board_generated


        while not done:
            # env.render() # - visualization of board
            action = random.choice(range(0, 100))
            n_state, reward, done, info = env.step(action)
            score += reward
            if reward < 0:
                random_choice[action] += 1
        # print('Episode:{} Score:{}'.format(episode, score))

    return random_choice


def simulate_game(random_chances):
    random_score = 0
    done = False
    env.reset()
    while not done:
        action = random_chances.index(max(random_chances))
        random_chances[action] = 0
        n_state, reward, done, info = env.step(action)
        random_score += reward

    return random_score

def build_model_sequential(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, 2, 10, 10)))
    # model.add(Dense(24, activation='relu'))
    # model.add(Dense(24, activation='relu'))
    # model.add(Dense(1024, activation='relu'))
    # model.add(Dense(512, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

def build_model_neuron(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1, 2, 10, 10)))
    # model.add(Dense(24, activation='relu'))
    # model.add(Dense(24, activation='relu'))
    # model.add(Dense(1024, activation='relu'))
    # model.add(Dense(512, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model

def build_agent_DQN(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

def train_show_results(name, agent):
    agent.fit(env, nb_steps=200, visualize=False, verbose=1)
    scores = agent.test(env, nb_episodes=100, visualize=False)
    return f"{name}: {np.mean(scores.history['episode_reward'])}"

# Build env
# https://github.com/thomashirtz/gym-battleship
env = gym.make('Battleship-v0',
               reward_dictionary={
                   'win': 0,
                   'missed': 0,
                   'touched': -10, # hitted
                   'repeat_missed': 5,
                   'repeat_touched': -30
               })
OBSERVATION_SPACE = env.observation_space.shape[0]
ACTION_SPACE = env.action_space.n

results = []

# Random simulation
random_choice = random_game()
max_random_choice = sum(random_choice)
random_chances = [i / max_random_choice for i in random_choice]
random_score = simulate_game(random_chances)
results.append(f'random score: {random_score}')


def neuron_simulation(model, actions, results):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    naf = SARSAAgent(model=model, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10)

    memory_CEM = EpisodeParameterMemory(limit=1000, window_length=1)
    cema = CEMAgent(model=model, memory=memory_CEM,
                   nb_actions=actions, nb_steps_warmup=10)


    dqn.compile(optimizer=Adam(learning_rate=1e-3))
    results.append(train_show_results('RL-neuron-DQNAgent', dqn))

    naf.compile(optimizer=Adam(learning_rate=1e-3))
    results.append(train_show_results('RL-neuron-NAFAgent ', naf))

    cema.compile()
    results.append(train_show_results('RL-neuron-cema_agent', cema))


def sequential_simulation(model, actions, results):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    naf = SARSAAgent(model=model, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10)

    memory_CEM = EpisodeParameterMemory(limit=1000, window_length=1)
    cema = CEMAgent(model=model, memory=memory_CEM,
                   nb_actions=actions, nb_steps_warmup=10)


    dqn.compile(optimizer=Adam(learning_rate=1e-3))
    results.append(train_show_results('RL-sequential-DQNAgent', dqn))

    naf.compile(optimizer=Adam(learning_rate=1e-3))
    results.append(train_show_results('RL-sequential-NAFAgent ', naf))

    cema.compile()
    results.append(train_show_results('RL-sequential-cema_agent', cema))


# Nauron simulation
model_neuron = build_model_neuron(OBSERVATION_SPACE, ACTION_SPACE)
neuron_simulation(model_neuron, ACTION_SPACE, results)

# Rl simulation
model_neuron = build_model_sequential(OBSERVATION_SPACE, ACTION_SPACE)
sequential_simulation(model_neuron, ACTION_SPACE, results)

# print score
print(results)
