# -*- mode: html; coding: utf-8 -*-
<%
def flag_active_menu(check_menu_name):
    if not menu_name:
        return ''
    
    if check_menu_name == menu_name or \
            menu_name.startswith(check_menu_name + '/'):
        return 'active'
    
    return ''
%>\
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        
        <title>${title | h}</title>
        <meta name="description" content="${description | h}" />
        <meta name="keywords" content="${keywords | h}" />
        <meta name='yandex-verification' content='7d1b48eb6ab2227b' />
        <meta name="app__root" content="${request.environ['app.ROOT'] | h}" />
        <meta name="app__static_root" content="${request.environ['app.STATIC_ROOT'] | h}" />
        
        <link rel="shortcut icon" href="${request.environ['app.FAVICON'] | h}" />
        <link rel="stylesheet" media="screen" href="${request.environ['app.STATIC_ROOT'] | h}/css/default.css" />
    </head>
    <body>
        <div class="page-limit">
            <div class="page-border page-color">
                <header>
                    <div>
                        <div class="header-logo-img-block">
                            <a href="${request.environ['app.ROOT'] | h}/"><img class="header-logo-img" alt="[logo]" src="${request.environ['app.STATIC_ROOT'] | h}/img/default/header_logo.png" /></a>
                        </div>
                        <div class="header-logo-text-block">
                            <div>
                                Pnzact: Согласования и Разрешения в Пензе
                            </div>
                            <div style="display: hidden">Penzact</div>
                            <div style="display: hidden">Penzakt</div>
                            <div style="display: hidden">Пензакт</div>
                            <div class="header-logo-text-sub-text">
                                <div>Поможем решить проблемы с государством!</div>
                                <div class="highlight-color">Тел: ${tel | h}</div>
                            </div>
                        </div>
                    </div>
                    <nav class="header-border header-text">
                        <a class="header-item ${flag_active_menu('home') | h}" href="${request.environ['app.ROOT'] | h}/">О компании</a>
                        <a class="header-item ${flag_active_menu('private') | h}" href="${request.environ['app.ROOT'] | h}/private">Частным лицам</a>
                        <a class="header-item ${flag_active_menu('enterprise') | h}" href="${request.environ['app.ROOT'] | h}/enterprise">Юр лицам</a>
                        <a class="header-item ${flag_active_menu('our_clients') | h}" href="${request.environ['app.ROOT'] | h}/our-clients">Наши клиенты</a>
                        <a class="header-item ${flag_active_menu('contacts') | h}" href="${request.environ['app.ROOT'] | h}/contacts">Контакты</a>
                    </nav>
                </header>
                <main>
                    <%include file="${content_file}" />
                    <div class="clear-both"></div>
                </main>
            </div>
            <footer class="footer-border footer-text">
                <p>Copyright Pnzact Team.</p>
                <p>
                    <script>
                        //<[CDATA[
                        // LiveInternet counter
                        document.write("<a href='http://www.liveinternet.ru/click' "+
                        "target=_blank><img src='//counter.yadro.ru/hit?t45.1;r"+
                        escape(document.referrer)+((typeof(screen)=="undefined")?"":
                        ";s"+screen.width+"*"+screen.height+"*"+(screen.colorDepth?
                        screen.colorDepth:screen.pixelDepth))+";u"+escape(document.URL)+
                        ";"+Math.random()+
                        "' alt='' title='LiveInternet' "+
                        "border='0' width='31' height='31'><\/a>")
                        //]]>
                    </script>
                </p>
            </footer>
        </div>
        <script>
            //<[CDATA[
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
            
            ga('create', 'UA-42105641-1', 'pnzact.ru');
            ga('send', 'pageview');
            //]]>
        </script>
    </body>
</html>
