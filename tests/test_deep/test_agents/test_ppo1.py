import shutil

from genrl import PPO1
from genrl.deep.common import OnPolicyTrainer
from genrl.environments import VectorEnv


def test_ppo1():
    env = VectorEnv("CartPole-v0")
    algo = PPO1("mlp", env, rollout_size=128)
    trainer = OnPolicyTrainer(algo, env, log_mode=["csv"], logdir="./logs", epochs=1)
    trainer.train()
    shutil.rmtree("./logs")


def test_ppo1_cnn():
    env = VectorEnv("Pong-v0", env_type="atari")
    algo = PPO1("cnn", env, rollout_size=128)
    trainer = OnPolicyTrainer(algo, env, log_mode=["csv"], logdir="./logs", epochs=1)
    trainer.train()
    shutil.rmtree("./logs")
