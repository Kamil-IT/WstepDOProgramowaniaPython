import random

import gym
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, IntegerLookup, Layer
from tensorflow.keras.optimizers import Adam
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory
import gym_battleship



def random_game():
    random_choice_max = [0 for i in range(0, 100)]
    random_choice = [0 for i in range(0, 100)]

    for episode in range(1, 1000):
        state = env.reset()
        done = False
        score = 0
        max_score = 0

        while not done:
            # env.render() - visualization of board
            action = random.choice(range(0, 100))
            n_state, reward, done, info = env.step(action)
            score += reward
            if reward < 0:
                random_choice[action] += 1
            if done == True and max_score < score:
                random_choice_max = random_choice
                max_score = score
            if done == True:
                score = 0
        # print('Episode:{} Score:{}'.format(episode, score))

    return random_choice_max


def simulate_game(random_chances):
    random_score = 0
    done = False
    while not done:
        action = random_chances.index(max(random_chances))
        random_chances[action] = 0
        n_state, reward, done, info = env.step(action)
        random_score += reward

    return random_score

def build_model(states, actions):
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

def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn

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


# Random simulation
random_choice = random_game()
max_random_choice = sum(random_choice)
random_chances = [i / max_random_choice for i in random_choice]
random_score = simulate_game(random_chances)
print(f'random score: {random_score}')


# Rl simulation
model = build_model(OBSERVATION_SPACE, ACTION_SPACE)

dqn = build_agent(model, ACTION_SPACE)
dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])
dqn.fit(env, nb_steps=200, visualize=False, verbose=1)

scores = dqn.test(env, nb_episodes=100, visualize=False)
print(f"RL: {np.mean(scores.history['episode_reward'])}")
print(f"Random: {random_score}")
