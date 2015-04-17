// -*- mode: js; coding: utf-8 -*-

(function (global) {
    'use strict'
    
    var module = global.app__role = {
            ROLE_LIST: [
                    ['page-outer-role', 'page-limit'],
                    ['page-role', 'page-border', 'page-color'],
                    ['highlight-color-role', 'highlight-color'],
                    ['clear-both-role', 'clear-both'],
                    ['header-role', 'header-border', 'header-text'],
                    ['header-item-role', 'header-item'],
                    ['footer-role', 'footer-text'],
                    ['content-epigraph-role', 'content-epigraph'],
                    ],
            
            init_elem: function (elem) {
                var is_updated = true
                
                while (is_updated) {
                    is_updated = false
                    
                    for (var role_i = 0; role_i < module.ROLE_LIST.length; ++role_i) {
                        var role = module.ROLE_LIST[role_i]
                        var role_elem_list = elem.getElementsByClassName(role[0])
                        
                        if (!role_elem_list.length) {
                            continue
                        }
                        
                        is_updated = true
                        
                        for (var role_elem_i = 0; role_elem_i < role_elem_list.length; ++role_elem_i) {
                            var role_elem = role_elem_list[role_elem_i]
                            
                            role_elem.classList.remove(role[0])
                            
                            for (var class_i = 1; class_i < role.length; ++class_i) {
                                role_elem.classList.add(role[class_i])
                            }
                        }
                    }
                }
            },
            }
})(this)
