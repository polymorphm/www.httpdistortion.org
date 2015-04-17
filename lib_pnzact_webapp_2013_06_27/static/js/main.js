// -*- mode: js; coding: utf-8 -*-

(function (global) {
    'use strict'
    
    var module = global.app__main = {
            init_elem: function (elem) {
                app__role.init_elem(elem)
            },
            
            main: function () {
                module.init_elem(document)
            },
            }
    
    document.addEventListener('DOMContentLoaded', function (evt) {
        module.main()
    })
})(this)
