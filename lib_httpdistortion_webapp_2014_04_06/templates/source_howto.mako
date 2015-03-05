# -*- mode: html; coding: utf-8 -*-
<h1>${title | h}</h1>

<p>Эта инструкция главным образом предназначена для пользователей <span class="highlight-color">GNU/Linux</span> ,
        которые хотели бы собрать утилиту для собственного использования.</p>

<p>Используйте <span class="highlight-color">Git</span> чтобы получить файлы утилиты,
        по аналогии с тем, как показано в следующем примере:</p>

<pre class="code-block">$ git clone https://github.com/polymorphm/plasticine-socks-server.git

$ cd plasticine-socks-server

$ git checkout plasticine-socks-server-0.9.2</pre>

<p>Для запуска утилиты потребуется версия <span class="highlight-color">Python</span>
        не менее чем <span class="highlight-color">3.4</span> .
        Или же можно обойтись версией <span class="highlight-color">3.3</span> , но только при условии
        дополнительной установки модуля
        <span class="highlight-color">"<a href="https://pypi.python.org/pypi/asyncio" target="_blank">asyncio</a>"</span>
        (Python-3.4 уже по умолчанию содержит в себе встроенный модуль "asyncio").</p>

<p>Если запустить утилиту с ключём <span class="highlight-color">"--help"</span> , то отобразится следующая справка:</p>

<pre class="code-block">usage: plasticine-socks-server [-h] [--use-fork] [--pid-file PID-FILE-PATH]
                               CONFIG-PATH

SOCKS (SOCKS Protocol Version 5) server with support non-regular use cases via
pluggable features

positional arguments:
  CONFIG-PATH           path to config file

optional arguments:
  -h, --help            show this help message and exit
  --use-fork            use fork operation (after sockets creation)
  --pid-file PID-FILE-PATH
                        path to pid file</pre>

<p>Для выполнения наших целей -- содержимое конфигурационного файла должно указывать
        на использование "addrinfo_appspot" и "http_distortion":</p>

<pre class="code-block"># файл plasticine-socks-server.cfg

[plasticine-socks-server]

port = 1080
features = addrinfo_appspot http_distortion</pre>

Утилиту можно запускать, используя средства systemd:

<pre class="code-block">$ mkdir -p ~/.config/systemd/user

$ cp EXAMPLE.plasticine-socks-server.service ~/.config/systemd/user/http-distortion.service

$ nano ~/.config/systemd/user/http-distortion.service # прописываем путь к утилите и к её cfg-файлу

$ systemctl --user daemon-reload

$ systemctl --user start http-distortion</pre>

<h2>Настройка web-браузера Mozilla Firefox</h2>

<p>Необходимо настроить <span class="highlight-color">Mozilla Firefox</span> в режим
работы SOCKS с указанием локального компьютера (::1) в качестве адреса
и соответствующего номера порта.</p>

<p>Важной особенностью является также и настройка, отвечающая за
        использование <span class="highlight-color">DNS</span> через SOCKS .</p>

<p>Все настройки Mozilla Firefox будут выглядеть следующим образом (ввести
        их можно, например, через псевдо-URL "about:config"):</p>

<pre class="code-block">network.proxy.type                 1
network.proxy.socks                ::1
network.proxy.socks_port           1080
network.proxy.socks_remote_dns     true</pre>

<p>Внимение! Настройка "network.proxy.socks_remote_dns" может не примениться до момента перезапуска браузера.</p>

<p>Удачи!</p>
