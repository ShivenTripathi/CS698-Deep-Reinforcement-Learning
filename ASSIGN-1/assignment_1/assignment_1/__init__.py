from gym.envs.registration import register

register(
    id='gaussianBandit-v0',
    entry_point='assignment_1.envs:gaussianBandit',
)
register(
    id='bernoulliBandit-v0',
    entry_point='assignment_1.envs:bernoulliBandit',
)
register(
    id='RWE-v0',
    entry_point='assignment_1.envs:RWE',
)