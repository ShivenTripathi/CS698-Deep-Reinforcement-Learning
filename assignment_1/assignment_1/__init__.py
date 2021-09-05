from gym.envs.registration import register

register(
    id='gaussianBandit',
    entry='assignment_1.envs:GaussianBanditEnv',
)
register(
    id='bernoulliBandit',
    entry='assignment_1.envs:BernoulliBanditEnv',
)
register(
    id='RWE',
    entry='assignment_1.envs:RWEEnv',
)