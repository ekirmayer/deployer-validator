from deployer_validator.general.coins import flip_coin
from deployer_validator.disk.info import get_disks_info
from deployer_validator.environment_vars.set_vars import set_global_env_variable_profile
from deployer_validator.environment_vars.read_vars import  print_all


def validate_environment(corsight_id):
    get_disks_info()
    set_global_env_variable_profile(corsight_id)
    print_all()
    flip_coin()
