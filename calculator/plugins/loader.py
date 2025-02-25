import importlib
import os

def load_plugins():
    plugins = {}
    plugin_directory = os.path.dirname(__file__)
    for filename in os.listdir(plugin_directory):
        if filename.endswith('_plugin.py'):
            module_name = f"plugins.{filename[:-3]}"
            module = importlib.import_module(module_name)
            plugin = module.get_plugin()
            plugins[plugin['name']] = plugin['class']
    return plugins