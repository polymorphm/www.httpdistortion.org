# -*- mode: html; coding: utf-8 -*-
<%
def flag_active_menu(check_menu_name):
    assert isinstance(check_menu_name, str)
    
    if not menu_name:
        return ''
    
    if check_menu_name == menu_name or \
            menu_name.startswith(check_menu_name + '/'):
        return 'active'
    
    return ''
%>\
<nav class="child-menu-block">
    <span class="menu-item ${flag_active_menu('source/overview') | h}">[<a href="${request.environ['app.ROOT'] + '/source/overview' | h}">Общая информация</a>]</span>
    <span class="menu-item ${flag_active_menu('source/howto') | h}">[<a href="${request.environ['app.ROOT'] + '/source/howto' | h}">Как собрать и запустить</a>]</span>
</nav>
