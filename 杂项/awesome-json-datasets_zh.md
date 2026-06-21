# 很棒的 JSON 数据集 [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

不需要身份验证的精彩 JSON 数据集的精选列表。

> [!重要]
> 该存储库现已存档。感谢所有贡献者做出的宝贵贡献！

## 内容
* [Bitcoin](#bitcoin)
* [Climate](#climate)
* [Crime](#crime)
* [Currency](#currency)
* [Food](#food)
* [Gaming](#gaming)
* [GitHub API](#github-api)
* [Government](#government)
* [历史事件](#historical-events)
* [HTTP](#http)
* [NASA](#nasa)
* [诺贝尔奖](#nobel-prize)
* [Population](#population)
* [GDP](#gdp)
* [Reddit](#reddit)
* [Travel](#travel)
* [电视节目](#tv-shows)
* [Movies](#movies)
* [开源许可证](#open-source-licenses)
* [更多精彩清单](#more-awesome-lists)
* [Contributing](#contributing)
* [License](#license)

## 比特币
* [最新区块](https://blockchain.info/latestblock)
* [未确认交易](https://blockchain.info/unconfirmed-transactions?format=json)

> 专业提示：查看[加密货币市值](https://api.coinmarketcap.com/v1/ticker/) 了解更多加密货币价格。

## 气候

* [美国年平均气温和距平](https://www.ncdc.noaa.gov/cag/time-series/us/110/00/tavg/ytd/12/1895-2016.json?base_prd=true&begbaseyear=1901&endbaseyear=2000) *(1880-2015 (对比 1901-2000)平均）*
* [美国连续年降水量](https://www.ncdc.noaa.gov/cag/time-series/us/110/00/pcp/ytd/12/1895-2016.json?base_prd=true&begbaseyear=1901&endbaseyear=2000) *(1895-2015)*

## 犯罪

* [DATA.POLICE.UK](https://data.police.uk/docs/)
  * [地点犯罪](https://data.police.uk/api/crimes-at-location?date=2015-02&lat=52.629729&lng=-1.131592)
  * [街头犯罪日期](https://data.police.uk/api/crimes-street-dates)
  * [Neighbourhoods](https://data.police.uk/api/leicestershire/neighbourhoods)
  * [势力列表](https://data.police.uk/api/forces)
* [DATA.GOV](https://www.data.gov/local/)
  * [芝加哥（2001年以来的历史数据）](https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.json?accessType=DOWNLOAD)
  * [洛杉矶（2010年以来的历史数据）](https://data.lacity.org/api/views/y8tr-7khq/rows.json?accessType=DOWNLOAD)

## 货币
* [汇率API](https://www.exchangerate-api.com)
  * [USD](https://api.exchangerate-api.com/v4/latest/USD)
  * [GBP](https://api.exchangerate-api.com/v4/latest/GBP)

## 食品
* [FDA 产品召回](https://api.fda.gov/food/enforcement.json)
* [开放食品事实](https://world.openfoodfacts.org/api/v0/product/5060292302201.json)

## 游戏
* [Pokémon](https://pokeapi.co/docsv2/)
* [神奇宝贝编号](http://pokeapi.co/api/v2/pokemon/1/) *（将“1”替换为所需的神奇宝贝编号）*
* [类型](http://pokeapi.co/api/v2/type/1/) *(将 `1` 替换为另一个数字以检索不同的类型)*
* [能力](http://pokeapi.co/api/v2/ability/1) *(将`1`替换为另一个数字以检索不同的能力)*
* [Pokédex](https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json)
* [万智牌：聚会](http://magic.wizards.com)
  * [MTG LEA 套装 + 附加配件](https://mtgjson.com/json/LEA-x.json)
  * [MTG LEB 套装 + 附加配件](https://mtgjson.com/json/LEB-x.json)
  * [MTG ARN 套装 + 附加配件](https://mtgjson.com/json/ARN-x.json)

> 专业提示：[https://mtgjson.com](https://mtgjson.com) 列出了更多《Magic: The Gathering》卡牌数据集，以及所有数据集的压缩版本。

* [Steam 玩家数量](https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v0001/?format=json&appid=0)

## GitHub API
* [Emojis](https://api.github.com/emojis)
* [Events](https://api.github.com/events)
* [Gists](https://api.github.com/gists)
* [Meta](https://api.github.com/meta)

## 政府
* 美国政治家
  * [现任美国参议员](https://www.govtrack.us/api/v2/role?current=true&role_type=senator)
  * [现任美国代表](https://www.govtrack.us/api/v2/role?current=true&role_type=representative&limit=438)

> 专业提示：[GovTrack](https://www.govtrack.us/) 提供了[强大的 API](https://www.govtrack.us/developers/api)，用于查看国会、点名和法案的数据。

* 司法部
  * [博客文章](https://www.justice.gov/api/v1/blog_entries.json?amp%3Bpagesize=2)
  * [新闻稿](https://www.justice.gov/api/v1/press_releases.json?pagesize=2)
  * [Speeches](https://www.justice.gov/api/v1/speeches.json?pagesize=2)
  * [职位空缺公告](http://www.justice.gov/api/v1/vacancy_announcements.json?pagesize=2)
* 苏格兰议会
  * [Departments](https://data.parliament.scot/api/departments)
  * [Events](https://data.parliament.scot/api/events)
  * [政府角色](https://data.parliament.scot/api/governmentroles)
  * [Members](https://data.parliament.scot/api/members)

> 专业提示：您可以在 [http://parliamentdata.ca/](http://parliamentdata.ca/) 做**很多**更多事情

* 印度政府
  * [州代码](http://vocab.nic.in/rest.php/states/json)
  * [消费者物价指数](https://data.gov.in/node/1084041/datastore/export/json)
  * [农业生产](https://data.gov.in/node/135611/datastore/export/json)
  * [区/DRDA/街区/村庄的数量](https://data.gov.in/node/100853/datastore/export/json)
  * [按现价计算的国内生产总值](https://www.quandl.com/api/v1/datasets/MOSPI/GDP.json)
* 澳大利亚
  * [ABC 本地电台](http://data.gov.au/geoserver/abc-local-stations/wfs?request=GetFeature&typeName=ckan_d534c0e9_a9bf_487b_ac8f_b7877a09d162&outputFormat=json)
  * [维多利亚州警察局地点](http://data.gov.au/geoserver/police-station-locations/wfs?request=GetFeature&typeName=762b47b2_e706_4cab_b0c7_cf8e406aefc1&outputFormat=json)
  * [维多利亚博物馆收藏](https://collections.museumvictoria.com.au/api/search)
* 西班牙
  * [马德里省直辖市](https://datos.comunidad.madrid/catalogo/dataset/032474a0-bf11-4465-bb92-392052962866/resource/301aed82-339b-4005-ab20-06db41ee7017/download/municipio_comunidad_madrid.json)
  * [巴塞罗那省直辖市](https://do.diba.cat/api/dataset/municipis/format/json2)
  * [马德里省教育中心（非大学）](https://datos.comunidad.madrid/catalogo/dataset/ae433b7e-98f7-4547-8aa5-6ada557a429f/resource/21424b1c-6465-4db9-a5e3-6ddf180c634b/download/centros_educativos.json)

> 专业提示：在 [https://datos.gob.es/](https://datos.gob.es/catalogo?res_format_label=JSON)，您可以过滤各种公共西班牙语数据。从大学到地方和地区政府机构。

## 历史事件
* 语言
  * [English](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=en)
  * [German](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=de)
  * [Italian](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=it)
  * [Spanish](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=es)
  * [Portuguese](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=pt)
  * [Catalan](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=ca)
  * [Indonesian](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=id)
  * [Romanian](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=ro)
  * [Turkish](http://www.vizgr.org/historical-events/search.php?format=json&begin_date=-3000000&end_date=20151231&lang=tr)

> 专业提示：您可以更改 URL 中的“begin_date”和“end_date”以获取特定时间间隔内的事件。更多选项[此处](http://www.vizgr.org/historical-events/)。

## HTTP协议
* [IP](http://httpbin.org/ip)
* [user-agent](http://httpbin.org/user-agent)
* [headers](http://httpbin.org/headers)
* [GET](http://httpbin.org/get)
* [gzip](http://httpbin.org/gzip)
* [deflate](http://httpbin.org/deflate)
* [response-headers](http://httpbin.org/response-headers?Content-Type=text/plain;%20charset=UTF-8&Server=MaxCDN)
* [cookies](http://httpbin.org/cookies)
* [stream](http://httpbin.org/stream/10)
* [delay](http://httpbin.org/delay/3)
* [缓存](http://httpbin.org/cache/60) *(`60` === `60 秒`)*

> 专业提示：您可以在 [http://httpbin.org](http://httpbin.org/) 上做**更多**事情。

## 美国宇航局
* [国际空间站当前位置](http://api.open-notify.org/iss-now.json)
* [现在有多少人在太空中](http://api.open-notify.org/astros.json)
* [地球陨石着陆](https://data.nasa.gov/resource/y77d-th95.json)
* [近地小行星和彗星](https://data.nasa.gov/resource/2vr3-k9wn.json) *（NEOWISE发现）*

## 自然灾害
* [Earthquakes](https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson)

## 诺贝尔奖
* [Prize](http://api.nobelprize.org/v1/prize.json)
* [Laureate](http://api.nobelprize.org/v1/laureate.json)
* [Country](http://api.nobelprize.org/v1/country.json)

## 开源许可证
* [All](https://api.opensource.org/licenses/)
* [Copyleft](https://api.opensource.org/licenses/copyleft)
* [OSI 批准](https://api.opensource.org/licenses/osi-approved)
* [Redundant](https://api.opensource.org/licenses/redundant)
* [Permissive](https://api.opensource.org/licenses/permissive)
* [Obsolete](https://api.opensource.org/licenses/obsolete)
* [Misc](https://api.opensource.org/licenses/miscellaneous)
* [Popular](https://api.opensource.org/licenses/popular)
* [Discouraged](https://api.opensource.org/licenses/discouraged)
* [Non-reusable](https://api.opensource.org/licenses/non-reusable)
* [特殊用途](https://api.opensource.org/licenses/special-purpose)
* [Retired](https://api.opensource.org/licenses/retired)

> 成为 OSI 成员 [此处](https://opensource.org/civicrm/contribute/transact?reset=1&id=1)

## 人口

* 历史人口（1960年以来）
  * [China](http://api.worldbank.org/countries/CHN/indicators/SP.POP.TOTL?per_page=5000&format=json)
  * [India](http://api.worldbank.org/countries/IND/indicators/SP.POP.TOTL?per_page=5000&format=json)
  * [美国](http://api.worldbank.org/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json)

## 国内生产总值
* [USA](http://api.worldbank.org/countries/USA/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json)
* [China](http://api.worldbank.org/countries/CHN/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json)
* [India](http://api.worldbank.org/countries/IND/indicators/NY.GDP.MKTP.CD?per_page=5000&format=json)

> 专业提示：链接到国家/地区列表[此处](http://api.worldbank.org/countries?per_page=304&format=json)

## 红迪网
* [/r/all](https://www.reddit.com/r/all.json)
* [/r/AskReddit](https://www.reddit.com/r/AskReddit.json)
* [/r/funny](https://www.reddit.com/r/funny.json)
* [/r/pics](https://www.reddit.com/r/pics.json)
* [/r/todayilearned](https://www.reddit.com/r/todayilearned.json)
* [/r/announcements](https://www.reddit.com/r/announcements.json)
* [/r/worldnews](https://www.reddit.com/r/worldnews.json)
* [/r/science](https://www.reddit.com/r/science.json)
* [/r/IAmA](https://www.reddit.com/r/IAmA.json)
* [/r/videos](https://www.reddit.com/r/videos.json)
* [/r/gaming](https://www.reddit.com/r/gaming.json)
* [/r/linux](https://www.reddit.com/r/linux.json)

> 专业提示：您可以将 `.json` 附加到任何 subreddit url。

## 旅行
* [2003-2016 年各机场每月航空公司延误情况](https://think.cs.vt.edu/corgis/datasets/json/airlines/airlines.json)
* 美国联邦航空管理局 (FAA) 机场状况
  * [SFO](http://services.faa.gov/airport/status/SFO?format=application/json)
  * [LAX](http://services.faa.gov/airport/status/LAX?format=application/json)
  * [PHX](http://services.faa.gov/airport/status/PHX?format=application/json)
  * [JFK](http://services.faa.gov/airport/status/JFK?format=application/json)
  * [ATL](http://services.faa.gov/airport/status/ATL?format=application/json)
  * [MIA](http://services.faa.gov/airport/status/MIA?format=application/json)
  * [AUS](http://services.faa.gov/airport/status/AUS?format=application/json)
  * [BOS](http://services.faa.gov/airport/status/BOS?format=application/json)
  * [CLE](http://services.faa.gov/airport/status/CLE?format=application/json)
  * [ORD](http://services.faa.gov/airport/status/ORD?format=application/json)
  * [PDX](http://services.faa.gov/airport/status/PDX?format=application/json)
  * [SJC](http://services.faa.gov/airport/status/SJC?format=application/json)

> 注意：仅适用于美国机场，不适用于国际机场。

## 电视节目

* [机器人先生（美国）](http://api.tvmaze.com/singlesearch/shows?q=mr-robot&embed=episodes)
* [风骚律师 (AMC)](http://api.tvmaze.com/singlesearch/shows?q=better-call-saul&embed=episodes)
* [祖国（演出时间）](http://api.tvmaze.com/singlesearch/shows?q=Homeland&embed=episodes)
* [硅谷（HBO）](http://api.tvmaze.com/singlesearch/shows?q=silicon-valley&embed=episodes)
* [行尸走肉 (AMC)](http://api.tvmaze.com/singlesearch/shows?q=the-walking-dead&embed=episodes)
* [南方公园（喜剧中心）](http://api.tvmaze.com/singlesearch/shows?q=south-park&embed=episodes)
* [权力的游戏 (HBO)](http://api.tvmaze.com/singlesearch/shows?q=game-of-thrones&embed=episodes)
* [纸牌屋 (Netflix)](http://api.tvmaze.com/singlesearch/shows?q=house-of-cards&embed=episodes)
* [《生活大爆炸》（哥伦比亚广播公司）](http://api.tvmaze.com/singlesearch/shows?q=big-bang-theory&embed=episodes)
* [毒枭 (Netflix)](http://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes)
* [黑镜（Netflix）](http://api.tvmaze.com/singlesearch/shows?q=black-mirror&embed=episodes)
* [怪奇物语（Netflix）](http://api.tvmaze.com/singlesearch/shows?q=stranger-things&embed=episodes)
* [瑞克和莫蒂（成人游泳）](http://api.tvmaze.com/singlesearch/shows?q=rick-&-morty&embed=episodes)
* [西部世界 (HBO)](http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes)

> 专业提示：替换未列出的节目的字段值，例如`显示？q=显示名称`。更多选项[此处](http://www.tvmaze.com/api)

*瑞克和莫蒂
  * [获取所有字符](https://rickandmortyapi.com/api/character/)
  * [获取单个字符](https://rickandmortyapi.com/api/character/2)
  * [过滤位置](https://rickandmortyapi.com/api/location/?name=earth)
  * [获取一集](https://rickandmortyapi.com/api/episode/12)
  * [获取多个剧集](https://rickandmortyapi.com/api/episode/10,28)

> 专业提示：更多选项请访问 [https://rickandmortyapi.com/](https://rickandmortyapi.com/)

## 电影
* [从维基百科中删除的美国电影](https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json)
* [Showtime](http://showtimes.everyday.in.th/api/v2/)
  * [泰国当前上映的电影](http://showtimes.everyday.in.th/api/v2/movie/)
  * [在泰国的电影院](http://showtimes.everyday.in.th/api/v2/theater/)

## 更多精彩清单
* [真棒](https://github.com/sindresorhus/awesome) *(OG 列表)*
* [寻求帮助](https://github.com/fullstackla/awesome-help-wanted) *（寻求帮助的开源项目）*
* [JSON](https://github.com/burningtree/awesome-json) *（库和资源）*
* [WPO](https://github.com/davidsonfellipe/awesome-wpo) *（网页性能优化）*
* [Shell](https://github.com/alebcay/awesome-shell) *（CLI 框架、工具包和指南）*
* [公共 API](https://github.com/toddmotto/public-apis) *（用于 Web 开发的 JSON API，其中一些需要身份验证）*
* [公共数据集](https://github.com/caesar0301/awesome-public-datasets) *（不仅仅是 JSON 的数据集）*
* [风格指南](https://github.com/kciter/awesome-style-guide) *(编程语言、平台、框架)*

## 贡献
如果您想贡献，请阅读[贡献指南](CONTRIBUTING.md)。

## 许可证
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

在法律允许的范围内，[MaxCDN](https://www.maxcdn.com) 已放弃本作品的所有版权以及相关或邻接权。

<img src="https://static.scarf.sh/a.png?x-pxid=bb0fba6a-42e5-4544-9348-f91051d1aa4b" />
