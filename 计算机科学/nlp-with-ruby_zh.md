<img src="header.png" align="center">

[![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome#readme) [![Support Me](https://img.shields.io/badge/%F0%9F%92%97-Support%20Me-blue.svg?style=flat-square)](https://www.patreon.com/arbox)

[[RubyML](https://github.com/arbox/machine-learning-with-ruby) |
[RubyDataScience](https://github.com/arbox/data-science-with-ruby) |
[RubyInterop](https://github.com/arbox/ruby-interoperability)]


# 使用 Ruby 实现出色的 NLP [<img src="ruby.jpg"align="left" width="30px" height="30px" />][ruby]

> 在 Ruby 中进行文本处理的有用资源

此精选列表包括 [_awesome_](https://github.com/sindresorhus/awesome/blob/master/awesome.md)
有关文本计算处理的资源、图书馆、信息源
使用人类语言[Ruby 编程语言](ruby)。
该字段通常被称为
[NLP](https://en.wikipedia.org/wiki/Natural_language_processing),
[计算语言学](https://en.wikipedia.org/wiki/Computational_linguistics),
[HLT](https://en.wikipedia.org/wiki/Language_technology)（人类语言技术）
并且可以与
[人工智能](https://en.wikipedia.org/wiki/Artificial_intelligence),
[机器学习](https://en.wikipedia.org/wiki/Machine_learning),
[信息检索](https://en.wikipedia.org/wiki/Information_retrieval),
[文本挖掘](https://en.wikipedia.org/wiki/Text_mining),
[知识提取](https://en.wikipedia.org/wiki/Knowledge_extraction)
及其他相关学科。

该列表来自我们在语言模型和 NLP 工具方面的日常工作。
阅读[为什么](motivation.md) 这个列表很棒。我们的 [常见问题解答](FAQ.md) 描述了
您可能感兴趣的重要决定和有用的答案。

:sparkles: 欢迎每一个[贡献](#contributing)！通过拉取添加链接
请求或创建问题来开始讨论。

在 [Twitter](https://twitter.com/NonWebRuby) 上关注我们
请使用“#RubyNLP”哈希标签传播信息！

<!-- nodoc -->
## 内容

<!-- toc -->

- [:sparkles: 教程](#sparkles-tutorials)
- [NLP 管道子任务](#nlp-pipeline-subtasks)
  * [管道生成](#pipeline-generation)
  * [多用途发动机](#multipurpose-engines)
+ [在线 API](#on-line-apis)
  * [语言识别](#language-identification)
  * [Segmentation](#segmentation)
  * [词汇处理](#lexical-processing)
+ [词干提取](#stemming)
+ [词形还原](#词形还原)
+ [词法统计：计数类型和标记](#lexical-statistics-counting-types-and-tokens)
+ [过滤停用词](#filtering-stop-words)
  * [短语级别处理](#phrasal-level-processing)
  * [句法处理](#syntactic-processing)
+ [选区解析](#constituency-parsing)
  * [语义分析](#semantic-analysis)
  * [语用分析](#pragmatical-analysis)
- [高级别任务](#high-level-tasks)
  * [拼写和纠错](#spelling-and-error-correction)
  * [文本对齐](#text-alignment)
  * [机器翻译](#machine-translation)
  * [情绪分析](#sentiment-analysis)
  * [数字、日期和时间解析](#numbers-dates-and-time-parsing)
  * [命名实体识别](#named-entity-recognition)
  * [Text-to-Speech-to-Text](#text-to-speech-to-text)
- [对话代理、助理和聊天机器人](#dialog-agents-assistants-and-chatbots)
- [语言资源](#linguistic-resources)
- [机器学习库](#machine-learning-libraries)
- [数据可视化](#data-visualization)
- [光学字符识别](#optical-character-recognition)
- [文本提取](#text-extraction)
- [全文搜索、信息检索、索引](#full-text-search-information-retrieval-indexing)
- [语言感知字符串操作](#language-aware-string-manipulation)
- [文章、帖子、演讲和演示](#articles-posts-talks-and-presentations)
- [项目和代码示例](#projects-and-code-examples)
- [Books](#books)
- [Community](#community)
- [需要您的帮助！](#needs-your-help)
- [相关资源](#related-resources)
- [License](#license)

<!-- tocstop -->

<!-- doc -->

## :sparkles: 教程

请帮助我们填写此部分！ ：笑脸：

## NLP 管道子任务

NLP 管道以纯文本开始。

### 管道生成

- [composable_operations](https://github.com/t6d/composable_operations) - 
操作管道的定义框架。
- [ruby-spark](https://github.com/ondra-m/ruby-spark) - 
Spark 绑定具有易于理解的 DSL。
- [phobos](https://github.com/phobos/phobos) - 
[Apache Kafka](https://kafka.apache.org/) 的简化 Ruby 客户端。
- [parallel](https://github.com/grosser/parallel) - 
用于在多个 CPU 或多个线程中并行执行的主管。
- [pwrake](https://github.com/masa16/pwrake) - 
Rake 扩展可并行运行本地和远程任务。

### 多用途发动机

- [open-nlp](https://github.com/louismullie/open-nlp) - 
[OpenNLP](https://opennlp.apache.org/) 工具包的 Ruby 绑定。
- [stanford-core-nlp](https://github.com/louismullie/stanford-core-nlp) - 
斯坦福 [CoreNLP](https://github.com/stanfordnlp/CoreNLP) 工具的 Ruby 绑定。
- [treat](https://github.com/louismullie/treat) - 
Ruby 的自然语言处理框架（如 Python 的 [NLTK](http://www.nltk.org/)）。
- [nlp_toolz](https://github.com/LeFnord/nlp_toolz) - 
包装一些 [OpenNLP](https://opennlp.apache.org/) 类和
原始的[伯克利解析器](https://github.com/slavpetrov/berkeleyparser)。
- [open_nlp](https://github.com/hck/open_nlp) - 
[OpenNLP](https://opennlp.apache.org/) 工具包的 JRuby 绑定。
- [ruby-spacy](https://github.com/yohasebe/ruby-spacy) &mdash;
通过 [PyCall](https://github.com/mrkn/pycall.rb) 的 spaCy NLP 库的包装模块。

#### 在线API

- [alchemyapi_ruby](https://github.com/alchemyapi/alchemyapi_ruby) - 
适用于 AlchemyAPI/Bluemix 的旧版 Ruby SDK。
- [wit-ruby](https://github.com/wit-ai/wit-ruby) - 
用于 [Wit.ai](https://wit.ai/) 语言理解平台的 Ruby 客户端库。
- [wlapi](https://github.com/arbox/wlapi) - Ruby 客户端库
[Wortschatz Leipzig](http://wortschatz.uni-leipzig.de/de) 网络服务。
- [monkeylearn-ruby](https://github.com/monkeylearn/monkeylearn-ruby) - 情绪
分析、主题建模、语言检测、命名实体识别
基于 Ruby 的 Web API 客户端。
- [google-cloud-language](https://github.com/googleapis/google-cloud-ruby/tree/master/google-cloud-language) - 
Google 的 Ruby 自然语言服务 API。

### 语言识别

语言识别是每个 NLP 流程中首要的关键步骤之一。

- [scylla](https://github.com/hashwin/scylla) - 
语言分类和识别。

### 细分

用于标记化、单词和句子边界检测和消歧的工具。

- [tokenizer](https://github.com/arbox/tokenizer) - 
简单的多语言分词器。
  <sup>[[tutorial](tutorials/tokenizer.md)]</sup>
- [pragmatic_tokenizer](https://github.com/diasks2/pragmatic_tokenizer) - 
用于将字符串拆分为标记的多语言分词器。
- [nlp-pure](https://github.com/parhamr/nlp-pure) - 
用纯 Ruby 实现的自然语言处理算法具有最小的依赖性。
- [textoken](https://github.com/manorie/textoken) - 
简单且可定制的文本标记化库。
- [pragmatic_segmenter](https://github.com/diasks2/pragmatic_segmenter) - 
使用许多 cookie 进行单词边界消歧。
- [punkt-segmenter](https://github.com/lfcipriani/punkt-segmenter) - 
Punkt Segmenter 的纯 Ruby 实现。
- [tactful_tokenizer](https://github.com/zencephalon/Tactful_Tokenizer) - 
针对不同语言的基于正则表达式的分词器。
- [scapel](https://github.com/louismullie/scalpel) - 
句子边界消歧工具。

### 词汇处理

#### 词干提取

词干提取是信息检索中使用的术语，用于描述以下过程：
将词形简化为某种基本表示形式。词干要区分
来自 [Lemmatization](#lemmatization) 因为 `stems` 不一定有
语言动机。

- [ruby-stemmer](https://github.com/aurelian/ruby-stemmer) - 
Ruby-Stemmer 将 SnowBall API 公开给 Ruby。
- [uea-stemmer](https://github.com/ealdent/uea-stemmer) - 
用于搜索和索引的保守词干分析器。

#### 词形还原

词形还原被认为是寻找单词基本形式的过程。引理
经常被收录在字典中。

- [lemmatizer](https://github.com/yohasebe/lemmatizer) - 
基于 WordNet 的英语文本词形还原器。

#### 词法统计：计算类型和标记

- [wc](https://github.com/thesp0nge/wc) - 
计算文本中单词出现次数的工具。
- [word_count](https://github.com/AtelierConvivialite/word_count) - 
“String”和“Hash”对象的字计数器。
- [words_counted](https://github.com/abitdodgy/words_counted) - 
纯 Ruby 库使用不同的自定义选项进行单词统计。

#### 过滤停用词

- [stopwords-filter](https://github.com/brenes/stopwords-filter) - 过滤器和
基于 SnowBall 词形还原器的停用词词典。

### 短语级别处理

- [n_gram](https://github.com/reddavis/N-Gram) - 
N 元语法生成器。
- [ruby-ngram](https://github.com/tkellen/ruby-ngram) - 
将单词和短语分解为 ngram。
- [raingrams](https://github.com/postmodern/raingrams) - 
用纯 Ruby 编写的灵活且通用的 ngrams 库。

### 句法处理

#### 选区解析

- [stanfordparser](https://rubygems.org/gems/stanfordparser) - 
斯坦福解析器的基于 Ruby 的包装器。
- [rley](https://github.com/famished-tiger/Rley) - 
[Earley](https://en.wikipedia.org/wiki/Earley_parser) 的纯 Ruby 实现
上下文无关选区语法的解析算法。
- [rsyntaxtree](https://github.com/yohasebe/rsyntaxtree) - 
基于 [RMagick](https://github.com/rmagick/rmagick) 的 Ruby 语法树可视化。
  <sup>[dep: [ImageMagick](#imagemagick)]</sup>

### 语义分析

- [amatch](https://github.com/flori/amatch) - 
字符串之间的五种距离类型集（包括 Levenshtein、Sellers、Jaro-Winkler、“对距离”）。
- [damerau-levenshtein](https://github.com/GlobalNamesArchitecture/damerau-levenshtein) - 
使用 Damerau-Levenshtein 算法计算编辑距离。
- [hotwater](https://github.com/colinsurprenant/hotwater) - 
快速 Ruby FFI 字符串编辑距离算法。
- [levenshtein-ffi](https://github.com/dbalatero/levenshtein-ffi) - 
使用 Damerau-Levenshtein 算法进行快速字符串编辑距离计算。
- [tf_idf](https://github.com/reddavis/TF-IDF) - 
纯 Ruby 中的术语频率/逆文档频率。
- [tf-idf-similarity](https://github.com/jpmckinney/tf-idf-similarity) - 
使用 TF/IDF 计算文本之间的相似度。

### 语用分析
- [SentimentLib](https://github.com/nzaillian/sentiment_lib) - 
简单的可扩展情感分析 gem。

## 高级别任务

### 拼写和纠错

- [gingerice](https://github.com/subosito/gingerice) - 
通过 [Ginger](https://www.gingersoftware.com/) API 进行拼写和语法更正。
- [hunspell-i18n](https://github.com/romanbsd/hunspell) - 
Ruby 绑定到标准 [Hunspell](https://hunspell.github.io/) 拼写检查器。
- [ffi-hunspell](https://github.com/postmodern/ffi-hunspell) - 
[Hunspell](https://hunspell.github.io/) 的基于 FFI 的 Ruby 绑定。
- [hunspell](https://github.com/segabor/Hunspell) - 
Ruby 通过 Ruby C API 绑定到 [Hunspell](https://hunspell.github.io/)。

### 文本对齐

- [alignment](https://github.com/povilasjurcys/alignment) - 
双语文本的对齐例程（Gale-Church 实施）。

### 机器翻译

- [google-api-client](https://github.com/googleapis/google-api-ruby-client) - 
Google API Ruby 客户端。
- [microsoft_translator](https://github.com/ikayzo/microsoft_translator) - 
微软翻译 API 的 Ruby 客户端。
- [termit](https://github.com/pawurb/termit) - 
谷歌翻译与您的终端中的语音合成。
- [zipf](https://github.com/pks/zipf) - 
BLEU 和其他基本算法的实现。

### 情绪分析

- [stimmung](https://github.com/pachacamac/stimmung) - 
基于语义极性
[SentiWS](http://wortschatz.uni-leipzig.de/en/download) 词典。

### 数字、日期和时间解析

- [chronic](https://github.com/mojombo/chronic) - 
纯 Ruby 自然语言日期解析器。
- [chronic_between](https://github.com/jrobertson/chronic_between) - 
用于日期和时间范围的简单 Ruby 自然语言解析器。
- [chronic_duration](https://github.com/henrypoydar/chronic_duration) - 
用于计算经过时间的纯 Ruby 解析器。
- [kronic](https://github.com/xaviershay/kronic) - 
解析和格式化人类可读日期的方法。
- [nickel](https://github.com/iainbeeston/nickel) - 
从自然措辞的文本中提取日期、时间和消息信息。
- [tickle](https://github.com/yb66/tickle) - 
用于重复发生和重复事件的解析器。
- [numerizer](https://github.com/jduff/numerizer) - 
用于英语数字表达式的 Ruby 解析器。

### 命名实体识别

- [ruby-ner](https://github.com/mblongii/ruby-ner) - 
使用斯坦福 NER 和 Ruby 进行命名实体识别。
- [ruby-nlp](https://github.com/tiendung/ruby-nlp) - 
斯坦福 Pos-Tagger 和名称实体识别器的 Ruby 绑定。

### 文本到语音到文本

- [espeak-ruby](https://github.com/dejan/espeak-ruby) - 
小型 Ruby API，用于利用“espeak”和“lame”创建文本转语音 mp3 文件。
- [tts](https://github.com/c2h2/tts) - 
使用 Google 翻译服务进行文本到语音转换。
- [att_speech](https://github.com/adhearsion/att_speech) - 
AT&T 语音 API 上的 Ruby 包装器，用于语音转文本。
- [pocketsphinx-ruby](https://github.com/watsonbox/pocketsphinx-ruby) - 
口袋狮身人面像绑定。

## 对话代理、助理和聊天机器人

- [chatterbot](https://github.com/muffinista/chatterbot) - 
简单的基于 ruby 的 Twitter Bot 框架，使用 OAuth 进行身份验证。
- [lita](https://github.com/litaio/lita) - 
在[Redis](https://redis.io/)上使用持久存储编写的高度可扩展的聊天操作机器人框架。

## 语言资源

- [rwordnet](https://github.com/doches/rwordnet) - 
适用于 [Princeton WordNet®](https://wordnet.princeton.edu/) 的纯 Ruby 自包含 API 库。
- [wordnet](https://github.com/ged/ruby-wordnet/blob/master/README.rdoc) - 
[Princeton WordNet®](https://wordnet.princeton.edu/) 的性能优化绑定。

## 机器学习库

[机器学习](https://en.wikipedia.org/wiki/Machine_learning) 算法
使用纯 Ruby 或使用其他编程语言编写并具有适当的绑定
对于鲁比来说。

有关更多最新列表，请查看 [Awesome ML with Ruby][ml-with-ruby] 列表。

- [rb-libsvm](https://github.com/febeling/rb-libsvm) - 
使用 Ruby 的支持向量机。
- [weka](https://github.com/paulgoetze/weka-jruby) - 
Weka 的 JRuby 绑定，通过 Weka 实现的不同 ML 算法。
- [decisiontree](https://github.com/igrigorik/decisiontree) - 
纯 Ruby 中的决策树 ID3 算法
  <sup>[[post](https://www.igvita.com/2007/04/16/decision-tree-learning-in-ruby/)]</sup>.
- [rtimbl](https://github.com/maspwr/rtimbl) - 
来自 Timbl 框架的基于记忆的学习器。
- [classifier-reborn](https://github.com/jekyll/classifier-reborn) - 
通用分类器模块允许贝叶斯和其他类型的分类。
- [lda-ruby](https://github.com/ealdent/lda-ruby) - 
[LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) 的 Ruby 实现
（潜在狄利克雷分配）用于自动主题建模和文档聚类。
- [liblinear-ruby-swig](https://github.com/tomz/liblinear-ruby-swig) - 
LIBLINEAR 的 Ruby 接口（比 LIBSVM 对于文本分类更有效）。
- [linnaeus](https://github.com/djcp/linnaeus) - 
Redis 支持的贝叶斯分类器。
- [maxent_string_classifier](https://github.com/mccraigmccraig/maxent_string_classifier) - 
用于字符串数据的 JRuby 最大熵分类器，基于 OpenNLP Maxent 框架。
- [naive_bayes](https://github.com/reddavis/Naive-Bayes) - 
简单的朴素贝叶斯分类器。
- [nbayes](https://github.com/oasic/nbayes) - 
朴素贝叶斯的全功能 Ruby 实现。
- [omnicat](https://github.com/mustafaturan/omnicat) - 
用于文本分类的通用机架框架。
- [omnicat-bayes](https://github.com/mustafaturan/omnicat-bayes) - 
朴素贝叶斯文本分类实现作为 OmniCat 分类器策略。
- [ruby-fann](https://github.com/tangledpath/ruby-fann) - 
Ruby 绑定到[快速人工神经网络库 (FANN)](http://leenissen.dk/fann/wp/)。
- [rblearn](https://github.com/himkt/rblearn) - 特征提取和交叉验证库。

## 数据可视化

请参考【数据可视化】(https://github.com/arbox/data-science-with-ruby#visualization)
[Data Science with Ruby][ds-with-ruby] 列表中的部分。

## 光学字符识别

* [tesseract-ocr](https://github.com/meh/ruby-tesseract-ocr) - 
[Tesseract OCR 引擎](https://github.com/tesseract-ocr/tesseract) 上基于 FFI 的包装器。

## 文本提取

- [yomu](https://github.com/yomurb/yomu) - 
用于从文件和文档中提取文本和元数据的库
使用 [Apache Tika](https://tika.apache.org/) 内容分析工具包。

## 全文搜索、信息检索、索引

- [rsolr](https://github.com/rsolr/rsolr) - 
[Apache Solr](http://lucene.apache.org/solr/) 的 Ruby 和 Rails 客户端库。
- [sunspot](https://github.com/sunspot/sunspot) - 
[Apache Solr](http://lucene.apache.org/solr/) 的以 Rails 为中心的客户端。
- [thinking-sphinx](https://github.com/pat/thinking-sphinx) - 
[活动记录](https://guides.rubyonrails.org/active_record_basics.html)
用于在（不仅是）基于 Rails 的项目中使用 [Sphinx](http://sphinxsearch.com/) 的插件。
- [elasticsearch](https://github.com/elastic/elasticsearch-ruby/tree/master/elasticsearch) - 
[Elasticsearch](https://www.elastic.co/) 的 Ruby 客户端和 API。
- [elasticsearch-rails](https://github.com/elastic/elasticsearch-rails) - 
[Elasticsearch](https://www.elastic.co/) 的 Ruby 和 Rails 集成。
- [google-api-client](https://github.com/googleapis/google-api-ruby-client) - 
用于 [Google](https://developers.google.com/api-client-library/ruby/) 服务的 Ruby API 库。

## 语言感知字符串操作

用于语言感知字符串操作的库，即搜索、模式匹配、
大小写转换、转码、正则表达式等需要相关信息
底层语言。

- [fuzzy_match](https://github.com/seamusabshere/fuzzy_match) - 
与距离度量和正则表达式的模糊字符串比较。
- [fuzzy-string-match](https://github.com/kiyoka/fuzzy-string-match) - 
Ruby 的模糊字符串匹配库。
- [active_support](https://github.com/rails/rails/tree/master/activesupport/lib/active_support) - 
RoR `ActiveSupport` gem 有各种可以处理大小写的字符串扩展。
- [fuzzy_tools](https://github.com/brianhempel/fuzzy_tools) - 
用于 Ruby 中模糊搜索的工具集，经过调整以提高准确性。
- [u](http://disu.se/software/u-1.0/) - 
U 扩展了 Ruby 的 Unicode 支持。
- [unicode](https://github.com/blackwinter/unicode) - 
Unicode 规范化库。
- [CommonRegexRuby](https://github.com/talyssonoc/CommonRegexRuby) - 
在一个字符串中查找多种常见信息。
- [regexp-examples](https://github.com/tom-lord/regexp-examples) - 
生成与给定正则表达式匹配的字符串。
- [verbal_expressions](https://github.com/ryan-endacott/verbal_expressions) - 
让困难的正则表达式变得简单。
- [translit_kit](https://github.com/AnalyzePlatypus/TranslitKit) - 
将希伯来语和意第绪语文本音译为拉丁字符。
- [re2](https://github.com/mudge/re2) - 
用于文本挖掘和文本提取的高速正则表达式库。
- [regex_sample](https://github.com/mochizukikotaro/regex_sample) - 
从给定的正则表达式生成示例字符串。
- [iuliia](https://github.com/adnikiforov/iuliia-rb) &mdash;
以多种可能的方式将西里尔字母音译为拉丁字母（由[参考实现](https://github.com/nalgeon/iuliia)定义）。

## 文章、帖子、演讲和演示

- 2019
- _使用 Ruby 从图像中提取文本_ 作者：[aonemd](https://twitter.com/aonemd)
    <sup>[[post](https://aonemd.github.io/blog/extracting-text-from-images-using-ruby) |
[代码](https://gist.github.com/aonemd/7bb3c4760d9e47a9ce8e270198cb40a0)]</sup>
- 2018
- [Cassandra Corrales] 的_自然语言处理和推文情感分析_(https://twitter.com/casita305)
    <sup>[[post](https://medium.com/@cmcorrales3/natural-language-processing-and-tweet-sentiment-analysis-fa1edbb5ddd5)]</sup>
- 2017
- _Google NLP API 遇见 Ruby_ 作者：[Aja Hammerly](https://twitter.com/the_thagomizer)
    <sup>[[post](http://www.thagomizer.com/blog/2017/04/13/the-google-nlp-api-meets-ruby.html)]</sup>
- _语法并非一切：NLP For Rubyists_ 作者：[Aja Hammerly](https://twitter.com/the_thagomizer)
    <sup>[[slides](http://www.thagomizer.com/files/NLP_RailsConf2017.pdf)]</sup>
- _JRuby 上的科学计算_ 作者：[Prasun Anand](https://twitter.com/prasun_anand)
    <sup>[[slides](https://www.slideshare.net/PrasunAnand2/fosdem2017-scientific-computing-on-jruby) |
[视频](https://ftp.fau.de/fosdem/2017/K.4.201/ruby_scientific_computing_on_jruby.mp4) |
[幻灯片](https://www.slideshare.net/PrasunAnand2/scientific-computing-on-jruby) |
[幻灯片](https://www.slideshare.net/PrasunAnand2/scientific-computation-on-jruby)]</sup>
- _Ruby 中的 Unicode 标准化_ 作者：[Starr Horne](https://twitter.com/starrhorne)
    <sup>[[post](https://blog.honeybadger.io/ruby_unicode_normalization/)]</sup>
- 2016
- _用 Ruby 快速创建 Telegram 机器人_ 作者：[Ardian Haxha](https://twitter.com/ArdianHaxha)
    <sup>[[tutorial](https://www.sitepoint.com/quickly-create-a-telegram-bot-in-ruby/)]</sup>
- _深度学习：Ruby 开发人员简介_，作者：[Geoffrey Litt](https://twitter.com/geoffreylitt)
    <sup>[[slides](https://speakerdeck.com/geoffreylitt/deep-learning-an-introduction-for-ruby-developers)]</sup>
- _如何将纯 Ruby word2vec 程序速度提高 3 倍以上_ 作者：[Kei Sawada](https://twitter.com/remore)
    <sup>[[slides](https://speakerdeck.com/remore/how-i-made-a-pure-ruby-word2vec-program-more-than-3x-faster)]</sup>
- _Dōmo arigatō，Roboto 先生：使用 Ruby 进行机器学习_ 作者：[Eric Weinstein](https://twitter.com/ericqweinstein)
    <sup>[[slides](https://speakerdeck.com/ericqweinstein/domo-arigato-mr-roboto-machine-learning-with-ruby) | [video](https://www.youtube.com/watch?v=T1nFQ49TyeA)]</sup>
- 2015
- [Jesus Castello] 的_N-gram 分析的乐趣和利润_(https://github.com/matugm)
    <sup>[[tutorial](https://www.rubyguides.com/2015/09/ngram-analysis-ruby/)]</sup>
- [Lorenzo Masini](https://github.com/rugginoso) _用 Ruby 让机器学习变得简单_
    <sup>[[tutorial](https://www.leanpanda.com/blog/2015/08/24/machine-learning-automatic-classification/)]</sup>
- _使用 Ruby 机器学习查找帕丽斯·希尔顿 (Paris Hilton) 名言_ 作者：[Rick Carlino](https://github.com/RickCarlino)
    <sup>[[tutorial](http://web.archive.org/web/20160414072324/http://datamelon.io/blog/2015/using-ruby-machine-learning-id-paris-hilton-quotes.html)]</sup>
- _探索 Ruby 中的自然语言处理_ 作者：[Kevin Dias](https://github.com/diasks2)
    <sup>[[slides](https://www.slideshare.net/diasks2/exploring-natural-language-processing-in-ruby)]</sup>
- _用 Ruby 让机器学习变得简单_ 作者：[Lorenzo Masini](https://twitter.com/rugginoso)
    <sup>[[post](https://www.leanpanda.com/blog/2015/08/24/machine-learning-automatic-classification/)]</sup>
- Bobby Grayson 的《实用 Ruby 数据科学》
    <sup>[[slides](http://slides.com/bobbygrayson/p#/)]</sup>
- 2014
- _用 Ruby 进行自然语言解析_ 作者：[Glauco Custódio](https://github.com/glaucocustodio)
    <sup>[[tutorial](http://glaucocustodio.github.io/2014/11/10/natural-language-parsing-with-ruby/)]</sup>
- _揭秘数据科学：用 Rails 和 Ngram 分析会议演讲_作者：
[托德·施奈德](https://github.com/toddwschneider)
    <sup>[[video](https://www.youtube.com/watch?v=2ZDCxwB29Bg) | [code](https://github.com/Genius/abstractogram)]</sup>
- _用 Ruby 进行自然语言处理_ 作者：[Konstantin Tennhard](https://github.com/t6d)
    <sup>[[video](https://www.youtube.com/watch?v=5u86qVh8r0M) | [video](https://www.youtube.com/watch?v=oFmy_QBQ5DU) |
[视频](https://www.youtube.com/watch?v=sPkeeWnsMn0) |
[幻灯片](http://euruko2013.org/speakers/presentations/natural_language_processing_with_ruby_and_opennlp-tennhard.pdf)]</sup>
- 2013
- _如何解析 'go' - Ruby 中的自然语言处理_ by
[汤姆·卡特赖特](https://twitter.com/tomcartwrightuk)
    <sup>[[slides](https://www.slideshare.net/TomCartwright/natual-language-processing-in-ruby) |
[视频](https://skillsmatter.com/skillscasts/4883-how-to-parse-go)]</sup>
- _Ruby 中的自然语言处理_ 作者：[Brandon Black](https://twitter.com/brandonmblack)
    <sup>[[slides](https://speakerdeck.com/brandonblack/natural-language-processing-in-ruby) |
[视频](http://confreaks.tv/videos/railsconf2013-natural-language-processing-with-ruby)]</sup>
- _Ruby 自然语言处理：n-gram_ 作者：[Nathan Kleyn](https://github.com/nathankleyn)
    <sup>[[tutorial](https://www.sitepoint.com/natural-language-processing-ruby-n-grams/) |
[代码](https://github.com/nathankleyn/ruby-nlp)]</sup>
- _寻找洛夫克拉夫特，第 1 部分：NLP 和 Treat Gem 简介_ 作者：
[罗伯特·奎尔斯](https://github.com/rlqualls)
    <sup>[[tutorial](https://www.sitepoint.com/seeking-lovecraft-part-1-an-introduction-to-nlp-and-the-treat-gem/)]</sup>
- 2012
- _Ruby 机器学习，第一部分_ 作者：[Vasily Vasinov](https://twitter.com/vasinov)
    <sup>[[tutorial](http://www.vasinov.com/blog/machine-learning-with-ruby-part-one/)]</sup>
- 2011
- _Ruby one-liners_ 作者：[Benoit Hamelin](https://twitter.com/benoithamelin)
    <sup>[[post](http://benoithamelin.tumblr.com/ruby1line)]</sup>
- _Ruby 中的聚类_ 作者：[Colin Drake](https://twitter.com/colinfdrake)
    <sup>[[post](https://colindrake.me/post/k-means-clustering-in-ruby/)/)]</sup>
- 2010
- _bayes_motel – Ruby_ 的贝叶斯分类，作者：[Mike Perham](https://twitter.com/mperham)
    <sup>[[post](http://www.mikeperham.com/2010/04/28/bayes_motel-bayesian-classification-for-ruby/)]</sup>
- 2009
- _将 UEA-Lite Stemmer 移植到 Ruby_ 作者：[Jason Adams](https://twitter.com/ealdent)
    <sup>[[post](https://ealdent.wordpress.com/2009/07/16/porting-the-uea-lite-stemmer-to-ruby/)]</sup>
- _Ruby 的 NLP 资源_ 作者：[Jason Adams](https://twitter.com/ealdent)
    <sup>[[post](https://ealdent.wordpress.com/2009/09/13/nlp-resources-for-ruby/)]</sup>
- 2008
- _Ruby 中的支持向量机 (SVM)_ 作者：[Ilya Grigorik](https://twitter.com/igrigorik)
    <sup>[[post](https://www.igvita.com/2008/01/07/support-vector-machines-svm-in-ruby/)]</sup>
- _用 Ruby 进行实用文本分类_ [Gleicon Moraes](https://twitter.com/gleicon)
    <sup>[[post](https://zenmachine.wordpress.com/practical-text-classification-with-ruby/) |
[代码](https://github.com/gleicon/zenmachine)]</sup>
- 2007
- _Ruby 中的决策树学习_ 作者：[Ilya Grigorik](https://twitter.com/igrigorik)
    <sup>[[post](https://www.igvita.com/2007/04/16/decision-tree-learning-in-ruby/)]</sup>
- 2006
- _说我的语言：使用 Ruby 进行自然语言处理_ 作者：[Michael Granger](https://deveiate.org/resume.html)
    <sup>[[slides](https://deveiate.org/misc/Speak-My-Language.pdf) |
[撰写](http://blog.nicksieger.com/articles/2006/10/22/rubyconf-natural-language- Generation-and-processing-in-ruby/) |
[撰写](http://juixe.com/papers/RubyConf2006.pdf)]</sup>

## 项目和代码示例

- [Going the Distance](https://github.com/schneems/going_the_distance) - 
各种距离算法的实现以及示例计算。
- [Named entity recognition with Stanford NER and Ruby](https://github.com/mblongii/ruby-ner) - 
Ruby 和 Java 中的 NER 示例以及一些[说明](https://web.archive.org/web/20120722225402/http://mblongii.com/2012/04/15/named-entity-recognition-with-stanford-ner-and-ruby/)。
- [Words Counted](http://rubywordcount.com/) - 
可定制的单词统计示例
[words_counted](https://github.com/abitdodgy/words_counted)。
- [RSyntaxTree](https://yohasebe.com/rsyntaxtree/) - 
基于网络的语法树可视化演示。

## 书籍

- [米勒，罗布](https://twitter.com/robmil/)。
_使用 Ruby 进行文本处理：从您周围的数据中提取价值。_
务实的程序员，2015 年。
   <sup>[[link](https://www.amazon.com/Text-Processing-Ruby-Extract-Surrounds/dp/1680500708)]</sup>
- [马克·沃森](https://twitter.com/mark_l_watson)。
_脚本智能：Web 3.0 信息收集和处理._
阿普雷斯，2010。
   <sup>[[link](https://www.amazon.de/Scripting-Intelligence-Information-Gathering-Processing/dp/1430223510)]</sup>
- [马克·沃森](https://twitter.com/mark_l_watson)。
_实用语义网和链接数据应用。_ Lulu，2010。
   <sup>[[link](http://www.lulu.com/shop/mark-watson/practical-semantic-web-and-linked-data-applications-java-edition/paperback/product-10915016.html)]</sup>

## 社区

- [Reddit](https://www.reddit.com/r/LanguageTechnology/search?q=ruby&restrict_sr=on)
- [堆栈溢出](https://stackoverflow.com/search?q=%5Bnlp%5D+and+%5Bruby%5D)
- [Twitter](https://twitter.com/search?q=Ruby%20NLP%20%23ruby%20OR%20%23nlproc%20OR%20%23rubynlp%20OR%20%23nlp&src=typd&lang=en)

## 需要您的帮助！

本节中的所有项目对于社区都非常重要，但需要
更多关注。如果您有空闲时间和奉献精神，请花几个小时
关于这里的代码。

- [ferret](https://github.com/dbalmain/ferret) - 
C 和 Ruby 中的信息检索。
- [summarize](https://github.com/ssoper/summarize) - 
[Open Text Summarizer](https://github.com/neopunisher/Open-Text-Summarizer) 的 Ruby 本机包装器。

## 相关资源

- [神经机器翻译实现](https://github.com/jonsafari/nmt-list)
- [Awesome Ruby](https://github.com/markets/awesome-ruby#natural-language-processing) - 
除其他很棒的项目外，还有 NLP 相关项目的简短列表。
- [Ruby NLP](https://github.com/diasks2/ruby-nlp) - 
最先进的 NLP Ruby 库集合。
- [Speech and Natural Language Processing](https://github.com/edobashira/speech-language-processing) - 
NLP 相关资源的一般列表（主要不适合 Ruby 程序员）。
- [Scientific Ruby](http://sciruby.com/) - 
Ruby 的线性代数、可视化和科学计算。
- [iRuby](https://github.com/SciRuby/iruby) - Jupyter 的 IRuby 内核（以前称为 IPython）。
- [Awesome OCR](https://github.com/kba/awesome-ocr) - 
大量 OCR（光学字符识别）资源。
- [Awesome TensorFlow](https://github.com/jtoy/awesome-tensorflow) - 
使用 TensorFlow 库进行机器学习。
- <a name="imagemagic"></a>
[ImageMagick](https://imagemagick.org/index.php)

## 许可证

[![Creative Commons Zero 1.0](http://mirrors.creativecommons.org/presskit/buttons/80x15/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/) `Awesome NLP with Ruby` by [Andrei Beliankou](https://github.com/arbox) and
[贡献者](https://github.com/arbox/nlp-with-ruby/graphs/contributors)。

在法律允许的范围内，将 CC0 与
“Awesome NLP with Ruby”已放弃所有版权和相关或邻接权
到“非常棒的 Ruby NLP”。

您应该已收到 CC0 法律代码的副本以及此文件
工作。如果没有，请参阅 <https://creativecommons.org/publicdomain/zero/1.0/>。

<!--- Links --->
[红宝石]：https://www.ruby-lang.org/en/
[动机]：https://github.com/arbox/nlp-with-ruby/blob/master/motivation.md
[常见问题解答]：https://github.com/arbox/nlp-with-ruby/blob/master/FAQ.md
[ds-with-ruby]：https://github.com/arbox/data-science-with-ruby
[ml-with-ruby]：https://github.com/arbox/machine-learning-with-ruby
[更改-pr]：https://github.com/RichardLitt/knowledge/blob/master/github/amending-a-commit-guide.md
