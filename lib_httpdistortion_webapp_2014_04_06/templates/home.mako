# -*- mode: html; coding: utf-8 -*-
<div class="select-block">
    <h1>http-distortion</h1>
    
    <p><span class="highlight-color">http-distortion</span> — утилита для
            обхода цензуры интернет-провайдеров
            (<a href="http://www.zapret-info.gov.ru/" target="_blank">www.zapret-info.gov.ru</a>).</p>
    
    <p>Скачать последнюю версию утилиты можно по ссылке: ${download_link_html}.</p>
</div>

<h2>Механизм работы</h2>

<p>Утилита http-distortion совершает две независимые манипуляции для обхода цензуры:</p>

<ol>
    <li>
        <p>DNS-запросы отправляются через HTTPS, что препятствует
                интернет-провайдерам отслеживать и подменять DNS-пакеты.</p>
    </li>
    
    <li>
        <p><span class="highlight-color">В заголовки HTTP-трафика вносятся небольшие искажения</span>.</p>
        
        <p>Эти искажения незначительны и не мешают работе web-сайтов, но сбивают с толку инструменты цензуры интернет-провайдеров.</p>
    </li>
</ol>

<p>Необходимо отметить, что интернет-провайдеры используют различные реализации инструментов цензуры. Поэтому для некоторых провайдеров утилита http-distortion работоспособна, для других — окажется бесполезной. Например, утилита окажется бесполезной для всех тех интернет-провайдеров, которые не занимаются анализом HTTP-трафика, а просто блокируют web-сайты по IP-адресу.</p>

<div class="select-block">
    <h2>Установка и использование</h2>
    
    <ol>
        <li>
            <p>У вас должен быть установлен web-браузер <span class="highlight-color">Mozilla Firefox</span>
                    (скачать: <a href="https://getfirefox.com/" target="_blank">getfirefox.com</a>). Для корректной работы утилиты,
                    после новой установки Mozilla Firefox, необходимо запустить
                    его хотя бы один раз.</p>
        </li>
        
        <li><p>Скачайте архивный файл утилиты <span class="highlight-color">http-distortion</span> (${download_link_html}) и распакуйте его в удобное для вас место.</p></li>
        
        <li><p>Удостоверьтесь, что web-браузер Mozilla Firefox на этом шаге закрыт.</p></li>
        
        <li><p>Запустите файл "<span class="highlight-color">install-and-start.cmd</span>". Выскочившее окно утилиты оставьте открытым.</p></li>
        
        <li><p>Запустите web-браузер Mozilla Firefox и наслаждайтесь интернетом без цензуры.</p></li>
    </ol>
</div>

<h2>Удаление</h2>

<p>Файл "<span class="highlight-color">uninstall.cmd</span>" удаляет все изменения, внесённые утилитой в конфигурацию web-браузера Mozilla Firefox.</p>

<p>Удостоверьтесь, что web-браузер Mozilla Firefox закрыт во время запуска "uninstall.cmd".</p>

<p>Утилита http-distortion не изменяет никаких системных файлов вашего компьютера и не вносит изменений в системный реестр.</p>

<p>Удачи!</p>
