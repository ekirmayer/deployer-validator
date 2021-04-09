import argparse
import platform
from deployer_validator.environment_validation import validate_environment
from deployer_validator.supported_platforms import check_is_platform_supported


def init(help=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--validate', '-v', help="Run the pre installation validation flow", action="store_true")
    parser.add_argument('--CORSIGHT_ID', type=str, help='CORSIGHT_ID', default='1')
    if help:
        parser.print_help()
    else:
        return parser.parse_args()


if __name__ == '__main__':
    print("Running on: {}".format(platform.platform()))
    if not check_is_platform_supported():
        exit(1)
    args = init()
    if args.validate:
        print("\nRun validate")
        validate_environment(corsight_id=args.CORSIGHT_ID)
    else:
        init(True)
