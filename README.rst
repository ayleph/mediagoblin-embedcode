=====================
mediagoblin-embedcode
=====================

This plugin adds the ability to display an "embed code" for video and audio media types.
The plugin uses template hooks to create an additional section in the media
sidebar and display code to allow the current video or audio to be embedded on an
external page.

Compatibility
=====================

This plugin has been tested with mediagoblin 0.9.0

Set up the plugin
=================

1. Retrieve the plugin from its public git repository.

::

  $ git clone https://github.com/ayleph/mediagoblin-embedcode.git

2. Copy the plugin to your MediaGoblin plugin path.

::

  $ cp -r mediagoblin-embedcode/embedcode /path/to/mediagoblin/mediagoblin/plugins/

3. Enable the plugin adding the following line to the ``[plugins]`` section of
   your mediagoblin config file.

::

  [[mediagoblin.plugins.embedcode]]
