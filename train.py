from marllib import marl


def train_sample():
    # prepare the environment academy_pass_and_shoot_with_keeper
    # can add extra env params. remember to check env configuration before use
    env = marl.make_env(environment_name="football", map_name="academy_pass_and_shoot_with_keeper")

    # initialize algorithm and load hyperparameters
    mappo = marl.algos.mappo(hyperparam_source="common")
    # can add extra algorithm params. remember to check algo_config hyperparams before use
    # mappo = marl.algos.MAPPO(hyperparam_source='common', use_gae=True,  batch_episode=10, kl_coeff=0.2, num_sgd_iter=3)
    # build agent model based on env + algorithms + user preference if checked available
    model = marl.build_model(env, mappo, {"core_arch": "mlp", "encode_layer": "128-256"})

    # start learning + extra experiment settings if needed. remember to check ray.yaml before use
    mappo.fit(env, model, stop={'episode_reward_mean': 200, 'timesteps_total': 20000},
            local_mode=False,
            share_policy='all', checkpoint_freq=50)





if __name__ == '__main__':
    train_sample()