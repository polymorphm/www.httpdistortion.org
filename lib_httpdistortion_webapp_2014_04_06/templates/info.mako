# -*- mode: html; coding: utf-8 -*-
<h1>${title | h}</h1>

<p>Дополнительая информация оформлена ввиде вероятных вопросов и
        соответствующих ответов на них.</p>

<h2 class="highlight-color">Какие приемущества даёт утилита http-distortion
        перед огромным количеством других способов обхода цензуры?</h2>

<p>Главное приемущество в том, что утилита http-distortion -- не перенаправляет web-трафик
        через сторонние сервера.</p>

<p>Это значит, что скорость вашего интернета зависит только от скорости вашего интернет-провайдера
        и скорости компьютера.</p>

<p>Если утилита http-distortion -- смогла успешно заработать (обойти цензуру)
        относительно вашего интернет-провайдера,
        то это как минимум добавляет для вас ещё 1 способ не быть отрезанным от мира.</p>

<h2 class="highlight-color">Что если утилита http-distortion не заработала? Сообщений с ошибками не
        появлялось, но цензура всё ещё блокирует web-сайты..</h2>

<p>Вероятнее всего это значит, что ваш случай не подходит под ситуацию, при которой
        утилита http-distortion смогла бы помочь.</p>

<p>Так как каждый интернет-провайдер использует свои механизмы блокировки -- то
        заранее вряд ли можно предсказать будет ли успех у утилиты
        относительно очередного интернет-провайдера.</p>

<p>Но расстраиваться не стоит, так как существует огромное количество других
        способов обойти цензуру ;).</p>

<h2 class="highlight-color">Почему главные файлы утилиты http-distortion --
        оформлены ввиде пакетных файлов (*.cmd), а не нормальных исполняемых файлов (*.exe)?</h2>

<p>Целью утилиты -- было предоставить хорошую и ясную работоспособность.
        а не запутать пользователя.</p>

<p>Если пользоваль является достаточно-продвинутым -- то ему будет интересно
        изучить как работает программа, и возможно внести в неё улучшения.</p>

<p>Компиляция в исполняемые файлы (*.exe) частично отпугнёт интерес пользователя
        к изучению, но при этом не даст абсолютно ни каких существенных приемуществ.</p>

<h2 class="highlight-color">Правильно ли я понимаю, что утилита http-distortion
        подготовлена только для Microsoft Windows? где версия для GNU/Linux и
        других ОС?</h2>

<p>Верно! утилита http-distortion -- это сборка для Microsoft Windows.</p>

<p>Однако разработка изначально велась для GNU/Linux (а только уже потом
        тестировалась на Microsoft Windows), и Linux-пользователям не
        составит совершенно ни какого труда запустить утилиту из файлов
        <a href="${request.environ['app.ROOT'] + '/source/howto' | h}">исходного кода</a> .</p>

<p>Что касается пользовалей Apple OS X -- то здесь ни каких тестов ни разу не проводилось.
        однако, разобравшись в <a href="${request.environ['app.ROOT'] + '/source/howto' | h}">исходниках</a>,
        вы можете попробовать стать первым тестером и сообщить о результатах ;) , или даже
        подготовить свою собственную сборку для Apple OS X.</p>

<h2 class="highlight-color">Я использую Google Chrome! Где решение для Google Chrome?</h2>

<p>Пока что реализовано решение только для Mozilla Firefox.</p>

<p>Ситуация с Google Chrome сейчас изучается, но вы можете ускорить это,
        если пришлёте технически-раскрытую идею реализации! :-)</p>

<h2 class="highlight-color">Где посмотреть список запрещённых цензурой сайтов
        zapret-info?</h2>

<p>Актуальный список находится тут:
        <a href="https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv" target="_blank">https://raw.githubusercontent.com/zapret-info/z-i/master/dump.csv</a>
        .</p>
