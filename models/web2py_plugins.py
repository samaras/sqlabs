# -*- coding: utf-8 -*-

info_plugin_metas = dict(
    plugin_solidform=dict(
        label='Solid Form',
        short_description='A custom SQLFORM with denser layout',
        long_description='',
    ),
    plugin_notemptymarker=dict(
        label='Not-Empty Marker',
        short_description='Automatically adding not-empty marker for forms',
        long_description='',
    ),
    plugin_hradio_widget=dict(
        label='Horizontal Radio Widget',
        short_description='A radio widget arranging its radio buttons horizontally',
        long_description=SPAN(
A("A built-in radio widget in web2py", _href="http://web2py.com/examples/static/epydoc/web2py.gluon.sqlhtml.RadioWidget-class.html"), 
""" arranges its radio buttons vertically, which occupies a relatively large area. 
Here we implemented a horizontal radio widget, and further made it clickable for it's labels. 
"""),
    ),
    plugin_multiselect_widget=dict(
        label='Multiple Select Widget',
        short_description='A user-friendly multiple options widget',
        long_description=SPAN(
A("A built-in multiple options widget in web2py", _href="http://web2py.com/examples/static/epydoc/web2py.gluon.sqlhtml.MultipleOptionsWidget-class.html"),
""" is made by a single select input tag,
which would be difficult to handle when it had many options.
We built more user-friendly multiple select widget with two select input tags.
"""),
    ),
    plugin_suggest_widget=dict(
        label='Suggest Widget',
        short_description='A refined autocomplete widget',
        long_description='',
    ),
    plugin_lazy_options_widget=dict(
        label='Lazy Options Widget',
        short_description='A lazy loading options widget triggered by a js event',
        long_description='',
    ),
    plugin_anytime_widget=dict(
        label='Anytime Widget',
        short_description='A date-time picker widget using anytime.js',
        long_description='',
    ),
    plugin_color_widget=dict(
        label='Color Widget',
        short_description='A color picker widget using colorpicker.js',
        long_description='',
    ),
    plugin_elrte_widget=dict(
        label='elRTE WYSIWYG Widget',
        short_description='A WYSIWYG editor widget using elRTE.js',
        long_description='',
    ),
    plugin_uploadify_widget=dict(
        label='Uploadify Widget',
        short_description='A file upload widget using uploadify.js',
        long_description='',
    ),
    plugin_solidtable=dict(
        label='Solid Table',
        short_description='A custom SQLTable with denser layout',
        long_description='',
    ),
    plugin_paginator=dict(
        label='Pagenator',
        short_description='A standard paginator',
        long_description='',
    ),
    plugin_tablescope=dict(
        label='Table Scope',
        short_description='A standard table scope selector',
        long_description='',
    ),
    plugin_tablecheckbox=dict(
        label='Table Checkbox',
        short_description='Attaching checkboxes to a table',
        long_description='',
    ),
    plugin_tablepermuter=dict(
        label='Table Permuter',
        short_description='Making table rows permutable',
        long_description='',
    ),
    plugin_mptt=dict(
        label='Modified Preorder Tree Traversal',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_treeviewer=dict(
        label='Tree Viewer',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_revision_crud=dict(
        label='Revision CRUD',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_generic_menu=dict(
        label='Generic Menu',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_tagging=dict(
        label='Tagging',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_recommender=dict(
        label='Recommender',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_crontools=dict(
        label='Cron Tools',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_deploytools=dict(
        label='Deploy Tools',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
    plugin_testtools=dict(
        label='Test Tools',
        show_image=False,
        short_description='',
        long_description='',
        status='under-construction',
    ),
)

if request.controller.startswith('plugin_'):
    import os
    from gluon.storage import Storage

    def _to_code(lines):
        return CODE(''.join(lines[1:]).strip(' ').strip('\n').replace('\r', ''))
        
    def _get_code(directory, filename):
        path = os.path.join(request.folder, directory, filename)
        def _get_code_core():
            if not os.path.exists(path):
                raise HTTP(404)
            f = open(path, 'r')
            lines = f.readlines()
            f.close()
            return _to_code(lines)
        return cache.ram('code:%s/%s' % (directory, filename), _get_code_core, time_expire=10)

    plugin_name = request.controller
    
    # reload the plugin module
    local_import(plugin_name, reload=True)
    
    # load the controll (usage) code
    controller_code = _get_code('controllers', '%s.py' % plugin_name)
    
    # load the module (source) code
    module_code = _get_code('modules', '%s.py' % plugin_name)
    
    info_plugin = info_plugin_metas[plugin_name]
    response.web2py_plugins = Storage(
        plugin_name=plugin_name,
        plugin_label=info_plugin['label'],
        plugin_short_description=info_plugin['short_description'],
        plugin_long_description=info_plugin['long_description'],
        controller_code=controller_code,
        module_code=module_code,
    )
    response.view = 'web2py_plugins.html'