# -*- mode: html; coding: utf-8 -*-
<h1>${title | h}</h1>

% for content__lot_title, content__lot_amount, content__buy_url in content__lot_list:
<div class="content--lot-object"
        data-lot-title="${content__lot_title | h}"
        data-lot-amount="${content__lot_amount | h}"
        data-buy-url="${content__buy_url | h}"
        ></div>
% endfor
<script>
    //<![CDATA[
    (function (global) {
        'use strict'
        
        function init_lot_elem (lot_elem) {
            var lot_title = lot_elem.dataset.lotTitle
            var lot_amount = lot_elem.dataset.lotAmount
            var buy_url = lot_elem.dataset.buyUrl
            
            var text_elem = document.createElement('span')
            var p_elem = document.createElement('p')
            var buy_elem = document.createElement('a')
            
            text_elem.textContent = lot_title +': '+ lot_amount
            
            buy_elem.textContent = '[Купить!]'
            buy_elem.href = '#'
            
            buy_elem.addEventListener('click', function (evt) {
                evt.preventDefault()
                
                location.assign(buy_url)
            })
            
            p_elem.appendChild(text_elem)
            p_elem.appendChild(document.createTextNode(' ---------- '))
            p_elem.appendChild(buy_elem)
            
            lot_elem.innerHTML = ''
            lot_elem.appendChild(p_elem)
        }
        
        function main () {
            var lot_elem_list = document.querySelectorAll('.content--lot-object')
            
            if (!lot_elem_list.length) {
                return
            }
            
            for (var i = 0; i < lot_elem_list.length; ++i) {
                var lot_elem = lot_elem_list[i]
                
                lot_elem.classList.remove('content--lot-object')
                
                init_lot_elem(lot_elem)
            }
        }
        
        main()
    })(this)
    //]]>
</script>
