#!/usr/bin/env/python
#coding:utf8
#author:MagiRui

htlm = '''
<!DOCTYPE html>
<html lang="zh-CN" class=" book-new-nav">
  <head>
    <meta charset="utf-8">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">

  <meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.douban.com/book/">
  <meta name="keywords" content="豆瓣读书,新书速递,畅销书,书评,书单"/>
  <meta name="description" content="记录你读过的、想读和正在读的书，顺便打分，添加标签及个人附注，写评论。根据你的口味，推荐适合的书给你。" />
  <meta name="verify-v1" content="EYARGSAVd5U+06FeTmxO8Mj28Fc/hM/9PqMfrlMo8YA=">
  <meta property="wb:webmaster" content="7c86191e898cd20d">
  <meta property="qc:admins" content="1520412177364752166375">

    <title>
    豆瓣读书
</title>
    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico"
      type="image/x-icon">
    <script src="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js"></script>
    <script>
      var Douban = {}, Book = {}
      var Do=function(){Do.actions.push([].slice.call(arguments))};Do.ready=function(){Do.actions.push([].slice.call(arguments))},Do.add=Do.define=function(o,l){Do.mods[o]=l},Do.global=function(){Do.global.mods=Array.concat(Do.global.mods,[].slice.call(arguments))},Do.global.mods=[],Do.mods={},Do.actions=[];
    </script>


<script src="https://img3.doubanio.com/f/book/6a411a14e088636db2bc428ec7125b476791e3fd/js/book/lib/define.js"></script>
<script>
  define.ns('Book')
  define.config({
    'jquery': '$'
  , 'piwik': 'Piwik'
  , 'mod/ga': 'Book.ga'
  , 'mod/ajax': 'Book.ajax'
  , 'mod/cookie': 'Book.cookie'
  })

  Do.add('mod/cookie', {
    path: 'https://img3.doubanio.com/f/book/6542b92d560cd64f30c9248e6c35499cc11c0d29/js/book/mod/cookie.js'
  , type: 'js'
  })

  Do.add('mod/ajax', {
    path: 'https://img3.doubanio.com/f/book/b455e168dbfaa03597d2e336c3f56e32843361c9/js/book/mod/ajax.js'
  , requires: ['mod/cookie']
  , type: 'js'
  })

  Do.add('mod/ga', {
    path: 'https://img3.doubanio.com/f/book/42544a42ebd9be4aee64b3a8c6df1a15a8c8e020/js/book/mod/ga.js'
  , type: 'js'
  })
</script>


<script>!function(e){var o=function(o,n,t){var c,i,r=new Date;n=n||30,t=t||"/",r.setTime(r.getTime()+24*n*60*60*1e3),c="; expires="+r.toGMTString();for(i in o)e.cookie=i+"="+o[i]+c+"; path="+t},n=function(o){var n,t,c,i=o+"=",r=e.cookie.split(";");for(t=0,c=r.length;t<c;t++)if(n=r[t].replace(/^\s+|\s+$/g,""),0==n.indexOf(i))return n.substring(i.length,n.length).replace(/\"/g,"");return null},t=e.write,c={"douban.com":1,"douban.fm":1,"google.com":1,"google.cn":1,"googleapis.com":1,"gmaptiles.co.kr":1,"gstatic.com":1,"gstatic.cn":1,"google-analytics.com":1,"googleadservices.com":1},i=function(e,o){var n=new Image;n.onload=function(){},n.src="https://www.douban.com/j/except_report?kind=ra022&reason="+encodeURIComponent(e)+"&environment="+encodeURIComponent(o)},r=function(o){try{t.call(e,o)}catch(e){t(o)}},a=/<script.*?src\=["']?([^"'\s>]+)/gi,g=/http:\/\/(.+?)\.([^\/]+).+/i;e.writeln=e.write=function(e){var t,l=a.exec(e);return l&&(t=g.exec(l[1]))?c[t[2]]?void r(e):void("tqs"!==n("hj")&&(i(l[1],location.href),o({hj:"tqs"},1),setTimeout(function(){location.replace(location.href)},50))):void r(e)}}(document);
</script>



  <link href="https://img3.doubanio.com/f/book/e7612a013a5e76c7c680323c74748d21cd703ba0/css/book/master.css" rel="stylesheet" type="text/css">

  <link href="https://img3.doubanio.com/f/book/222a5c61e041638af8defc87cf97f4a863a77922/css/book/base/init.css" rel="stylesheet">
  <style type="text/css"></style>
  <script>var _head_start = new Date();</script>



  <script type='text/javascript'>
    var _vds = _vds || [];
    (function(){ _vds.push(['setAccountId', '22c937bbd8ebd703f2d8e9445f7dfd03']);
        _vds.push(['setCS1','user_id','0']);
            (function() {var vds = document.createElement('script');
                vds.type='text/javascript';
                vds.async = true;
                vds.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'dn-growing.qbox.me/vds.js';
                var s = document.getElementsByTagName('script')[0];
                s.parentNode.insertBefore(vds, s);
            })();
    })();
</script>


  <script type='text/javascript'>
    var _vwo_code=(function(){
      var account_id=249272,
          settings_tolerance=2000,
          library_tolerance=2500,
          use_existing_jquery=false,
          // DO NOT EDIT BELOW THIS LINE
          f=false,d=document;return{use_existing_jquery:function(){return use_existing_jquery;},library_tolerance:function(){return library_tolerance;},finish:function(){if(!f){f=true;var a=d.getElementById('_vis_opt_path_hides');if(a)a.parentNode.removeChild(a);}},finished:function(){return f;},load:function(a){var b=d.createElement('script');b.src=a;b.type='text/javascript';b.innerText;b.onerror=function(){_vwo_code.finish();};d.getElementsByTagName('head')[0].appendChild(b);},init:function(){settings_timer=setTimeout('_vwo_code.finish()',settings_tolerance);var a=d.createElement('style'),b='body{opacity:0 !important;filter:alpha(opacity=0) !important;background:none !important;}',h=d.getElementsByTagName('head')[0];a.setAttribute('id','_vis_opt_path_hides');a.setAttribute('type','text/css');if(a.styleSheet)a.styleSheet.cssText=b;else a.appendChild(d.createTextNode(b));h.appendChild(a);this.load('//dev.visualwebsiteoptimizer.com/j.php?a='+account_id+'&u='+encodeURIComponent(d.URL)+'&r='+Math.random());return settings_timer;}};}());_vwo_settings_timer=_vwo_code.init();
  </script>


  <script></script>
  <link rel="stylesheet" href="https://img3.doubanio.com/misc/mixed_static/13419eb47c7c7dd7.css">

  </head>
  <body>

  <script>var _body_start = new Date();</script>





    <link href="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">

<div class="top-nav-info">
  <a href="https://www.douban.com/accounts/login?source=book" class="nav-login" rel="nofollow">登录</a>
  <a href="https://www.douban.com/accounts/register?source=book" class="nav-register" rel="nofollow">注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>




<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="on">
      <a href="https://book.douban.com"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/group" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
    <li>
      <a href="#more" class="bn-more"><span>更多</span></a>
      <div class="more-items">
        <table cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td>
                <a href="https://ypy.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-ypy&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣摄影</a>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/984c231/shire/bundle.js" defer="defer"></script>








    <link href="//img3.doubanio.com/dae/accounts/resources/19507ad/book/bundle.css" rel="stylesheet" type="text/css">




<div id="db-nav-book" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary">
    <div class="nav-logo">
      <a href="https:&#47;&#47;book.douban.com">豆瓣读书</a>
    </div>
    <div class="nav-search">
      <form action="https:&#47;&#47;book.douban.com/subject_search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          <label for="inp-query">
          </label>
          <div class="inp"><input id="inp-query" name="search_text" size="22" maxlength="60" placeholder="书名、作者、ISBN" value=""></div>
          <div class="inp-btn"><input type="submit" value="搜索"></div>
          <input type="hidden" name="cat" value="1001" />
        </fieldset>
      </form>
    </div>
  </div>
  </div>
  <div class="nav-secondary">


<div class="nav-items">
  <ul>
    <li    ><a href="https://book.douban.com/cart/"
     >购书单</a>
    </li>
    <li    ><a href="https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban"
            target="_blank"
     >电子图书</a>
    </li>
    <li    ><a href="https://market.douban.com/book?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web"
     >豆瓣书店</a>
    </li>
    <li    ><a href="https://book.douban.com/annual/2017?source=navigation"
            target="_blank"
     >2017年度榜单</a>
    </li>
    <li    ><a href="https://book.douban.com/standbyme/2017?source=navigation"
            target="_blank"
     >2017读书报告</a>
    </li>
    <li          class=" book-cart"
    ><a href="https://market.douban.com/cart/?biz_type=book&utm_campaign=book_nav_cart&utm_source=douban&utm_medium=pc_web"
            target="_blank"
     >购物车</a>
    </li>
  </ul>
</div>

  </div>
</div>

<script id="suggResult" type="text/x-jquery-tmpl">
  <li data-link="{{= url}}">
            <a href="{{= url}}" onclick="moreurl(this, {from:'book_search_sugg', query:'{{= keyword }}', subject_id:'{{= id}}', i: '{{= index}}', type: '{{= type}}'})">
            <img src="{{= pic}}" width="40" />
            <div>
                <em>{{= title}}</em>
                {{if year}}
                    <span>{{= year}}</span>
                {{/if}}
                <p>
                {{if type == "b"}}
                    {{= author_name}}
                {{else type == "a" }}
                    {{if en_name}}
                        {{= en_name}}
                    {{/if}}
                {{/if}}
                 </p>
            </div>
        </a>
        </li>
  </script>




    <script src="//img3.doubanio.com/dae/accounts/resources/19507ad/book/bundle.js" defer="defer"></script>





  <div id="wrapper">

  <!-- douban ad begin -->
  <div id="dale_book_home_top_super_banner" class="ad-placeholder" style="margin: -18px 0 18px;">
  </div>
  <!-- douban ad end -->


  <div id="content">


    <div class="grid-16-8 clearfix">

      <div class="article">





  <div class="section books-express ">
    <div class="hd">

  <h2 class=''>
    <span class="">新书速递</span>
      <span class="link-more">
        <a class="" href="/latest?icn=index-latestbook-all"
          >更多»</a>
      </span>
  </h2>

      <div class="slide-controls">
        <ol class="slide-dots">
          <li><a data-index="1" href="#" class=""></a></li>
          <li><a data-index="2" href="#" class=""></a></li>
          <li><a data-index="3" href="#" class=""></a></li>
          <li><a data-index="4" href="#" class=""></a></li>
        </ol>
        <div class="slide-btns">
          <a href="#" class="prev">&#8249;</a>
          <a href="#" class="next">&#8250;</a>
        </div>
      </div>
    </div>
    <div class="bd">
      <div class="carousel">
        <div class="slide-list">


    <ul class="list-col list-col5 list-express slide-item">


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30270242/?icn=index-editionrecommend" title="星尘">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29850573.jpg" class=""
                  width="115px" height="172px" alt="星尘">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/>
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30270242/?icn=index-editionrecommend"
                  title="星尘">星尘</a>
              </div>
              <div class="author">
                [英] 尼尔·盖曼
              </div>
              <div class="more-meta">
                <h4 class="title">
                  星尘
                </h4>
                <p>
                  <span class="author">
                    [英] 尼尔·盖曼
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    江苏凤凰文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  “从前有个年轻人，他想追寻心之所向。”
----------------------
为了一个吻，一个牵手一生的约定，特里斯坦穿越禁忌的城墙，寻找一颗坠落的星星。
因无知而无惧，因年轻而无畏，特里斯坦走进精灵仙境，开始了一段惊险的奇幻之旅。那里有危机四伏的食人森林、风起 云涌的风暴堡、神秘邪恶的女巫、光怪陆离的魔法……他能否安然越过险境，找到心之所向？
-
这是一部弥漫着淡淡忧伤...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30314033/?icn=index-editionrecommend" title="无所畏">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29872681.jpg" class=""
                  width="115px" height="172px" alt="无所畏">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/>
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30314033/?icn=index-editionrecommend"
                  title="无所畏">无所畏</a>
              </div>
              <div class="author">
                冯唐
              </div>
              <div class="more-meta">
                <h4 class="title">
                  无所畏
                </h4>
                <p>
                  <span class="author">
                    冯唐
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">

                  冯唐全新作品，一部坦露自我的真诚之作。
全书分为如何获得成功、爱情如何对抗时间、生活怎么过才算有意义、自我价值如何体现四个部分，并收录《如何避免成为一个油腻的中年猥琐男》《找个好看的扑倒》《爱情如何对抗时间》《我爸认识所有的鱼》等知名篇目。
此书对冯唐来说，是一个新的开始，中年的冯唐在书中坦言自己的中年危机、父亲的去世、老妈的人生哲学，以及对...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/26849607/?icn=index-editionrecommend" title="黎曼猜想漫谈">
                <img src="https://img3.doubanio.com/view/subject/m/public/s28950702.jpg" class=""
                  width="115px" height="172px" alt="黎曼猜想漫谈">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/>
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/26849607/?icn=index-editionrecommend"
                  title="黎曼猜想漫谈">黎曼猜想漫谈</a>
              </div>
              <div class="author">
                卢昌海
              </div>
              <div class="more-meta">
                <h4 class="title">
                  黎曼猜想漫谈
                </h4>
                <p>
                  <span class="author">
                    卢昌海
                  </span>
                  /
                  <span class="year">
                    2016-8-20
                  </span>
                  /
                  <span class="publisher">
                    清华大学出版社
                  </span>
                </p>
                <p class="abstract">

                  史上zui富有创造性的数学家——黎曼。
他奉行恩师高斯的座右铭，宁肯少些，但要成熟。
黎曼生前只发表10篇论文，却是很多领域的开拓者。
他提出的黎曼猜想是数学史上的不朽谜语，被公认为是zui伟大的数学猜想。
作者以非常明晰的数学阐释文字与优雅、生动、有趣的传记和历史篇章交替出现，对一个史诗般的数学之谜作了迷人而流畅的叙述，而这个谜还将继续挑战和刺激着世人...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30325282/?icn=index-editionrecommend" title="什么都能拿来画">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29868740.jpg" class=""
                  width="115px" height="172px" alt="什么都能拿来画">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/>
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30325282/?icn=index-editionrecommend"
                  title="什么都能拿来画">什么都能拿来画</a>
              </div>
              <div class="author">
                罗罗布
              </div>
              <div class="more-meta">
                <h4 class="title">
                  什么都能拿来画
                </h4>
                <p>
                  <span class="author">
                    罗罗布
                  </span>
                  /
                  <span class="year">
                    2018-8-1
                  </span>
                  /
                  <span class="publisher">
                    电子工业出版社
                  </span>
                </p>
                <p class="abstract">

                  《什么都能拿来画：罗罗布的创意简笔画》是一本创意简笔画教程，案例步骤详尽，涵盖生活中的方方面面。知名卡通IP 罗罗布用简单、好玩的方式，带你玩转一整年的画画游戏，希望你能从中体会到画画的乐趣。快跟它一起拿起画笔，看看身边有什么常见的东西可以拿来画画，期待你发现它们的新玩法！
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30143261/?icn=index-editionrecommend" title="货币战争">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29840304.jpg" class=""
                  width="115px" height="172px" alt="货币战争">
              </a>
            </div>
                <div class="intervenor-info">
                    <img src="https://img3.doubanio.com/f/book/ef040178fab1770d60e3f2f12ba4c7aa70714396/pics/book/partner/jd_recommend.png" class='jd-icon' width="16" height="16"/>
                    <span>推荐</span>
                </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30143261/?icn=index-editionrecommend"
                  title="货币战争">货币战争</a>
              </div>
              <div class="author">
                [美]詹姆斯·里卡兹&nbsp;/&nbsp;James Rickards
              </div>
              <div class="more-meta">
                <h4 class="title">
                  货币战争
                </h4>
                <p>
                  <span class="author">
                    [美]詹姆斯·里卡兹&nbsp;/&nbsp;James Rickards
                  </span>
                  /
                  <span class="year">
                    2018-7
                  </span>
                  /
                  <span class="publisher">
                    上海译文出版社
                  </span>
                </p>
                <p class="abstract">

                  1971年8月15日，一个安静的星期日晚上，理查德•尼克松总统发表广播演说，宣布他的新经济政策。政府将实施全国性的价格管制，对国外进口商品征收高额附加税，并禁止用美元兑换黄金。由于一场正在进行的货币战争摧毁了人们对美元的信任，美国正处于危机之中。
一次又一次，纸币贬值，资产冻结，黄金被没收，资本被管制。对此，美国也无法独善其身。事实上，从1770年...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30244560/?icn=index-latestbook-subject" title="海街日记（全7册）">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29872105.jpg" class=""
                  width="115px" height="172px" alt="海街日记（全7册）">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30244560/?icn=index-latestbook-subject"
                  title="海街日记（全7册）">海街日记（全7册）</a>
              </div>
              <div class="author">
                [日]吉田秋生
              </div>
              <div class="more-meta">
                <h4 class="title">
                  海街日记（全7册）
                </h4>
                <p>
                  <span class="author">
                    [日]吉田秋生
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    雅众文化/浙江文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  ◆家人就是温暖存在的理由！
◆荣获 第6届日本漫画大奖
第11届文化厅媒体艺术祭漫画部门优秀奖
第61届小学馆漫画奖
◆2018年戛纳金棕榈奖得主日本导演是枝裕和暖心治愈代表作《海街日记》原作 ◆长泽雅美、绫濑遥、夏帆、广濑丝丝四大女神联袂出演
◆总销量突破350万册 日本小学馆首次官方授权简体版
◆以鎌仓为舞台，吉田秋生用哀伤而温柔的笔触描绘了家人间的羁绊
◆《海...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30223198/?icn=index-latestbook-subject" title="毕加索画传1">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29790620.jpg" class=""
                  width="115px" height="172px" alt="毕加索画传1">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30223198/?icn=index-latestbook-subject"
                  title="毕加索画传1">毕加索画传1</a>
              </div>
              <div class="author">
                [法] 朱莉·比尔曼 编&nbsp;/&nbsp;[法] 克莱芒·乌布雷 绘
              </div>
              <div class="more-meta">
                <h4 class="title">
                  毕加索画传1
                </h4>
                <p>
                  <span class="author">
                    [法] 朱莉·比尔曼 编&nbsp;/&nbsp;[法] 克莱芒·乌布雷 绘
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    后浪丨湖南美术出版社
                  </span>
                </p>
                <p class="abstract">

                  毕加索情人的口述史
一位青年艺术家的肖像
◎ 编辑推荐
☆ 毕加索是怎样炼成的？
毕加索情人的口述史，一部别样的美术史，贯穿艺术家的“玫瑰时期”
一个天才的成长有时好比一名君王抵达权力中心的过程：至高的美和力量背后，是无数人的牺牲、包 容和付出。这部画传以费尔南德·奥利维耶的视角，为我们讲述一个私密、任性、才华横溢的年轻毕加索。
☆ 费尔南德·奥利维耶被嫌...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27190983/?icn=index-latestbook-subject" title="耶路撒冷，一个女人">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29786830.jpg" class=""
                  width="115px" height="172px" alt="耶路撒冷，一个女人">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27190983/?icn=index-latestbook-subject"
                  title="耶路撒冷，一个女人">耶路撒冷，一个女人</a>
              </div>
              <div class="author">
                [以]亚伯拉罕·耶霍舒亚
              </div>
              <div class="more-meta">
                <h4 class="title">
                  耶路撒冷，一个女人
                </h4>
                <p>
                  <span class="author">
                    [以]亚伯拉罕·耶霍舒亚
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract">

                  《耶路撒冷，一个女人》出版于2004年，入围2005年布克国际文学奖短名单，荣获2006年《洛杉矶时报》图书奖，并于2010年由以色列著名导演伊安•瑞克利斯改编成电影《人力资源经理》。
这是一次古怪的“英雄救美”。“美人”在故事的开头就死于耶路撒冷集市上发生的一起爆炸事件，身份不明，只有一张工资单暗示她曾是某大型面包店的夜间清洁工。于是，迅速有记者撰文,...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30258604/?icn=index-latestbook-subject" title="八月炮火">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29845460.jpg" class=""
                  width="115px" height="172px" alt="八月炮火">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30258604/?icn=index-latestbook-subject"
                  title="八月炮火">八月炮火</a>
              </div>
              <div class="author">
                [美] 巴巴拉·塔奇曼
              </div>
              <div class="more-meta">
                <h4 class="title">
                  八月炮火
                </h4>
                <p>
                  <span class="author">
                    [美] 巴巴拉·塔奇曼
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    理想国 | 上海三联书店
                  </span>
                </p>
                <p class="abstract">

                  精彩无比的一战经典之作，普利策奖委员会也为之“绕道”颁奖。
作者巴巴拉·塔奇曼被誉为“历史学者中的艺术家”，她的写作，令人沉浸、着迷。
是什么让世界踏进这场“不可能”发生的战争？肯尼迪总统从中汲取历史教训化解美苏危机。
【编辑推荐】
★ 普利策奖获奖经典作品，以精彩笔法展现帝国时代的终结战“一战”是如何开启并迅速陷入僵局，叩问是什么让帝王、政客和...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30257649/?icn=index-latestbook-subject" title="田园的忧郁">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29861372.jpg" class=""
                  width="115px" height="172px" alt="田园的忧郁">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30257649/?icn=index-latestbook-subject"
                  title="田园的忧郁">田园的忧郁</a>
              </div>
              <div class="author">
                [日] 佐藤春夫
              </div>
              <div class="more-meta">
                <h4 class="title">
                  田园的忧郁
                </h4>
                <p>
                  <span class="author">
                    [日] 佐藤春夫
                  </span>
                  /
                  <span class="year">
                    2018-9-1
                  </span>
                  /
                  <span class="publisher">
                    雅众文化/陕西师范大学出版总社
                  </span>
                </p>
                <p class="abstract">

                  芥川龙之介 太宰治 三岛由纪夫等的文学偶像
日本唯美派大师 佐藤春夫经典代表作
野间文艺翻译奖得主 岳远坤 倾情献译
【内容简介】
为躲避都市的喧嚣，青年携妻子和狗来到荒草茂盛的武藏野闲散安身。然而退居荒僻之地后，焦虑和幻觉却常常向他袭来……作品以诗一般的笔触展现了武藏野的四季变换， 深刻表达了都市青年面对青春的忧郁、苦闷与彷徨，充满了世纪末的颓废气息和...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30322552/?icn=index-latestbook-subject" title="荆楚岁时记">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29865959.jpg" class=""
                  width="115px" height="172px" alt="荆楚岁时记">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30322552/?icn=index-latestbook-subject"
                  title="荆楚岁时记">荆楚岁时记</a>
              </div>
              <div class="author">
                [梁]宗懔 撰&nbsp;/&nbsp;[隋]杜公瞻 注&nbsp;/&nbsp;姜彦稚 辑校
              </div>
              <div class="more-meta">
                <h4 class="title">
                  荆楚岁时记
                </h4>
                <p>
                  <span class="author">
                    [梁]宗懔 撰&nbsp;/&nbsp;[隋]杜公瞻 注&nbsp;/&nbsp;姜彦稚 辑校
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    中华书局
                  </span>
                </p>
                <p class="abstract">

                  《荆楚岁时记》，记录中国古代楚地（以江汉为中心的地区）时俗风物故事的笔记体文集，由南北朝梁宗懔(约501～565)撰。全书凡37篇，记载了自元旦至除夕的24节令和时俗。有注，传为隋代杜公瞻作。注中引用经典俗传计68部80余条，说明某一风俗的源流承绪，偶尔也记载北方的节令时俗。 本书以《广汉魏丛书》为底本，参考明陈继儒《广秘笈》本等十种刊本，以及三十四种...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30303886/?icn=index-latestbook-subject" title="港岛之恋">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29849369.jpg" class=""
                  width="115px" height="172px" alt="港岛之恋">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30303886/?icn=index-latestbook-subject"
                  title="港岛之恋">港岛之恋</a>
              </div>
              <div class="author">
                刘玥
              </div>
              <div class="more-meta">
                <h4 class="title">
                  港岛之恋
                </h4>
                <p>
                  <span class="author">
                    刘玥
                  </span>
                  /
                  <span class="year">
                    2018-9-1
                  </span>
                  /
                  <span class="publisher">
                    江苏文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  所有青春的疯狂与妥协， 都是为了有一天能与你相遇， 并且一见钟情
豆瓣阅读超人气作者刘玥，专为女孩写女孩故事的人，作品点击量过千万
十个故事，关于爱情里那些完美或遗憾
只要勇敢向前，就会看见光亮
------------------------------------------
【编辑推荐】
*豆瓣阅读明星作者、坐拥千万点击量，曾获得第九届新概念作文大 赛一等奖，多次获得豆瓣阅读征文大赛奖项；
*作者多年留...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30302126/?icn=index-latestbook-subject" title="巴西：未来之国">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29862877.jpg" class=""
                  width="115px" height="172px" alt="巴西：未来之国">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30302126/?icn=index-latestbook-subject"
                  title="巴西：未来之国">巴西：未来之国</a>
              </div>
              <div class="author">
                [奥地利] 斯蒂芬·茨威格&nbsp;/&nbsp;Stefan Zweig
              </div>
              <div class="more-meta">
                <h4 class="title">
                  巴西：未来之国
                </h4>
                <p>
                  <span class="author">
                    [奥地利] 斯蒂芬·茨威格&nbsp;/&nbsp;Stefan Zweig
                  </span>
                  /
                  <span class="year">
                    2018-10
                  </span>
                  /
                  <span class="publisher">
                    后浪丨四川文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  他在流亡之地见到了未来与希望
告别《昨日的世界》，茨威格发现了他的乌托邦与理想国
一代德语文学巨匠的巴西传奇
寄托着一个理想主义者绝望前的天真与热忱
◎ 编辑推荐
☆ 茨威格选择了巴西这个“未来之国”，作为自己人生的终点站
“我对这个国家的热爱与日俱增，在与我操同一种语言的世 界沉沦以及我的精神故乡欧洲自我毁灭之后，除了这里，我不愿在任何地方重新立身。”...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30247517/?icn=index-latestbook-subject" title="镖人">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29835816.jpg" class=""
                  width="115px" height="172px" alt="镖人">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30247517/?icn=index-latestbook-subject"
                  title="镖人">镖人</a>
              </div>
              <div class="author">
                许先哲
              </div>
              <div class="more-meta">
                <h4 class="title">
                  镖人
                </h4>
                <p>
                  <span class="author">
                    许先哲
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">

                  ◆轰动日本的中国漫画！3次登上日本央视NHK电视台新闻报道节目，被日本媒体誉为“世界级水平的中国动漫精品”！
◆征服日本资深漫画编辑！双叶社（代表作《蜡笔小新》）前主编栗原一二亲笔作序！小学馆（代表作《名侦探柯南》）前主编御木基宏连连称赞！
◆漫画大师高桥留美子（代表作《犬夜叉》）、藤泽亨（代表作《麻辣教师GTO》），著名作家马伯庸，《大圣归来》...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27112575/?icn=index-latestbook-subject" title="给青年作家的信">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29815368.jpg" class=""
                  width="115px" height="172px" alt="给青年作家的信">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27112575/?icn=index-latestbook-subject"
                  title="给青年作家的信">给青年作家的信</a>
              </div>
              <div class="author">
                (爱尔兰) 科伦·麦凯恩
              </div>
              <div class="more-meta">
                <h4 class="title">
                  给青年作家的信
                </h4>
                <p>
                  <span class="author">
                    (爱尔兰) 科伦·麦凯恩
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    人民文学出版社
                  </span>
                </p>
                <p class="abstract">

                  作家 陶立夏 倾情翻译
美国国家图书奖得主   《转吧，这伟大的世界》作者
科伦·麦凯恩 Colum McCann
分享写作的孤独、光荣、禁忌、伟大
对于既是火花四射的指引，更是冲锋的号角
——————
本书是美国国家图书奖得主科伦·麦凯恩探讨写作和人生的散文集。在这本睿智、凝练、迷人、充满幽默感的书信集中，麦凯恩征引自己多年的写作和教学经验，从写作技巧、写作习惯、写...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/28355578/?icn=index-latestbook-subject" title="ab珊瑚">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29850668.jpg" class=""
                  width="115px" height="172px" alt="ab珊瑚">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/28355578/?icn=index-latestbook-subject"
                  title="ab珊瑚">ab珊瑚</a>
              </div>
              <div class="author">
                [日] 黑田夏子
              </div>
              <div class="more-meta">
                <h4 class="title">
                  ab珊瑚
                </h4>
                <p>
                  <span class="author">
                    [日] 黑田夏子
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    上海译文出版社
                  </span>
                </p>
                <p class="abstract">

                  日本第148届芥川龙之介文学奖获奖作品
第24届早稻田文学新人奖
芥川龙之介文学奖史上最年长获奖者
独特文体创造出的剔透幽深世界！
《ab珊瑚》是2013年芥川奖获奖作品。收录了获芥川奖之作《ab珊瑚》及三个短篇小说《球》《民惠的花》《彩虹》。
《ab珊瑚》是孩童时期的记忆片断，将六岁时的故事从十年后的视角以及四十年后的视角重新进行审视，带给人一种独特的时间感...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30297754/?icn=index-latestbook-subject" title="妈妈和我">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29871843.jpg" class=""
                  width="115px" height="172px" alt="妈妈和我">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30297754/?icn=index-latestbook-subject"
                  title="妈妈和我">妈妈和我</a>
              </div>
              <div class="author">
                中川碧&nbsp;/&nbsp;村松江梨子
              </div>
              <div class="more-meta">
                <h4 class="title">
                  妈妈和我
                </h4>
                <p>
                  <span class="author">
                    中川碧&nbsp;/&nbsp;村松江梨子
                  </span>
                  /
                  <span class="year">
                    2018-8-15
                  </span>
                  /
                  <span class="publisher">
                    全本书店|北京联合出版公司
                  </span>
                </p>
                <p class="abstract">

                  村松江梨子和中川碧是日本的两位绘本作者，她们在很年轻的时候成立了一个K.m.p.绘本组合，共同创作了这本书。
绘本并没有明显和完整的故事情节，只是以简单的线条、稚拙而不乏幽默的笔触描绘了幼年依赖于妈妈生活时的诸多平淡小事，充满了色声香味触的温馨细节。正是这些细节构成了每 个人对生活和世界的基本感知，很容易击中内心深处的记忆，让人瞬间回到从前。
这样...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30262578/?icn=index-latestbook-subject" title="阿波罗23号">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29815628.jpg" class=""
                  width="115px" height="172px" alt="阿波罗23号">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30262578/?icn=index-latestbook-subject"
                  title="阿波罗23号">阿波罗23号</a>
              </div>
              <div class="author">
                [英] 贾斯廷·理查兹
              </div>
              <div class="more-meta">
                <h4 class="title">
                  阿波罗23号
                </h4>
                <p>
                  <span class="author">
                    [英] 贾斯廷·理查兹
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">

                  月球行走的宇航员，凭空现身于商业中心；
悠闲遛狗的妙龄女子，却在真空死于非命。
月球暗面的军事基地，到底藏着怎样不可告人的秘密？
随着博士和艾米踏上月球，更多的谜团接踵而至：
月球基地和得克萨斯荒漠为何仅仅只有一步之遥？
运行多年的尖端系统为何忽然崩溃？
艾米为何会站在博士的对立面？！
那直视博士的冰冷灰眸，正将人类死死拖向深渊……
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30258599/?icn=index-latestbook-subject" title="肥瘦对写">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29845407.jpg" class=""
                  width="115px" height="172px" alt="肥瘦对写">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30258599/?icn=index-latestbook-subject"
                  title="肥瘦对写">肥瘦对写</a>
              </div>
              <div class="author">
                骆以军&nbsp;/&nbsp;董启章
              </div>
              <div class="more-meta">
                <h4 class="title">
                  肥瘦对写
                </h4>
                <p>
                  <span class="author">
                    骆以军&nbsp;/&nbsp;董启章
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    广西师范大学出版社
                  </span>
                </p>
                <p class="abstract">

                  【作品看点】
1、“废柴”书写者骆以军vs.文字魔术师董启章，26封无话不谈的文学书信，直捣小说家的练功房！两位来自台湾和香港的华语中生代小说家，一肥一瘦，同年出生，地域文化、性格脑洞和创作风格截然不同，他们轮替设题对谈写信，不同次元的文学宇宙激烈碰撞，会擦出怎样的火花？
2、一堂青年写作者的小说课，天马行空的文学主题。这些书信的内容从“人渣作家”...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30262087/?icn=index-latestbook-subject" title="云是黑色的">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29807219.jpg" class=""
                  width="115px" height="172px" alt="云是黑色的">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30262087/?icn=index-latestbook-subject"
                  title="云是黑色的">云是黑色的</a>
              </div>
              <div class="author">
                刘梓洁
              </div>
              <div class="more-meta">
                <h4 class="title">
                  云是黑色的
                </h4>
                <p>
                  <span class="author">
                    刘梓洁
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    世纪文景 | 上海人民出版社
                  </span>
                </p>
                <p class="abstract">

                  ☆蝉联诚品书店八周畅销NO.1的《父后七日》作者、金马奖编剧、台湾新生代人气作家的连作短篇，展现都市爱情的不同形态与残酷真相。
☆洞悉爱情角力的荒谬与精彩、冷酷与温柔的短篇小说集。
☆如果是命中注定，应该不会那么难遇见，遇见之后，也不应该有那么多困难。
-------------------
天空是白色的，但云是黑色的。七篇各自独立，却又隐秘相连的短篇，传递着都市爱情中至深...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30288066/?icn=index-latestbook-subject" title="宋宴">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29833180.jpg" class=""
                  width="115px" height="172px" alt="宋宴">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30288066/?icn=index-latestbook-subject"
                  title="宋宴">宋宴</a>
              </div>
              <div class="author">
                徐鲤&nbsp;/&nbsp;郑亚胜&nbsp;/&nbsp;卢冉
              </div>
              <div class="more-meta">
                <h4 class="title">
                  宋宴
                </h4>
                <p>
                  <span class="author">
                    徐鲤&nbsp;/&nbsp;郑亚胜&nbsp;/&nbsp;卢冉
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">

                  蒸羊煮鱼、素食仿菜、粥面汤羹、糕饼蜜饯，从宫廷飨宴、文人茶会，到平民餐饭
——七十佳肴，回味两宋风流。
春之清爽，夏之圆熟，秋之鲜香，冬之醇厚——四时为限，不时不食。
节庆时俗，风物掌故，诗词名画——信笔游宋，无知无味。
脱始于《山家清供》《中馈录》等宋元食谱，以今日食材，还原古法美味。
共赴一席宋人飨宴。
————————
或许你从未见过如此“丰盛”...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30206366/?icn=index-latestbook-subject" title="日本合众国">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29861569.jpg" class=""
                  width="115px" height="172px" alt="日本合众国">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30206366/?icn=index-latestbook-subject"
                  title="日本合众国">日本合众国</a>
              </div>
              <div class="author">
                [美]彼得·特莱亚斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  日本合众国
                </h4>
                <p>
                  <span class="author">
                    [美]彼得·特莱亚斯
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">

                  一本作的故事背景沿用科幻大师菲利普•K.迪克在经典或然历史小说《高堡奇人》中的设定。
一九四八年，轴心国在第二次世界大战中获胜，日本与德国瓜分了北美，西海岸改称“大日本合众国”。
四十年后，一款非法电子游戏《美利坚合众国》在北美大肆传播。游戏要求玩家想象如果当年盟军战胜，世界会变成什么样。
审查官石村与特高课秘密警察月野受命彻查抵抗组织“乔治•华...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30262912/?icn=index-latestbook-subject" title="如果你住在这里">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29820375.jpg" class=""
                  width="115px" height="172px" alt="如果你住在这里">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30262912/?icn=index-latestbook-subject"
                  title="如果你住在这里">如果你住在这里</a>
              </div>
              <div class="author">
                [美] 吉尔斯·拉沃什
              </div>
              <div class="more-meta">
                <h4 class="title">
                  如果你住在这里
                </h4>
                <p>
                  <span class="author">
                    [美] 吉尔斯·拉沃什
                  </span>
                  /
                  <span class="year">
                    2018-10
                  </span>
                  /
                  <span class="publisher">
                    后浪丨花山文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  “堪称艺术品”的儿童建筑科普绘本
每翻开一页，都是一个新的世界
精妙恢弘的浮雕剪纸拼贴画，带你走进世界各地的房子，探索它们的生活和秘密。
◎ 编辑推荐
☆ “堪称艺术品”的科普绘本，以精妙恢弘的手工拼贴画展现细节丰富、宏伟壮观的浮雕建筑。
☆ 翻开这本书，走进16栋世界各地的奇妙房子，聆听每栋房子的秘密，想象你会经历的生活：和松鼠做邻居，划船去上学，在房...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30278164/?icn=index-latestbook-subject" title="永久的托词">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29855609.jpg" class=""
                  width="115px" height="172px" alt="永久的托词">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30278164/?icn=index-latestbook-subject"
                  title="永久的托词">永久的托词</a>
              </div>
              <div class="author">
                [日] 西川美和
              </div>
              <div class="more-meta">
                <h4 class="title">
                  永久的托词
                </h4>
                <p>
                  <span class="author">
                    [日] 西川美和
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    北京十月文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  《永久的托词》是日本电影蓝丝带奖导演奖、横滨电影节导演奖、日本电影学院奖编剧奖得主——西川美和的长篇小说代表作，入围直木奖、日本书店大奖、山本周五郎奖。
★妻子死了，他却一滴眼泪也流不出来。但就连像他那样差劲的人，居然也能拯救某个人吗？
津村启的妻子突遭车祸身亡，对妻子已没什么感情的他，对外不得不佯装悲伤。
机缘巧合下，津村 启结识了在同一场事...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30219710/?icn=index-latestbook-subject" title="日本设计六十年:1950—2010">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29845337.jpg" class=""
                  width="115px" height="172px" alt="日本设计六十年:1950—2010">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30219710/?icn=index-latestbook-subject"
                  title="日本设计六十年:1950—2010">日本设计六十年:1950—2010</a>
              </div>
              <div class="author">
                [日]内田繁
              </div>
              <div class="more-meta">
                <h4 class="title">
                  日本设计六十年:1950—2010
                </h4>
                <p>
                  <span class="author">
                    [日]内田繁
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    中信出版集团/楚尘文化
                  </span>
                </p>
                <p class="abstract">

                  首部日本设计史权威著作
日本设计大师内田繁以亲历者身份，梳理日本战后六十年的设计潮流变迁
揭秘日本设计的意义及其秘密
◆日本设计大师内田繁以亲历者身份写就的日本设计全书。
内田繁，出生于1943年，作为日本乃至世界一流设计师，几乎参与、见证了六十年来日本设计的全部进程，可谓一个日本设计六十年的活化石。他以亲历者和设计师的身份、从切身体验出发的写作，...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30210713/?icn=index-latestbook-subject" title="黑发女大学生之死">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29879144.jpg" class=""
                  width="115px" height="172px" alt="黑发女大学生之死">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30210713/?icn=index-latestbook-subject"
                  title="黑发女大学生之死">黑发女大学生之死</a>
              </div>
              <div class="author">
                [美]罗伯特·斯通
              </div>
              <div class="more-meta">
                <h4 class="title">
                  黑发女大学生之死
                </h4>
                <p>
                  <span class="author">
                    [美]罗伯特·斯通
                  </span>
                  /
                  <span class="year">
                    2018-8-1
                  </span>
                  /
                  <span class="publisher">
                    上海文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  《黑发女大学生之死》是美国当代小说大师、美国国家图书奖得主罗伯特·斯通的绝唱之作，文字如石碑般隽永，如宝石般精密，借由一场悲剧去想象人类恶行，揭开笼罩美利坚的神秘黑雾，拷问人类阴暗的裂隙。
女大学生茉德·史塔克，身材高挑，艳丽动人，聪明伶俐，出身爱尔兰天主教家庭，却大胆在当地报纸发文，抨击“反堕胎”游行示威者，由此引起当地大学城保守群众的强...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30276702/?icn=index-latestbook-subject" title="中央帝国的哲学密码">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29879307.jpg" class=""
                  width="115px" height="172px" alt="中央帝国的哲学密码">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30276702/?icn=index-latestbook-subject"
                  title="中央帝国的哲学密码">中央帝国的哲学密码</a>
              </div>
              <div class="author">
                郭建龙
              </div>
              <div class="more-meta">
                <h4 class="title">
                  中央帝国的哲学密码
                </h4>
                <p>
                  <span class="author">
                    郭建龙
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    鹭江出版社
                  </span>
                </p>
                <p class="abstract">

                  《中央帝国的财政密码》作者重磅新作。
读懂了中央帝国的统治哲学，就把握了中央帝国统治的思想根基。
葛剑雄，林达，余世存，张鸣，马勇，张广天，周濂，刘苏里，俞敏洪，李鸿谷，陈志武，骆玉明，李淼 ，郑培凯盛赞推荐。
本书以中国封建哲学为经，以现代政治理论为纬，上至秦汉，下 至晚晴，划分神学谶纬期 、玄学自然期、三教开放期、经世致用期、道学封闭期、实学兴...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30289219/?icn=index-latestbook-subject" title="探险家公会">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29857393.jpg" class=""
                  width="115px" height="172px" alt="探险家公会">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30289219/?icn=index-latestbook-subject"
                  title="探险家公会">探险家公会</a>
              </div>
              <div class="author">
                [美]凯文•科斯特纳（Kevin Costner）,[英]乔恩•贝尔德（Jon Baird）, [美]瑞克•罗斯（Rick Ross）
              </div>
              <div class="more-meta">
                <h4 class="title">
                  探险家公会
                </h4>
                <p>
                  <span class="author">
                    [美]凯文•科斯特纳（Kevin Costner）,[英]乔恩•贝尔德（Jon Baird）, [美]瑞克•罗斯（Rick Ross）
                  </span>
                  /
                  <span class="year">
                    2018-9-1
                  </span>
                  /
                  <span class="publisher">
                    未读·文艺家·北京联合出版公司
                  </span>
                </p>
                <p class="abstract">

                  ★好莱坞硬汉影星凯文•科斯特纳首次跨界创作冒险图像小说。
★三人创作团队九年构思，精心打造迷宫般的故事线。
★故事烧脑，情怀爆表，开卷重回探险黄金时代。
★从创作之初到成书装帧无不体现匠心：
全书近七百幅漫画均为手工勾勒墨线；
坚持使用与故事背景同时期的蘸水笔；
诚意致敬二十世纪早期冒险漫画作家。
★图文并茂，全彩印刷；双封烫金，装帧复古。
★随书赠送藏...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/26704758/?icn=index-latestbook-subject" title="冻结时期的诗篇">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29856187.jpg" class=""
                  width="115px" height="172px" alt="冻结时期的诗篇">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/26704758/?icn=index-latestbook-subject"
                  title="冻结时期的诗篇">冻结时期的诗篇</a>
              </div>
              <div class="author">
                [波兰] 切斯瓦夫·米沃什
              </div>
              <div class="more-meta">
                <h4 class="title">
                  冻结时期的诗篇
                </h4>
                <p>
                  <span class="author">
                    [波兰] 切斯瓦夫·米沃什
                  </span>
                  /
                  <span class="year">
                    2018-9-1
                  </span>
                  /
                  <span class="publisher">
                    上海译文出版社
                  </span>
                </p>
                <p class="abstract">

                  ★波兰文学专家译介，中文世界首次完整呈现米沃什诗歌全貌
★二十世纪伟大的波兰诗人、诺贝尔文学奖得主
★70载创作，335首诗歌
★诗的见证，比新闻更可靠
切斯瓦夫•米沃什，二十世纪最伟大的诗人之一，以其无可匹敌的精确与优雅，定义了他所属时代的悲剧与美。他的诗歌，无论是描 述他在波兰度过的少年时代、战乱中华沙的悲痛或对信仰的追寻，都令人啧啧称奇、惊叹不...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30210687/?icn=index-latestbook-subject" title="困难的爱">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29863484.jpg" class=""
                  width="115px" height="172px" alt="困难的爱">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30210687/?icn=index-latestbook-subject"
                  title="困难的爱">困难的爱</a>
              </div>
              <div class="author">
                [意] 伊塔洛·卡尔维诺
              </div>
              <div class="more-meta">
                <h4 class="title">
                  困难的爱
                </h4>
                <p>
                  <span class="author">
                    [意] 伊塔洛·卡尔维诺
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    译林出版社
                  </span>
                </p>
                <p class="abstract">

                  一份困难的爱，一种困难的生活。
卡尔维诺以“爱”和“人生”的困难为主线，轻盈地捕捉普通人的生活影像：为会心上人在二等车厢局促一夜的困难；一夜风流后无从炫耀艳遇的困难；迫于生计日夜错肩的夫妇的困难；戴上眼镜发现新世界却因视线太清晰而看不清的困难；生活在烟云笼罩、净化无望的城市的困难……这些困难构成了人类生命的常数，勾连起对现世的沉思轨迹，以及...
                </p>
              </div>
            </div>
          </li>
    </ul>
    <ul class="list-col list-col5 list-express slide-item">


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30126850/?icn=index-latestbook-subject" title="最后的对话 Ⅱ">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29807355.jpg" class=""
                  width="115px" height="172px" alt="最后的对话 Ⅱ">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30126850/?icn=index-latestbook-subject"
                  title="最后的对话 Ⅱ">最后的对话 Ⅱ</a>
              </div>
              <div class="author">
                [阿根廷] 豪尔赫·路易斯·博尔赫斯&nbsp;/&nbsp;[阿根廷] 奥斯瓦尔多·费拉里
              </div>
              <div class="more-meta">
                <h4 class="title">
                  最后的对话 Ⅱ
                </h4>
                <p>
                  <span class="author">
                    [阿根廷] 豪尔赫·路易斯·博尔赫斯&nbsp;/&nbsp;[阿根廷] 奥斯瓦尔多·费拉里
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    新星出版社
                  </span>
                </p>
                <p class="abstract">

                  本书是拉美文坛泰斗博尔赫斯生前最后的、也是最大规模的对谈录，对话者是同为拉美文学名家的费拉里。118篇涉及不同话题的平等对谈，秒杀市面上所有单调、短小的博尔赫斯“采访稿”。
对话集是了解一位哲学家、作家思想最直白、最坦荡的方式。在博尔赫斯生前的最后三年，阿根廷国立电台敏锐地发现了这一要义。他们策划了一档连续时间长达三年的对话节目，不同于以往流...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/27169753/?icn=index-latestbook-subject" title="隐剑秋风抄">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29831808.jpg" class=""
                  width="115px" height="172px" alt="隐剑秋风抄">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/27169753/?icn=index-latestbook-subject"
                  title="隐剑秋风抄">隐剑秋风抄</a>
              </div>
              <div class="author">
                [日] 藤泽周平
              </div>
              <div class="more-meta">
                <h4 class="title">
                  隐剑秋风抄
                </h4>
                <p>
                  <span class="author">
                    [日] 藤泽周平
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    译林出版社
                  </span>
                </p>
                <p class="abstract">

                  ◆ 时代小说泰斗，作品销量超两千三百万册。文字如美玉无瑕，多篇入选日本中学课本。
◆ 村上春树痴迷的日本战后首席小说家，少数值得翻译其全集的作家之一，华语圈首度大规模译介。
◆ 电影大师山田洋次三度改编揽获数十项大奖。木村拓哉、松隆子、真田广之、宫泽理惠都曾是藤泽笔下的江湖儿女。
◆ 侯孝贤推荐给张震、舒淇的必读书；宫部美雪、井上厦等人撰文盛赞，文艺...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30194504/?icn=index-latestbook-subject" title="小银和我">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29873493.jpg" class=""
                  width="115px" height="172px" alt="小银和我">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30194504/?icn=index-latestbook-subject"
                  title="小银和我">小银和我</a>
              </div>
              <div class="author">
                [西]胡安·拉蒙·希梅内斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  小银和我
                </h4>
                <p>
                  <span class="author">
                    [西]胡安·拉蒙·希梅内斯
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    中信出版集团
                  </span>
                </p>
                <p class="abstract">

                  许多年以前，在西班牙某一个小乡村里，有一头小毛驴，名叫小银。
它像个小男孩，天真、好奇而又调皮。它喜欢美，甚至还会唱几支简短的咏叹调。
它有自己的语言，足以充分表达它的喜悦、欢乐、沮丧或者失望。
有一天，它悄悄咽了气。世界上从此缺少了它的声音，好像它从来就没有出生过一样 。
这件事说起来真有些叫人忧伤，因此西班牙诗人希梅内斯为它写了一百多首诗。每...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30203294/?icn=index-latestbook-subject" title="哥谭重案组2：小丑与疯人">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29827423.jpg" class=""
                  width="115px" height="172px" alt="哥谭重案组2：小丑与疯人">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30203294/?icn=index-latestbook-subject"
                  title="哥谭重案组2：小丑与疯人">哥谭重案组2：小丑与疯人</a>
              </div>
              <div class="author">
                [美] 艾德·布鲁贝克 格雷格·卢卡 编&nbsp;/&nbsp;迈克尔·拉克 绘
              </div>
              <div class="more-meta">
                <h4 class="title">
                  哥谭重案组2：小丑与疯人
                </h4>
                <p>
                  <span class="author">
                    [美] 艾德·布鲁贝克 格雷格·卢卡 编&nbsp;/&nbsp;迈克尔·拉克 绘
                  </span>
                  /
                  <span class="year">
                    2018-10
                  </span>
                  /
                  <span class="publisher">
                    后浪丨北京联合出版公司
                  </span>
                </p>
                <p class="abstract">

                  在蝙蝠侠的阴影下
做一名哥谭警察
并不容易
◎ 编辑推荐
☆ 被誉为“最佳蝙蝠侠系列漫画”的经典作品。
☆ 美国漫画最高奖艾斯纳奖及哈维奖获奖系列。
☆ 聚焦哥谭警局，解密在蝙蝠侠的阴影下，哥谭的警员们如何同超级罪犯战斗。
☆ 剧情紧张、悬疑，有如一部发生在世界上最疯狂城市中的刑侦美剧。
☆ 人物塑造生动，互动精彩。
◎ 内容简介
《哥谭重案组2：小丑与疯人》是DC经典...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30237193/?icn=index-latestbook-subject" title="一生的凝视">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29856459.jpg" class=""
                  width="115px" height="172px" alt="一生的凝视">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30237193/?icn=index-latestbook-subject"
                  title="一生的凝视">一生的凝视</a>
              </div>
              <div class="author">
                [英] 简 ·鲍恩 摄&nbsp;/&nbsp;[英] 卢克·多德 编
              </div>
              <div class="more-meta">
                <h4 class="title">
                  一生的凝视
                </h4>
                <p>
                  <span class="author">
                    [英] 简 ·鲍恩 摄&nbsp;/&nbsp;[英] 卢克·多德 编
                  </span>
                  /
                  <span class="year">
                    2018-10
                  </span>
                  /
                  <span class="publisher">
                    后浪丨湖南美术出版社
                  </span>
                </p>
                <p class="abstract">

                  “英国布列松”简·鲍恩一生的创作精华
从世界名流的标志性肖像到深刻而温柔的街拍
在曾由男性主宰的英国媒体界她从未空手而归
◎ 编辑推荐
▲ 世界名流在她面前卸下防备，袒露自我
用购物袋装相机的小个子女士简·鲍恩有一种神奇的力量，往往能在五到十 分钟的拍摄许可时间内拍到理想的画面。她不仅能准确把握人物的精髓，还能让对方以自己的心意回应她的对视。在平等坦诚...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30223814/?icn=index-latestbook-subject" title="沙丘5：沙丘异端">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29849458.jpg" class=""
                  width="115px" height="172px" alt="沙丘5：沙丘异端">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30223814/?icn=index-latestbook-subject"
                  title="沙丘5：沙丘异端">沙丘5：沙丘异端</a>
              </div>
              <div class="author">
                [美] 弗兰克·赫伯特
              </div>
              <div class="more-meta">
                <h4 class="title">
                  沙丘5：沙丘异端
                </h4>
                <p>
                  <span class="author">
                    [美] 弗兰克·赫伯特
                  </span>
                  /
                  <span class="year">
                    2018-8
                  </span>
                  /
                  <span class="publisher">
                    江苏凤凰文艺出版社
                  </span>
                </p>
                <p class="abstract">

                  人类每次正视自己的渺小，都是自身的一次巨大进步。
——————————
一千五百年前，神帝雷托遇刺身亡，引发了剧烈的社会动荡，数以万亿计的人离散到整个宇宙。
如今，他们纷纷带着力量重返故土。姐妹会、尊母、特莱拉人……一时间，古老的势力与新兴的力量相继登上舞台，新的争端已然爆发。少女什阿娜，继承了厄崔迪人控制沙虫的能力。她的出现，令这场争端再次升...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30248364/?icn=index-latestbook-subject" title="北斋漫画">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29820393.jpg" class=""
                  width="115px" height="172px" alt="北斋漫画">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30248364/?icn=index-latestbook-subject"
                  title="北斋漫画">北斋漫画</a>
              </div>
              <div class="author">
                葛饰北斋&nbsp;/&nbsp;永田生慈&nbsp;/&nbsp;浦上满
              </div>
              <div class="more-meta">
                <h4 class="title">
                  北斋漫画
                </h4>
                <p>
                  <span class="author">
                    葛饰北斋&nbsp;/&nbsp;永田生慈&nbsp;/&nbsp;浦上满
                  </span>
                  /
                  <span class="year">
                    2018-8-1
                  </span>
                  /
                  <span class="publisher">
                    北京联合出版公司
                  </span>
                </p>
                <p class="abstract">

                  200多年前，一套画尽了世间百态的漫画，曾影响整个世界，它便是《北斋漫画》。《北斋漫画》是日本江户时期的浮世绘画家葛饰北斋，为弟子们绘就的绘画启蒙教科书。收录了葛饰北斋的4000余幅画作，当中既有市井人物的喜怒哀乐，日常生活中的百器百具，又有鸟兽虫鱼、山川草木、名胜古迹、神话传说、历史人物、妖怪幽灵……包罗万象，细致周详，无所不绘及。
此版《北...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30255676/?icn=index-latestbook-subject" title="我一直想要告诉你的事">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29869265.jpg" class=""
                  width="115px" height="172px" alt="我一直想要告诉你的事">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30255676/?icn=index-latestbook-subject"
                  title="我一直想要告诉你的事">我一直想要告诉你的事</a>
              </div>
              <div class="author">
                [加] 艾丽丝·门罗
              </div>
              <div class="more-meta">
                <h4 class="title">
                  我一直想要告诉你的事
                </h4>
                <p>
                  <span class="author">
                    [加] 艾丽丝·门罗
                  </span>
                  /
                  <span class="year">
                    2018-9
                  </span>
                  /
                  <span class="publisher">
                    译林出版社
                  </span>
                </p>
                <p class="abstract">

                  《我一直想要告诉你的事》是2013年诺贝尔文学奖得主艾丽丝·门罗所创作的第三部小说作品，被认为是门罗继《女孩与女人的生活》尝试长篇写作后的成功转身，从此门罗只安心创作短篇。 一直想要告诉你的事，是深埋心中数十年、不得表白的畸恋，是与丈夫所想大相径庭的定情真相，是对不成才却得宠的亲兄弟的厌恶，是缘散后细数那些前尘往事……寻常人的生活，成就了诸多...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30305993/?icn=index-latestbook-subject" title="生活的逻辑">
                <img src="https://img3.doubanio.com/view/subject/m/public/s29881104.jpg" class=""
                  width="115px" height="172px" alt="生活的逻辑">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30305993/?icn=index-latestbook-subject"
                  title="生活的逻辑">生活的逻辑</a>
              </div>
              <div class="author">
                胡悦晗
              </div>
              <div class="more-meta">
                <h4 class="title">
                  生活的逻辑
                </h4>
                <p>
                  <span class="author">
                    胡悦晗
                  </span>
                  /
                  <span class="year">
                    2018-9-1
                  </span>
                  /
                  <span class="publisher">
                    社会科学文献出版社
                  </span>
                </p>
                <p class="abstract">

                  1927年至1937年间，上海、北京知识人主要供职于出版业与教育业；职业收入在城市居民收入中位居中等水平，但个人收入存在巨大差异；在居住、饮食、服饰与出行等日常消费层面也呈现出巨大差异。他们的日常交往主要在家庭、茶社、酒楼与咖啡馆等场所展开，交往方式主要有书信往来、沙龙聚餐、礼物馈赠等多种类型；知名作家及地方上流知识精英阶层拥有复杂的关系网络，...
                </p>
              </div>
            </div>
          </li>


          <li class="">
            <div class="cover">
              <a href="https://book.douban.com/subject/30253372/?icn=index-latestbook-subject" title="青年狗艺术家的画像">
                <img src="https://img1.doubanio.com/view/subject/m/public/s29807319.jpg" class=""
                  width="115px" height="172px" alt="青年狗艺术家的画像">
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a class="" href="https://book.douban.com/subject/30253372/?icn=index-latestbook-subject"
                  title="青年狗艺术家的画像">青年狗艺术家的画像</a>
              </div>
              <div class="author">
                [英] 狄兰·托马斯
              </div>
              <div class="more-meta">
                <h4 class="title">
                  青年狗艺术家的画像
                </h4>
                <p>
                  <span class="author">
                    [英] 狄兰·托马斯
                  </span>
                  /
                  <span class="year">
                    2018-10
                  </span>
                  /
                  <span class="publisher">
                    漓江出版社
                  </span>
                </p>
                <p class="abstract">

                  《青年狗艺术家的画像》是狄兰·托马斯一部半自传性的中短篇小说集。作者一方面表达了自己身为艺术家的想法，另一方面也描述了自己年轻时像狗一样嬉戏、打架的趣事作者兰像写诗一样写小说，笔法跳跃，天马行空，灵感源泉喷薄而发，威尔士小镇的风光和人物跃然纸上；充满诗意的故事中，可以窥见一个男孩成长的过程，充满了异想天开的想法和兴致勃勃的冒险念头。
                </p>
              </div>
            </div>
          </li>
    </ul>

        </div>
      </div>
    </div>
  </div>


  <!-- douban ad begin -->
  <div id="dale_book_home_left_top" class="ad-placeholder" style="margin:-30px 0 30px;"></div>
  <!-- douban app end -->





    <div class="section book_information">
        <div class="hd">

  <h2 class=''>
    <span class="">图书资讯</span>
  </h2>

            <div class="slide-controls">
                <ol class="slide-dots">
                    <li><a data-index="1" href="#"></a></li>
                    <li><a data-index="2" href="#"></a></li>
                    <li><a data-index="3" href="#"></a></li>
                    <li><a data-index="4" href="#"></a></li>
                </ol>
                <div class="slide-btns">
                    <a href="#" class="prev information-prev">&#8249;</a>
                    <a href="#" class="next information-next">&#8250;</a>
                </div>
            </div>
        </div>
        <div class="bd">
            <div class="slide-block">
                <ul class="col slide-list">
                        <li class="slide-item info-block">
                            <a href="https://book.douban.com/review/9672258/">
                                <div class="cover" style="background-image: url(https://img3.doubanio.com/view/subject/l/public/s29838084.jpg)"></div>
                                <div class="content">
                                    <span class="title">浪翻云：文学不是工业，作家也不是爱马仕的皮包匠人</span>
                                    <span class="meta">享读者</span>
                                    <p class="abstract">近日，湘籍作家浪翻云推出了小说《天地会》的第一部，将讲述中国帮派鼻祖的隐秘往事，一代乱世枭雄的隐忍与崛起。在南派江湖小说大家浪翻云的构造下，“天地会”有望成为新的一个大热IP。记者近日对浪翻云进行了...</p>
                                </div>
                            </a>
                        </li>
                        <li class="slide-item info-block">
                            <a href="https://book.douban.com/review/9660739/">
                                <div class="cover" style="background-image: url(https://img1.doubanio.com/view/subject/l/public/s29850128.jpg)"></div>
                                <div class="content">
                                    <span class="title">因为这部小说，她的人生结束得完美无缺</span>
                                    <span class="meta">文治图书</span>
                                    <p class="abstract">文章摘自 | 《阿吽》解说 作者 |山口瞳 翻译｜单元皓 昭和五十五年（1980年）即将落幕的时候，日本文学振兴会的人给我打了个电话。“喂，这是怎么回事？”从声音就能听出他的为难。此前，就在我被选为直木奖评委...</p>
                                </div>
                            </a>
                        </li>
                        <li class="slide-item info-block">
                            <a href="https://www.douban.com/note/691327130/">
                                <div class="cover" style="background-image: url()"></div>
                                <div class="content">
                                    <span class="title">豆瓣一周热门图书｜每个城市都有这样的社区，每个社区都有这样的人</span>
                                    <span class="meta">豆瓣读书</span>
                                    <p class="abstract">九月第四周，作家王占黑短篇小说集《街道江湖》以分镜式的描述对准这个熟人社会，呈现市井小人物的生活状态；普林斯顿大学教授约翰·麦克菲《写作这门手艺》公开讲述普林斯顿大学四十余年的写作课程；法国诗人洛...</p>
                                </div>
                            </a>
                        </li>
                        <li class="slide-item info-block">
                            <a href="https://book.douban.com/review/9658742/">
                                <div class="cover" style="background-image: url(https://img3.doubanio.com/view/subject/l/public/s29810975.jpg)"></div>
                                <div class="content">
                                    <span class="title">欧洲中世纪死刑如何演变成一场宗教秀</span>
                                    <span class="meta">楚尘文化</span>
                                    <p class="abstract">在欧洲，死刑有着悠久而血腥的历史。直到19世纪，死刑行刑均为公开活动；第二次世界大战以来，死刑被越来越谨慎地施行，世界上已有100多个国家废除了死刑，但还是有人死于刽子手之手。 《欧洲死刑史1200—1700》...</p>
                                </div>
                            </a>
                        </li>
                </ul>
            </div>
        </div>
    </div>





  <div class="section popular-books">
    <div class="hd">
      <h2>
        <span>最受关注图书榜</span>
        <span class="link-more">
          <a href="/chart?subcat=F&amp;icn=index-topchart-fiction">虚构类»</a>
        </span>
        <span class="link-more">
          <a href="/chart?icn=index-topchart-nonfiction">非虚构类»</a>
        </span>
      </h2>
    </div>
    <div class="bd">
      <ul class="list-col list-col2 list-summary s"
        data-dstat-areaid="61" data-dstat-mode="click,expose">



  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/30224833/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s29845937.jpg"
          alt="圣殿春秋" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/30224833/?icn=index-topchart-subject" class="">圣殿春秋</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          9.0
        </span>
      </p>
      <p class="author">
        作者：[英] 肯·福莱特
      </p>
      <p class="book-list-classification">
        外国文学&nbsp;/&nbsp;历史
      </p>
      <p class="extra-info">

          <span class="meta-label">有电子书</span>
      </p>

        <p class="reviews">
          上帝可以是假的，天堂可以不存在，但教堂是可以造出来的。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/9596437/?icn=index-topchart-subject">一片瓣瓣评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/30280610/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s29825852.jpg"
          alt="天长地久" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/30280610/?icn=index-topchart-subject" class="">天长地久</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.7
        </span>
      </p>
      <p class="author">
        作者：龙应台
      </p>
      <p class="book-list-classification">
        亲情&nbsp;/&nbsp;散文
      </p>
      <p class="extra-info">

      </p>

        <p class="reviews">
          把母亲当作朋友，趁现在还有时间。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/9610266/?icn=index-topchart-subject">哲空空评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/30198534/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s29799288.jpg"
          alt="死灵之书" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/30198534/?icn=index-topchart-subject" class="">死灵之书</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.5
        </span>
      </p>
      <p class="author">
        作者：[美]H.P.洛夫克拉夫特&nbsp;/&nbsp;[英]莱斯·爱德华兹（绘）
      </p>
      <p class="book-list-classification">
        克苏鲁&nbsp;/&nbsp;恐怖
      </p>
      <p class="extra-info">

          <span class="meta-label">有电子书</span>
      </p>

        <p class="reviews">
          “人类最古老、最强烈的情感便是恐惧，而最古老、最强烈的恐惧则来源于未知”
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/9644270/?icn=index-topchart-subject">某乌鸦评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/30274766/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s29825949.jpg"
          alt="潦草" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/30274766/?icn=index-topchart-subject" class="">潦草</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.9
        </span>
      </p>
      <p class="author">
        作者：贾行家
      </p>
      <p class="book-list-classification">
        随笔&nbsp;/&nbsp;中国当代文学
      </p>
      <p class="extra-info">

      </p>

        <p class="reviews">
          他无异于他所观察的人群。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/9606060/?icn=index-topchart-subject">钟螺评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/30224187/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s29810441.jpg"
          alt="侠隐" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/30224187/?icn=index-topchart-subject" class="">侠隐</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar40 star-img">
        </span>
        <span class="average-rating">
          7.8
        </span>
      </p>
      <p class="author">
        作者：张北海
      </p>
      <p class="book-list-classification">
        老北京&nbsp;/&nbsp;武侠
      </p>
      <p class="extra-info">

          <span class="meta-label">有电子书</span>
      </p>

        <p class="reviews">
          写的是逝去的武林，也是逝去的古都。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/9557148/?icn=index-topchart-subject">魏小河评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/30187217/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s29855169.jpg"
          alt="宋徽宗" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/30187217/?icn=index-topchart-subject" class="">宋徽宗</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.8
        </span>
      </p>
      <p class="author">
        作者：[美] 伊沛霞
      </p>
      <p class="book-list-classification">
        历史&nbsp;/&nbsp;海外汉学
      </p>
      <p class="extra-info">

          <span class="meta-label">有电子书</span>
      </p>

        <p class="reviews">
          在时局的碾压与追逐之下，从一个庸人，走向了一个罪人。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/9539209/?icn=index-topchart-subject">伯樵·阿苏勒评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/30203737/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s29793036.jpg"
          alt="鞑靼人沙漠" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/30203737/?icn=index-topchart-subject" class="">鞑靼人沙漠</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.8
        </span>
      </p>
      <p class="author">
        作者：[意] 迪诺·布扎蒂
      </p>
      <p class="book-list-classification">
        意大利文学&nbsp;/&nbsp;小说
      </p>
      <p class="extra-info">

      </p>

        <p class="reviews">
          或许它是世界上唯一的真相：穷尽一生所追求的幻梦始终只是一个幻梦。
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/9505472/?icn=index-topchart-subject">飞天蝙蝠柯镇恶评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/30199056/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s29765205.jpg"
          alt="铁道之旅" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/30199056/?icn=index-topchart-subject" class="">铁道之旅</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar45 star-img">
        </span>
        <span class="average-rating">
          8.9
        </span>
      </p>
      <p class="author">
        作者：[德]沃尔夫冈•希弗尔布施（Wolfgang Schivelbusch）
      </p>
      <p class="book-list-classification">
        铁路&nbsp;/&nbsp;历史社会学
      </p>
      <p class="extra-info">

          <span class="meta-label">有电子书</span>
      </p>

        <p class="reviews">
          希弗尔布施反复用史料提醒我们，时人对铁道的接受并非像现代人这样理所当然。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/9565244/?icn=index-topchart-subject">示播列评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/subject/27194592/?icn=index-topchart-subject">
        <img src="https://img3.doubanio.com/view/subject/m/public/s29796113.jpg"
          alt="双峰：最终档案" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_fiction'})"
          href="https://book.douban.com/subject/27194592/?icn=index-topchart-subject" class="">双峰：最终档案</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar40 star-img">
        </span>
        <span class="average-rating">
          8.1
        </span>
      </p>
      <p class="author">
        作者：[美]马克·弗罗斯特
      </p>
      <p class="book-list-classification">
        美国&nbsp;/&nbsp;悬疑
      </p>
      <p class="extra-info">

          <span class="meta-label">有电子书</span>
      </p>

        <p class="reviews">
          “我这里有一套探案的文字游戏，你把十几分档案读完，猜猜谁才是真正的凶手！”
          (<a onclick="moreurl(this, {from:'pop_fiction'})" href="https://book.douban.com/review/9543224/?icn=index-topchart-subject">慕容复评论</a>)
        </p>
    </div>
  </li>




  <li class="">
    <div class="cover">
      <a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/subject/30143251/?icn=index-topchart-subject">
        <img src="https://img1.doubanio.com/view/subject/m/public/s29828367.jpg"
          alt="老后破产" class="">
      </a>
    </div>
    <div class="info">
      <h4 class="title">
        <a onclick="moreurl(this, {from:'pop_nonfiction'})"
          href="https://book.douban.com/subject/30143251/?icn=index-topchart-subject" class="">老后破产</a>
      </h4>
      <p class="entry-star-small">
        <span class="allstar40 star-img">
        </span>
        <span class="average-rating">
          7.8
        </span>
      </p>
      <p class="author">
        作者：日本NHK特别节目录制组
      </p>
      <p class="book-list-classification">
        日本&nbsp;/&nbsp;老龄化
      </p>
      <p class="extra-info">

      </p>

        <p class="reviews">
          我们害怕的是在书中看到自己的未来。
          (<a onclick="moreurl(this, {from:'pop_nonfiction'})" href="https://book.douban.com/review/9649199/?icn=index-topchart-subject">骑桶者评论</a>)
        </p>
    </div>
  </li>

      </ul>
    </div>
  </div>


  <!-- douban ad begin -->
  <div id="dale_book_home_left_middle" class="ad-placeholder" style="margin:-50px 0 30px;"></div>
  <!-- douban app end -->


  <div class="section market-books">
    <div class="hd">
      <h2>
        <span>豆瓣书店</span>
        <span class="link-more">
          <a href="https://market.douban.com/book/?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web">查看全部»</a>
        </span>
      </h2>
    </div>
    <div class="bd">

      <div class="top">
        <div class="cover">
          <a href="https://market.douban.com/book/wildfruits?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web">
            <div class="pic" style="background-image: url(https://img3.doubanio.com/view/freyr_page_photo/raw/public/3121.jpg)"></div>
          </a>
        </div>
        <div id="market_books_header_info" class="info">
          <p class="title">野果
            <span class="price">￥69.00</span>
              <span class="free_delivery">／包邮</span>
          </p>
          <p class="desc indent-paragraph" data-row="4">自然主义大师梭罗遗作，秋日尽享《野果》之味 </p>
        </div>
      </div>
      <ul class="list-col list-col5">

          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/lpbeer?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/3094.jpg" width="106" height="140" alt="孤独星球：环球啤酒之旅"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/lpbeer?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">孤独星球：环球啤酒之旅</a>
              </div>
              <div class="price">￥88.50</div>
            </div>
          </li>

          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/Marjane?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/2824.jpg" width="106" height="140" alt="玛赞·莎塔碧漫画小说套装"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/Marjane?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">玛赞·莎塔碧漫画小说套装</a>
              </div>
              <div class="price">￥89.00</div>
            </div>
          </li>

          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/zen?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/3063.jpg" width="106" height="140" alt="禅与摩托车维修艺术：珍藏版"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/zen?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">禅与摩托车维修艺术：珍藏版</a>
              </div>
              <div class="price">￥59.80</div>
            </div>
          </li>

          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/huoniao?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/3035.jpg" width="106" height="140" alt="火鸟"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/huoniao?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">火鸟</a>
              </div>
              <div class="price">￥666.00</div>
            </div>
          </li>

          <li>
            <div class="cover">
              <a href="https://market.douban.com/book/shuangfeng2?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">
                <img src="https://img3.doubanio.com/view/freyr_page_photo/raw/public/2942.jpg" width="106" height="140" alt="双峰：最终档案"/>
              </a>
            </div>
            <div class="info">
              <div class="title">
                <a href="https://market.douban.com/book/shuangfeng2?utm_campaign=book_freyr_section&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank">双峰：最终档案</a>
              </div>
              <div class="price">￥198.00</div>
            </div>
          </li>
      </ul>
    </div>
  </div>


    <div class="section ebook-area"></div>

    <div id="reviews" class="section" ></div>

</div>
      <div class="aside">

  <!-- douban ad begin -->
  <div id="dale_book_home_top_right" class="s ad-placeholder"
    data-dstat-areaid="51" data-dstat-mode="click,expose"
    style="margin-top: 30px;"></div>
  <!-- douban ad end -->

  <!-- douban ad begin -->
  <div id="dale_book_home_top_right2" class="ad-placeholder"></div>
  <!-- douban ad end -->






  <h2 class=''>
    <span class="">热门标签</span>
      <span class="link-more">
        <a class="" href="/tag/?view=type&amp;icn=index-sorttags-all"
          >所有热门标签»</a>
      </span>
  </h2>

  <ul class="hot-tags-col5 s" data-dstat-areaid="54" data-dstat-mode="click,expose">



    <li>
        <ul class="clearfix">
            <li class="tag_title">
                文学
            </li>
            <li>
                <a href="/tag/小说" class="tag">小说</a>
            </li>
            <li>
                <a href="/tag/随笔" class="tag">随笔</a>
            </li>
            <li>
                <a href="/tag/日本文学" class="tag">日本文学</a>
            </li>
            <li class="last">
                  <a href="/tag/散文" class="tag">散文</a>
            </li>
            <li>
                <a href="/tag/诗歌" class="tag">诗歌</a>
            </li>
            <li>
                <a href="/tag/童话" class="tag">童话</a>
            </li>
            <li>
                <a href="/tag/名著" class="tag">名著</a>
            </li>
            <li class="last">
                  <a href="/tag/港台" class="tag">港台</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#文学" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>




    <li>
        <ul class="clearfix">
            <li class="tag_title">
                流行
            </li>
            <li>
                <a href="/tag/漫画" class="tag">漫画</a>
            </li>
            <li>
                <a href="/tag/推理" class="tag">推理</a>
            </li>
            <li>
                <a href="/tag/绘本" class="tag">绘本</a>
            </li>
            <li class="last">
                  <a href="/tag/青春" class="tag">青春</a>
            </li>
            <li>
                <a href="/tag/科幻" class="tag">科幻</a>
            </li>
            <li>
                <a href="/tag/言情" class="tag">言情</a>
            </li>
            <li>
                <a href="/tag/奇幻" class="tag">奇幻</a>
            </li>
            <li class="last">
                  <a href="/tag/武侠" class="tag">武侠</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#流行" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>




    <li>
        <ul class="clearfix">
            <li class="tag_title">
                文化
            </li>
            <li>
                <a href="/tag/历史" class="tag">历史</a>
            </li>
            <li>
                <a href="/tag/哲学" class="tag">哲学</a>
            </li>
            <li>
                <a href="/tag/传记" class="tag">传记</a>
            </li>
            <li class="last">
                  <a href="/tag/设计" class="tag">设计</a>
            </li>
            <li>
                <a href="/tag/建筑" class="tag">建筑</a>
            </li>
            <li>
                <a href="/tag/电影" class="tag">电影</a>
            </li>
            <li>
                <a href="/tag/回忆录" class="tag">回忆录</a>
            </li>
            <li class="last">
                  <a href="/tag/音乐" class="tag">音乐</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#文化" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>




    <li>
        <ul class="clearfix">
            <li class="tag_title">
                生活
            </li>
            <li>
                <a href="/tag/旅行" class="tag">旅行</a>
            </li>
            <li>
                <a href="/tag/励志" class="tag">励志</a>
            </li>
            <li>
                <a href="/tag/职场" class="tag">职场</a>
            </li>
            <li class="last">
                  <a href="/tag/教育" class="tag">教育</a>
            </li>
            <li>
                <a href="/tag/美食" class="tag">美食</a>
            </li>
            <li>
                <a href="/tag/灵修" class="tag">灵修</a>
            </li>
            <li>
                <a href="/tag/健康" class="tag">健康</a>
            </li>
            <li class="last">
                  <a href="/tag/家居" class="tag">家居</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#生活" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>




    <li>
        <ul class="clearfix">
            <li class="tag_title">
                经管
            </li>
            <li>
                <a href="/tag/经济学" class="tag">经济学</a>
            </li>
            <li>
                <a href="/tag/管理" class="tag">管理</a>
            </li>
            <li>
                <a href="/tag/商业" class="tag">商业</a>
            </li>
            <li class="last">
                  <a href="/tag/金融" class="tag">金融</a>
            </li>
            <li>
                <a href="/tag/营销" class="tag">营销</a>
            </li>
            <li>
                <a href="/tag/理财" class="tag">理财</a>
            </li>
            <li>
                <a href="/tag/股票" class="tag">股票</a>
            </li>
            <li class="last">
                  <a href="/tag/企业史" class="tag">企业史</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#经管" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>




    <li>
        <ul class="clearfix">
            <li class="tag_title">
                科技
            </li>
            <li>
                <a href="/tag/科普" class="tag">科普</a>
            </li>
            <li>
                <a href="/tag/互联网" class="tag">互联网</a>
            </li>
            <li>
                <a href="/tag/编程" class="tag">编程</a>
            </li>
            <li class="last">
                  <a href="/tag/交互设计" class="tag">交互设计</a>
            </li>
            <li>
                <a href="/tag/算法" class="tag">算法</a>
            </li>
            <li>
                <a href="/tag/通信" class="tag">通信</a>
            </li>
            <li>
                <a href="/tag/神经网络" class="tag">神经网络</a>
            </li>
            <li class="last">
                  <a href="/tag/?view=type&amp;icn=index-sorttags-hot#科技" class="tag more_tag">更多»</a>
            </li>
        </ul>
    </li>

  </ul>


  <!-- douban ad begin -->
  <div id="dale_book_homepage_right_bottom" class="ad-placeholder"></div>
  <!-- douban ad end -->


<div class="section weekly-top">
    <div class="hd">
        <h2>畅销图书榜</h2>
    </div>
    <div class="bd">
        <ul class="nav-vendor">
            <li class="on book-chart-hd" id="jd-book-chart-hd">
                <img src="https://img3.doubanio.com/f/book/7fd9bf017a2b6c0349981f25700e2b71c12df7d0/pics/book/partner/jd_chart_hover.png" width="18" height="18"/>
                <span>京东</span>
            </li>
            <li class="book-chart-hd" id="dangdang-book-chart-hd">
                <img src="https://img3.doubanio.com/f/book/31b437b71ced2d15e1e110d6be26b070da8c0d4a/pics/book/partner/dangdang_chart.png" width="18" height="18"/>
                <span>当当</span>
            </li>
        </ul>

            <ul class="list list-ranking">
                <li class="item">
                    <span class="rank-num">1.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/11524204/" class="name" target="_blank">围城</a>
                        <div class="author">钱钟书</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=3900&amp;pos=1&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEgZQE1wXBiJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQITAl0cWREdS0IJRmsSfFFVE39cFmJWeTJ6BUlDdHQcXFl1Dh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBtfHQcWBFwrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsVAxcPUhlfCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=11524204" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">2.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/27194530/" class="name" target="_blank">人类简史</a>
                        <div class="author">(法) 贝特朗·菲舒 著/(法) 迪迪埃·巴利赛维克 绘</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=12540&amp;pos=2&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIHZRtYFAcXBFIZWR0yEgRXGF0WCxE3EUQDS10iXhBeGh4cDF8QTwcKWUcYB0UHCwIRBVYdWBwBDV4QRwYlR2J4HUI%252BF0dxDlJ7OUVQUVoBfgUTVB4LOxhaFQsOBlcHWBITEQReGFIeAxI3Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sRAREGUx5eHAIWAFYrXCXbkrCDucnMnJjS3YxrJTIiN2UbaxY%253D%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsWABEBVhJYCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=27194530" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">3.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/6560091/" class="name" target="_blank">新华字典</a>
                        <div class="author">中国社会科学院语言研究所</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=1639&amp;pos=3&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEwFUG10WCyJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQMUBlUdWBwdS0IJRmtzWhp6Ul0ZTWF1HQdnE2EYdQcWWiNDDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBtYFQMbBVIrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsUBBMHUxhSCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=6560091" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">4.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26278316/" class="name" target="_blank">夏洛的网</a>
                        <div class="author">[美] E·B·怀特</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=1820&amp;pos=4&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEgNUG1MVByJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQIWBlUTWxAdS0IJRmtCUEcED0ccTWFrV1McOHN%252FZgEpbChTDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBpfEwoSD1wrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsVBhMHXRteCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=26278316" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">5.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/6973970/" class="name" target="_blank">人间失格</a>
                        <div class="author">[日] 太宰治</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=2190&amp;pos=5&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEw5cHl0dBiJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQMbDlAdUxEdS0IJRmtLQxN0Vx1fFWd0BA5JDW9AU1kLWwlTDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBtbFQIWAFQrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsUCxsCUxNfCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=6973970" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">6.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/1052990/" class="name" target="_blank">草房子</a>
                        <div class="author">曹文轩</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=1430&amp;pos=6&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIHZR5aEQISA1AYUyUCEwddH10RByJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQMSD1EdXxAdS0IJRmtvX2ZDHQEEY2AacSxkOW5VVWEHfARDDh5pVhpbEx4SB0kYWQQCFAxWH1AXBSIAUBxdEgsRAGUbXxQGFjdlG1olUHzf462DsLMO0%252F%252BUjp2VIgZlG18VAhcEXRtZEgAbA2Uca8yCpdH3iYKLiMePwitrJTIiN1QrWg%253D%253D%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsUAhoDUx9eCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=1052990" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">7.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/4913064/" class="name" target="_blank">活着</a>
                        <div class="author">余华</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=1839&amp;pos=7&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEgZdGlwQACJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQITD1QcXhcdS0IJRmtBe2EFAXxSFGdWfVFaQW9YSmMmRT9DDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBpdEwMQAFwrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsVAxoGUh5ZCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=4913064" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">8.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26852422/" class="name" target="_blank">古汉语常用字字典</a>
                        <div class="author">蒋绍愚/唐作藩/张万起/宋绍年/李树青</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=3190&amp;pos=8&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEg9WGl8WAiJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQIaBFQfWBUdS0IJRmt9e21jUk04HGdLW1FgHUFAEHkpGVNTDh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBtbHQEVAlIrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsVChEGURhbCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=26852422" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">9.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/30263126/" class="name" target="_blank">牛津高阶英汉双解词典（第9版）</a>
                        <div class="author">[英] 霍恩比</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=14369&amp;pos=9&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIHZRtYFAcXBFIZWR0yEgRXElwSBxU3EUQDS10iXhBeGh4cDF8QTwcKWUcYB0UHCwIRBVwcXBAFDV4QRwYldHJ3F3IfUlBwdx1QUmF%252FGwcjaV5lRB4LOxhaFQsOBlMHWhcTEgJeGVkeAhQ3Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sRABMDXRNfHQQQDlIrXCXbkrCDucnMnJjS3YxrJTIiN2UbaxYyTUMIRg%253D%253D%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsWABsAUh5cCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=30263126" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">10.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26606389/" class="name" target="_blank">白说</a>
                        <div class="author">白岩松</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=jingdong&amp;srcpage=bestseller&amp;price=3420&amp;pos=10&amp;url=http%3A%2F%2Funion-click.jd.com%2Fjdc%3Fe%3D%26p%3DAyIOZR5aEQISA1AYUyUCEgFSGlMcAiJDCkMFSjJLQhBaUAscSkIBR0ROVw1VC0dFFQIUAFQTUhUdS0IJRmtQBlBFIGNYY2EQYRJDJkdSew8AeCx1Dh43Uh5cEwUbBFIrWxEDFgNlK1sUMkBpja3tzaejG4Gx1MCKhTdUK1sQCxsDUBpSHQMUAVMrXCXbkrCDucnMnJjS3YxrJTIi%26t%3DW1dCFBBFC1pXUwkEAEAdQFkJBVsVBBUGXRJbCltXWwg%253D&amp;srcsubj=&amp;type=bkbuy&amp;subject=26606389" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
            </ul>
            <ul class="list list-ranking">
                <li class="item">
                    <span class="rank-num">1.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26926101/" class="name" target="_blank">我的第一本地理启蒙书</a>
                        <div class="author">郑利强 著/段虹 绘</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=3390&amp;pos=1&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s26926101%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D23967348&amp;srcsubj=&amp;type=bkbuy&amp;subject=26926101" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">2.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/2274208/" class="name" target="_blank">小熊和最好的爸爸（全7册）</a>
                        <div class="author">阿兰德·丹姆 文/亚历克斯·沃尔弗 图</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=3150&amp;pos=2&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s2274208%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D20039611&amp;srcsubj=&amp;type=bkbuy&amp;subject=2274208" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">3.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/4913064/" class="name" target="_blank">活着</a>
                        <div class="author">余华</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=2580&amp;pos=3&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s4913064%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D25137790&amp;srcsubj=&amp;type=bkbuy&amp;subject=4913064" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">4.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26954760/" class="name" target="_blank">月亮与六便士</a>
                        <div class="author">[英] 威廉·萨默塞特·毛姆</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=2870&amp;pos=4&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s26954760%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D24175371&amp;srcsubj=&amp;type=bkbuy&amp;subject=26954760" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">5.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/27012154/" class="name" target="_blank">我喜欢生命本来的样子</a>
                        <div class="author">周国平</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=4280&amp;pos=5&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s27012154%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D24198400&amp;srcsubj=&amp;type=bkbuy&amp;subject=27012154" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">6.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/25969064/" class="name" target="_blank">神奇校车 桥梁书版</a>
                        <div class="author">乔安娜柯尔　著/布鲁斯迪根 图</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=13500&amp;pos=6&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s25969064%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D23444350&amp;srcsubj=&amp;type=bkbuy&amp;subject=25969064" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">7.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/30245565/" class="name" target="_blank">你坏</a>
                        <div class="author">大冰</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=3010&amp;pos=7&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s30245565%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D25288851&amp;srcsubj=&amp;type=bkbuy&amp;subject=30245565" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">8.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26968034/" class="name" target="_blank">正面管教</a>
                        <div class="author">简·尼尔森 (Jane Nelsen)</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=3470&amp;pos=8&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s26968034%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D23990140&amp;srcsubj=&amp;type=bkbuy&amp;subject=26968034" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">9.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/27164116/" class="name" target="_blank">魔法拼音国</a>
                        <div class="author">姜自霞</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=7840&amp;pos=9&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s27164116%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D25081450&amp;srcsubj=&amp;type=bkbuy&amp;subject=27164116" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
                <li class="item">
                    <span class="rank-num">10.</span>
                    <div class="book-info">
                        <a href="https://book.douban.com/subject/26995832/" class="name" target="_blank">我不敢说，我怕被骂</a>
                        <div class="author">皮姆·范·赫斯特/妮可·塔斯马</div>
                    </div>
                    <a href="https://book.douban.com/link2/?pre=0&amp;vendor=dangdang&amp;srcpage=bestseller&amp;price=3140&amp;pos=10&amp;url=http%3A%2F%2Funion.dangdang.com%2Ftransfer.php%3Ffrom%3DP-306226-0-s26995832%26backurl%3Dhttp%3A%2F%2Fproduct.dangdang.com%2Fproduct.aspx%3Fproduct_id%3D24144615&amp;srcsubj=&amp;type=bkbuy&amp;subject=26995832" target="_blank"><span class="buy-button">去购买</span></a>
                </li>
            </ul>
    </div>
</div>



  <div class="block5">


  <h2 class=''>
    <span class="">豆瓣图书250</span>
      <span class="link-more">
        <a class="" href="/top250?icn=index-book250-all"
          >更多»</a>
      </span>
  </h2>


    <div class="content clearfix s" id="book_rec"
      data-dstat-areaid="58"
      data-dstat-mode="click,expose">


    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1048007/?icn=index-book250-subject">
          <img src="https://img3.doubanio.com/view/subject/m/public/s1067863.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1048007/?icn=index-book250-subject">
          高效能人士的七个习惯（精华版）
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1041482/?icn=index-book250-subject">
          <img src="https://img3.doubanio.com/view/subject/m/public/s1800355.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1041482/?icn=index-book250-subject">
          万历十五年
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/2154960/?icn=index-book250-subject">
          <img src="https://img1.doubanio.com/view/subject/m/public/s2611329.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/2154960/?icn=index-book250-subject">
          一个陌生女人的来信
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>
      <div class="clearfix rr" style="width:100%"></div>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1023045/?icn=index-book250-subject">
          <img src="https://img3.doubanio.com/view/subject/m/public/s1015872.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1023045/?icn=index-book250-subject">
          我们仨
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1088065/?icn=index-book250-subject">
          <img src="https://img3.doubanio.com/view/subject/m/public/s1074811.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1088065/?icn=index-book250-subject">
          阿Q正传
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/27614904/?icn=index-book250-subject">
          <img src="https://img3.doubanio.com/view/subject/m/public/s29651121.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/27614904/?icn=index-book250-subject">
          房思琪的初恋乐园
        </a>
        <p class="extra-info">


  <span class="meta-label">
    有电子书
  </span>

        </p>
      </dd>
    </dl>
      <div class="clearfix rr" style="width:100%"></div>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1005521/?icn=index-book250-subject">
          <img src="https://img3.doubanio.com/view/subject/m/public/s1056010.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1005521/?icn=index-book250-subject">
          伊豆的舞女
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1092335/?icn=index-book250-subject">
          <img src="https://img1.doubanio.com/view/subject/m/public/s2832939.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/1092335/?icn=index-book250-subject">
          教父
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>

    <dl>
      <dt>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/2022979/?icn=index-book250-subject">
          <img src="https://img1.doubanio.com/view/subject/m/public/s5813979.jpg" class="m_sub_img">
        </a>
      </dt>
      <dd>
        <a onclick="moreurl(this, {from:'top'})" href="https://book.douban.com/subject/2022979/?icn=index-book250-subject">
          喜宝
        </a>
        <p class="extra-info">


        </p>
      </dd>
    </dl>
      <div class="clearfix rr" style="width:100%"></div>

    </div>
  </div>


  <div class="contact">
    <h2>联系我们</h2>
    <ul class="apply-links">
      <li>
        合作联系：<img src="https://img3.doubanio.com/f/book/6a8e1160fbccbaa8c13ddf72e22145056bda0ba4/pics/book/email_book.png" />
      </li>
    </ul>
  </div>


  <div class="contact mod">
      <h2>关注我们</h2>
      <ul class="embassy-list clearfix">
          <li>
              <a href="https://site.douban.com/book/" target="_blank" class="icon-embassy-site"></a>
              <a href="https://site.douban.com/book/" target="_blank" class="primary-link">豆瓣小站</a>
          </li>
          <li>
              <a href="http://weibo.com/doubandushu" target="_blank" class="icon-embassy-weibo"></a>
              <a href="http://weibo.com/doubandushu" target="_blank" class="primary-link">微博</a>
          </li>
          <li>
              <a class="icon-embassy-weixin">
                  <div class="hover"><img class="home-qrcode" src="https://img3.doubanio.com/f/book/ee2d0bf8adc46ee0e1a53c28abf41a7a3b589e54/pics/book/home_qrcode@2x.jpg"></div>
              </a>
              <a class="primary-link" href="javascript:;">微信</a>
          </li>
      </ul>
  </div>
  <!-- douban app begin -->
  <div class="s" data-dstat-areaid="60" data-dstat-mode="click,expose">
    <!-- douban ad begin -->
    <div id="dale_book_home_inner_middle"></div>
    <div id="dale_book_home_download_middle"></div>
    <!-- douban ad end -->
  </div>
  <!-- douban app end -->

  <!-- douban ad begin -->
  <div id="dale_book_home_bottem_right" class="ad-placeholder"></div>
  <!-- douban ad end -->

      </div>
      <div class="extra">

  <!-- douban ad begin -->
  <div id="dale_book_home_bottom_super_banner" class="ad-placeholder"></div>
  <!-- douban app end -->

      </div>
    </div>
  </div>


  <div id="footer">

<span id="icp" class="fleft gray-link">
    &copy; 2005－2018 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about?policy=disclaimer">免责声明</a>

    · <a href="https://help.douban.com/?app=book" target="_blank">帮助中心</a>
    · <a href="https://book.douban.com/library_invitation">图书馆合作</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

    <script src="https://img3.doubanio.com/f/book/7495d157b1564be6aae1d21c79280b5ea374400a/js/book/lib/do/init.js"
      data-cfg-corelib="https://img3.doubanio.com/f/book/0495cb173e298c28593766009c7b0a953246c5b5/js/book/lib/jquery/jquery.js">
    </script>
  </div>

  </div>



  <script type="text/javascript" src="https://img3.doubanio.com/misc/mixed_static/14a849b70e265daa.js"></script>
  <!-- mako -->


<script>
  window.user_id = window.user_id || ''
  define.config({
    'ui/slide': 'Book.slide'
  , 'ui/bubble': 'Book.Bubble'
  })
  Do.add('book/index', { path: 'https://img3.doubanio.com/f/book/50b2790ba59deba551045acc3fd335f868155ec8/js/book/index.js' })
  Do.add('ui/slide', { path: 'https://img3.doubanio.com/f/book/2f473e3eae1803f9e743ea632607ad4f9677fb3b/js/book/ui/slide.js' })
  Do.add('ui/bubble', { path: 'https://img3.doubanio.com/f/book/95c407df830e0ab6119ed622ee42033acf0af414/js/book/ui/bubble.js' })
  Do.add('widget/tabs', { path: 'https://img3.doubanio.com/f/book/1c240c18b397f6c8583254c27b9c1f1ecebb6075/js/book/widget/tabs.js' })
  Do('book/index')
</script>
  <!-- douban ad begin -->







<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'ZdfdlTai37I',
            criteria = '3:/',
            preview = '',
            debug = false,
            adSlots = ['dale_book_home_top_right', 'dale_book_home_top_right2', 'dale_book_home_left_middle', 'dale_book_home_bottem_right', 'dale_book_home_top_super_banner', 'dale_book_home_left_top', 'dale_book_homepage_right_bottom', 'dale_book_home_inner_middle', 'dale_book_home_download_middle', 'dale_book_home_bottom_super_banner'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'https://img3.doubanio.com/f/adjs/cdc904d1376a43e44bbf399a0aff51973016cd77/ad.release.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>










  <!-- douban ad end -->





<script type="text/javascript">
  var _paq = _paq || [];
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://s.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
  })();
</script>

<script type="text/javascript">
var setMethodWithNs = function(namespace) {
  var ns = namespace ? namespace + '.' : ''
    , fn = function(string) {
        if(!ns) {return string}
        return ns + string
      }
  return fn
}

var gaWithNamespace = function(fn, namespace) {
  var method = setMethodWithNs(namespace)
  fn.call(this, method)
}

var _gaq = _gaq || []
  , accounts = [
      { id: 'UA-7019765-1', namespace: 'douban' }
    , { id: 'UA-7019765-16', namespace: '' }
    ]
  , gaInit = function(account) {
      gaWithNamespace(function(method) {
        gaInitFn.call(this, method, account)
      }, account.namespace)
    }
  , gaInitFn = function(method, account) {
      _gaq.push([method('_setAccount'), account.id])


  _gaq.push([method('_addOrganic'), 'google', 'q'])
  _gaq.push([method('_addOrganic'), 'baidu', 'wd'])
  _gaq.push([method('_addOrganic'), 'soso', 'w'])
  _gaq.push([method('_addOrganic'), 'youdao', 'q'])
  _gaq.push([method('_addOrganic'), 'so.360.cn', 'q'])
  _gaq.push([method('_addOrganic'), 'sogou', 'query'])
  if (account.namespace) {
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣'])
    _gaq.push([method('_addIgnoredOrganic'), 'douban'])
    _gaq.push([method('_addIgnoredOrganic'), '豆瓣网'])
    _gaq.push([method('_addIgnoredOrganic'), 'www.douban.com'])
  }

      if (account.namespace === 'douban') {
        _gaq.push([method('_setDomainName'), '.douban.com'])
      }

        _gaq.push([method('_setCustomVar'), 1, 'responsive_view_mode', 'desktop', 3])

        _gaq.push([method('_setCustomVar'), 2, 'login_status', '0', 2]);

      _gaq.push([method('_trackPageview')])
    }

for(var i = 0, l = accounts.length; i < l; i++) {
  var account = accounts[i]
  gaInit(account)
}


;(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})()
</script>









  <!-- anson42-docker-->

  </body>
</html>







































'''

import  re
pattern = re.compile('.*?cover.*?href="(.*?)" title="(.*?)"', re.S)
result = re.findall(pattern, htlm)
print(result)
print(result.group(2))