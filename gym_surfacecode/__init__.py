from gym.envs.registration import register

register(
    id='surfacecode-v0',
    entry_point='gym_surfacecode.envs:SurfaceCodeEnv')