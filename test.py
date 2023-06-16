import gfootball.env as football_env
from marllib import marl

env = marl.make_env(environment_name="football", map_name="academy_pass_and_shoot_with_keeper")