=====================
mediagoblin-embedcode
=====================

This plugin adds the ability to display "embed code" for video media types. 
The plugin uses template hooks to create an additional section in the media 
sidebar and display code to allow the current video to be embedded on an 
external page.

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
