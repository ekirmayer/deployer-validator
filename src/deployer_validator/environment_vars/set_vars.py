import os


def set_global_env_variable_profile(corsight_id):
    try:
        # Set environment for other terminal sessions
        with open('/etc/profile.d/CORSIGHT_ID.sh', 'w') as global_profile:
            global_profile.write(f'export CORSIGHT_ID={corsight_id}')
        # Set value for current session
        os.environ["CORSIGHT_ID"] = corsight_id
    except Exception as error:
        print(f'Failed to set the environment profile due to {error.__doc__}')
