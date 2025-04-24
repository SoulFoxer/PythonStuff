import yaml

class AppInfo:
    def __init__(self, name, url, commit, conan_file):
        self.name = name
        self.url = url
        self.commit = commit
        self.conan_file = conan_file

class Config:
    def __init__(self, release_branch, devkit_version, apps):
        self.release_branch = release_branch
        self.devkit_version = devkit_version
        self.apps = apps

    def get_app_by_name(self, name):
        return self.apps.get(name)

def load_config(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)

    apps = {}
    for app_name, app_data in data['apps'].items():
        apps[app_name] = AppInfo(
            app_name,
            app_data.get('url', 'default_url'),
            app_data.get('commit', 'default_commit'),
            app_data.get('conan-file', 'default_conan_file')
        )
    
    return Config(
        release_branch=data['release_branch'],
        devkit_version=data['devkit_version'],
        apps=apps
    )
