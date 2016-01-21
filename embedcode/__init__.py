# GNU MediaGoblin -- federated, autonomous media hosting
# Copyright (C) 2011, 2012 MediaGoblin contributors.  See AUTHORS.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from pkg_resources import resource_filename
import os
import logging

from mediagoblin.tools import pluginapi
from mediagoblin.tools.staticdirect import PluginStatic
_log = logging.getLogger(__name__)


PLUGIN_DIR = os.path.dirname(__file__)


def setup_plugin():
    _log.info('Setting up embedcode plugin...')
    config = pluginapi.get_config('mediagoblin.plugins.embedcode')
    pluginapi.register_routes(routes)
    embedcode_template = '/mediagoblin/plugins/embedcode/embed_code.html'
    pluginapi.register_template_hooks({'media_sideinfo': embedcode_template})

hooks = {
    'setup': setup_plugin
}
