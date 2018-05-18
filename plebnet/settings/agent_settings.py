"""
This subclass of settings is used to store the agent configuration.

This configuration should contain values which are set on initialization
of the first parent, and can change during the cloning process or during
the lifespan of the specific agent.

The file it self can be found in the PATH_TO_FILE location.
"""

# Total imports
import os

# Partial imports

# Local imports
from plebnet.settings import setting

# File parameters
PATH_TO_FILE = "plebnet/settings/configuration/agent.cfg"


class AgentSettings(object):

    def __init__(self):
        self.filename = os.path.join(os.path.expanduser("~/PlebNet"), PATH_TO_FILE)
        self.settings = setting.Settings(self.filename)
        self.settings.load()

    def get_uploaded(self):
        return self.settings.get("data", "uploaded")
