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
<!DOCTYPE html>

<html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width" />
        
        <title>${'{} | {}'.format(title, request.environ['app.DEFAULT_TITLE']) if title != request.environ['app.DEFAULT_TITLE'] else title | h}</title>
        <meta name="description" content="${description | h}" />
        <meta name="keywords" content="${keywords | h}" />
        <meta name="google-site-verification" content="1-VScJd9SGcFeapIEuerknx_4xY-wsmfvl63i6_e_QY" />
        <meta name="yandex-verification" content="4e4739aa580c2e91" />
        <meta name="app__root" content="${request.environ['app.ROOT'] | h}" />
        <meta name="app__static_root" content="${request.environ['app.STATIC_ROOT'] | h}" />
        
        <link rel="shortcut icon" href="${request.environ['app.FAVICON'] | h}" />
        <link rel="stylesheet" media="screen" href="${request.environ['app.STATIC_ROOT'] + '/css/layout.css' | h}" />
    </head>
    <body>
        <div class="page-block">
            <header>
                <nav class="menu-block">
                    <span class="menu-item ${flag_active_menu('home') | h}">[<a href="${request.environ['app.ROOT'] + '/' | h}">http-distortion</a>]</span>
                    <span class="menu-item ${flag_active_menu('info') | h}">[<a href="${request.environ['app.ROOT'] + '/info' | h}">Дополнительная информация</a>]</span>
                    <span class="menu-item ${flag_active_menu('download') | h}">[<a href="${request.environ['app.ROOT'] + '/download' | h}">Скачать</a>]</span>
                    <span class="menu-item ${flag_active_menu('source') | h}">[<a href="${request.environ['app.ROOT'] + '/source' | h}">Исходный код</a>]</span>
                </nav>
                %if child_menu_file:
                    <%include file="${child_menu_file}" />
                %endif:
            </header>
            <main class="content-border">
                <%include file="${content_file}" />
            </main>
            <footer>
                <p>
                    Feedback: &lt;<a href="mailto:polymorphm+httpdistortion@gmail.com">polymorphm+httpdistortion@gmail.com</a>&gt;
                </p>
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
    </body>
</html>
