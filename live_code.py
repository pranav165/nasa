software_dependency_list = {
    "unittest": "testdata",
    "testdata": "metapy",
    "metapy": "colorpy",
    "colorpy": "pyruby",
    "pyfail": "colorpy",
    "pyruby": None,
    "pychecks": "colorpy",
    "pycff": "pyruby",
    "abc": "xyz",
    "xyz": None
}

output = []
orig_package = 'unittest'


def get_package_dependencies(package_name=None):
    for package, dependency in software_dependency_list.items():
        if package == package_name and dependency:
            if dependency == orig_package:
                raise Exception("Circular dep found")
            print("Package {} has dependecy on {}".format(package, dependency))
            if dependency not in output:
                output.append(dependency)
            get_package_dependencies(package_name=dependency)
    return output


def single_package(package_name):
    get_package_dependencies(package_name=package_name)
    output.append(package_name)
    print(output)


def multi_package(package_names):
    for package in package_names:
        get_package_dependencies(package_name=package)
        if package not in output:
            output.append(package)
    print(output)


if __name__ == '__main__':
    single_package(package_name='unittest')
    # multi_package(package_names=['unittest', 'metapy', 'abc', 'pyruby'])
