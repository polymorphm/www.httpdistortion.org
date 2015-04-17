# -*- mode: html; coding: utf-8 -*-
<h1>${title | h}</h1>

<p>Вы УСПЕШНО купили лот: ${content__lot_title | h}! (по цене: ${content__lot_amount | h})</p>

<p>Вот что мы знаем о вас:</p>
<pre style="overflow-x: auto">${content__paypal_res_data | h}</pre>
