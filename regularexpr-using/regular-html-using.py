#!/usr/bin/python
#coding:utf8
#author:MagiRui

html = '''
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
'''

import  re
pattern = re.compile('.*?cover.*?href="(.*?)".*?title="(.*?)"', re.S)
result = re.findall(pattern, html)
print(result)

