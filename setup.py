from setuptools import setup

setup(name='gym_surfacecode',
      version='0.0.1',
      install_requires=['gym','keras'],
      packages=['gym_surfacecode'],
      package_dir={'gym_surfacecode': 'mypkg'},
      package_data={'gym_surfacecode': ['envs/referee_decoder/X_decoder','envs/referee_decoder/DP_decoder']},)