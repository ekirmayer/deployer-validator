import platform


def check_is_platform_supported():
    supported_platforms = ['Ubuntu']
    supported_platforms_by_version = ['Ubuntu_18.04']
    t = platform.dist()
    if not supported_platforms.__contains__(t[0]):
        print("The current OS ({0}) is not supported. Please contact the Support team".format(platform.system()))
        return False
    current_system = "{}_{}".format(t[0],t[1])
    if not supported_platforms_by_version.__contains__(current_system):
        print("The current OS ({0}) is not supported. Please contact the Support team".format(current_system))
        return False
    else:
        return True
