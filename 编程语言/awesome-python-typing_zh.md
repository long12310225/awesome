# 很棒的 Python 打字 [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

很棒的 Python 类型、存根、插件和使用它们的工具的集合。

## 内容

- [静态类型检查器](#static-type-checkers)
- [动态类型检查器](#dynamic-type-checkers)
- [存根包](#stub-packages)
- [附加类型](#additional-types)
- [向后移植和改进](#backports-and-improvements)
- [Tools](#tools)
- [Integrations](#integrations)
- [Articles](#articles)
- [Related](#related)

[PyPi 上类型化项目的完整列表](https://pypi.org/search/?q=&o=&c=Typing+%3A%3A+Typed) 位于此处。

## 静态类型检查器

- [basedmypy](https://github.com/KotlinIsland/basedmypy) - 基于静态类型和基线功能。
- [basedpyright](https://github.com/detachhead/basedpyright) - Pyright 分支改进了 VSCode 支持并进行了各种其他修复。
- [mypy](https://github.com/python/mypy) - 可选的静态类型 (PEP 484)。
- [pyanalyze](https://github.com/quora/pyanalyze) - 可扩展的静态分析器和类型检查器。
- [PyCharm](https://www.jetbrains.com/pycharm/) - 面向专业开发人员的 IDE。
- [pylyzer](https://github.com/mtshiba/pylyzer/) - 一个用于 Python 的快速静态代码分析器和语言服务器，用 Rust 编写。
- [pyrefly](https://github.com/facebook/pyrefly) - Python 的快速类型检查器和语言服务器。
- [pyright](https://github.com/Microsoft/pyright) - 快速类型检查器适用于大型 Python 源代码库。它可以在“监视”模式下运行，并在文件修改时执行快速增量更新。
- [pycroscope](https://github.com/JelleZijlstra/pycroscope) - Python 代码的半静态类型检查器。它导入它类型检查的模块，使“pycroscope”能够理解其他类型检查器将拒绝的许多动态结构。这使得可以使用直接与代码交互的插件来扩展“pycroscope”。
- [pytype](https://github.com/google/pytype) - 检查和推断类型的工具 - 无需类型注释。
- [ty](https://github.com/astral-sh/ty) - 一个非常快的 Python 类型检查器，由 Ruff 和 uv 的创建者用 Rust 编写。
- [zuban](https://github.com/zubanls/zuban) - 用 Rust 构建的与 Mypy 兼容的 Python 类型检查器和语言服务器。

## 动态类型检查器

- [beartype](https://github.com/beartype/beartype) - 纯 Python 中难以忍受的快速“O(1)”运行时类型检查。
- [pydantic](https://github.com/samuelcolvin/pydantic) - 使用 Python 类型提示进行数据解析。支持数据类。
- [pytypes](https://github.com/Stewori/pytypes) - 提供了一组丰富的用于运行时类型检查的实用程序。
- [strongtyping](https://github.com/FelixTheC/strongtyping) - 装饰器检查函数是否使用正确类型的参数调用。
- [typedpy](https://github.com/loyada/typedpy) - 类型安全、严格的 Python。与标准 Python 配合良好。
- [typeguard](https://github.com/agronholm/typeguard) - 另一种运行时类型检查器。
- [typical](https://github.com/seandstewart/typical/) - 使用类型提示的数据解析和自动类型强制。支持数据类、标准类、函数签名等。
- [trycast](https://github.com/davidfstr/trycast) - 解析类似 JSON 的值，其形状由类型化字典 (TypedDicts) 和其他标准 Python 类型提示定义。

## 存根包

- [asgiref](https://github.com/django/asgiref) - ASGI 规范，为 ASGI 服务器提供带有类型注释的 [asgiref.typing](https://github.com/django/asgiref/blob/main/asgiref/typing.py) 模块。
- [boto3-stubs](https://vemel.github.io/boto3_stubs_docs/) - [boto3](https://github.com/boto/boto3) 的存根。
- [botostubs](https://github.com/jeshan/botostubs) - 为您提供任何 IDE 中任何 boto3 API 的代码帮助。
- [celery-types](https://github.com/sbdchd/celery-types) - [Celery](https://github.com/celery/celery) 及其相关包的类型存根 [django-celery-results](https://github.com/celery/django-celery-results)、[ampq](https://github.com/celery/py-amqp)、[kombu](https://github.com/celery/kombu)、 [台球](https://github.com/celery/billiard)、[vine](https://github.com/celery/vine) 和 [ephem](https://github.com/brandon-rhodes/pyephem)。
- [django-stubs](https://github.com/typeddjango/django-stubs) - [Django](https://github.com/django/django) 的存根。
- [djangorestframework-stubs](https://github.com/typeddjango/djangorestframework-stubs) - [DRF](https://github.com/encode/django-rest-framework) 的存根。
- [grpc-stubs](https://github.com/shabbyrobe/grpc-stubs) - [grpc](https://github.com/grpc/grpc) 的存根。
- [lxml-stubs](https://github.com/lxml/lxml-stubs) - [lxml](https://lxml.de) 的存根。
- [PyQt5-stubs](https://github.com/stlehmann/PyQt5-stubs) - [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro) 的存根。
- [python-phonenumbers-stubs](https://github.com/AA-Turner/python-phonenumbers-stubs) - [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) 的存根。
- [pythonista-stubs](https://github.com/hbmartin/pythonista-stubs) - [Pythonista](http://omz-software.com/pythonista/docs/ios/) 的存根。
- [scipy-stubs](https://github.com/jorenham/scipy-stubs) - [SciPy](https://github.com/scipy/scipy) 的存根。
- [sqlalchemy-stubs](https://github.com/dropbox/sqlalchemy-stubs) - [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) 的存根。
- [sqlalchemy2-stubs](https://docs.sqlalchemy.org/en/14/orm/extensions/mypy.html) - [SQLAlchemy](https://www.sqlalchemy.org) 的官方存根和 mypy 插件。
- [torchtyping](https://github.com/patrick-kidger/torchtyping) - [PyTorch](https://pytorch.org/) 的增强类型注释。
- [types-aiobotocore](https://vemel.github.io/types_aiobotocore_docs/) - [aiobotocore](https://github.com/aio-libs/aiobotocore) 的存根。
- [typeshed](https://github.com/python/typeshed) - 具有静态类型的库存根集合。

## 附加类型

- [meiga](https://github.com/alice-biometrics/meiga) - 简单、类型化和基于 monad 的结果类型。
- [option](https://github.com/MaT1g3R/option) - Rust 类似 Option 和 Result 类型。
- [optype](https://github.com/jorenham/optype) - 自以为是的“collections.abc”和“operators”替代方案：灵活的单一方法协议和具有可预测名称的类型化运算符。
- [phantom-types](https://github.com/antonagestam/phantom-types) - 幻影类型。
- [returns](https://github.com/dry-python/returns) - 让你的函数返回一些有意义的、有类型的、安全的东西。
- [safetywrap](https://github.com/mplanchard/safetywrap) - 完全类型安全、类似 Rust 的结果和选项类型。
- [typet](https://github.com/contains-io/typet) - 长度限制类型，动态对象验证。
- [useful-types](https://github.com/hauntsaninja/useful_types) - 有用的协议和类型别名的集合。

## 向后移植和改进

- [future-typing](https://github.com/PrettyWood/future-typing) - 将标准集合和联合类型中的类型提示泛型向后移植为“X |” Y`。
- [typing-extensions](https://github.com/python/typing_extensions) - 向后移植和实验类型提示。
- [typing-utils](https://github.com/bojiang/typing_utils) - 向后移植 3.8+ 运行时输入实用程序（例如：get_origin）并添加 issubtype 等。

## 工具

### 短绒棉

- [flake8-annotations-complexity](https://github.com/best-doctor/flake8-annotations-complexity) - flake8 的插件，用于验证注释的复杂性。
- [flake8-annotations](https://github.com/sco1/flake8-annotations) - flake8 的插件，用于检查函数定义中是否存在类型注释。
- [flake8-pyi](https://github.com/ambv/flake8-pyi) - Flake8 插件，提供类型提示存根文件的专业化。
- [flake8-type-checking](https://github.com/snok/flake8-type-checking) - 插件可帮助您正确保护任何仅类型注释的导入。
- [flake8-typing-imports](https://github.com/asottile/flake8-typing-imports) - 检查输入导入是否受到适当保护的插件。
- [flake8-typing-only-imports](https://github.com/sondrelg/flake8-typing-only-imports) - flake8 插件可帮助识别将哪些导入放入类型检查块中，以及在导入移动后如何调整类型注释。
- [flake8-type-ignore](https://gitlab.com/jonafato/flake8-type-ignore/) - flake8 插件禁止输入：忽略输入的 Python 代码中的注释。
- [wemake-python-styleguide](https://github.com/wemake-services/wemake-python-styleguide) - 有史以来最严格、最固执己见的 Python linter。
- [Ruff](https://github.com/astral-sh/ruff/) - 极快的 linter，支持许多其他 lint 工具（例如 flake8）的 lint 规则。

### 测试

- [mypy-test](https://github.com/orsinium-labs/mypy-test) - 测试 mypy 插件、存根、自定义类型。
- [pytest-mypy-plugins](https://github.com/typeddjango/pytest-mypy-plugins) - Pytest 插件，用于测试 mypy 类型、存根和插件。
- [pytest-mypy-testing](https://github.com/davidfritzsche/pytest-mypy-testing) - Pytest 插件用于测试 mypy 静态类型分析。
- [pytest-mypy](https://github.com/dbader/pytest-mypy) - Pytest 的 Mypy 静态类型检查器插件。

### 使用类型

- [com2ann](https://github.com/ilevkivskyi/com2ann) - 用于将类型注释转换为类型注释的工具。
- [merge-pyi](https://github.com/google/pytype/tree/master/pytype/tools/merge_pyi) - pytype 工具链的一部分，将存根文件应用到源代码上。
- [mypy-baseline](https://github.com/orsinium-labs/mypy-baseline) - 将 mypy 与现有代码库集成。一种 CLI 工具，可过滤掉现有类型错误并仅报告新错误。
- [mypy-protobuf](https://github.com/dropbox/mypy-protobuf) - 从 protobuf 生成 mypy 存根的工具。
- [mypy-silent](https://github.com/whtsky/mypy-silent/) - 通过添加或删除代码注释来使 mypy 静音。
- [mypyc](https://github.com/python/mypy/tree/master/mypyc) - 将带 mypy 注释的静态类型 Python 模块编译为 CPython C 扩展。
- [retype](https://github.com/ambv/retype) - 将存根应用于代码的另一个工具。
- [typeforce](https://github.com/orsinium-labs/typeforce) - CLI 工具，通过类型注释丰富您的 Python 环境，为 mypy 提供支持。
- [typesplainer](https://github.com/wasi-master/typesplainer) - Python 类型解释器。
- [typing-inspect](https://github.com/ilevkivskyi/typing_inspect) - Typing_inspect 模块定义了实验性 API，用于运行时检查“typing”模块中定义的类型。
- [typing-json](https://pypi.org/project/typing-json/) - 用于处理类型化对象和 JSON 的库。

### 用于向现有代码添加注释的辅助工具

- [autotyping](https://github.com/JelleZijlstra/autotyping) - 自动为函数添加简单的返回类型注释（bool、None、Optional）。
- [infer-types](https://github.com/orsinium-labs/infer-types) - CLI 工具自动推断类型注释并将其添加到 Python 代码中。
- [jsonschema-gentypes](https://github.com/camptocamp/jsonschema-gentypes) - 根据 JSON 模式中的 TypedDict 生成 Python 类型。
- [monkeytype](https://github.com/instagram/MonkeyType) - 收集函数参数和返回值的运行时类型，并可以根据运行时收集的类型自动生成存根文件，甚至直接将草稿类型注释添加到代码中。
- [no_implicit_optional](https://github.com/hauntsaninja/no_implicit_optional) - 使隐式可选类型提示符合 [PEP 484](https://peps.python.org/pep-0484/#union-types) 的 codemod。
- [pyannotate](https://github.com/dropbox/pyannotate) - 根据运行时观察到的调用参数和返回类型将注释插入到源代码中。
- [PyTypes](https://github.com/pvs-hd-tea/PyTypes) - 通过 Python 跟踪推断类型。
- [pytest-annotate](https://github.com/kensho-technologies/pytest-annotate) - 用于 pytest 的 Pyannotate 插件。
- [pytest-monkeytype](https://github.com/mariusvniekerk/pytest-monkeytype) - 用于 pytest 的 MonkeyType 插件。
- [pytype annotate-ast](https://github.com/google/pytype/tree/master/pytype/tools/annotate_ast) - 一个正在开发的工具，用于使用 Python 类型注释 AST 的节点。
- [RightTyper](https://github.com/RightTyper/RightTyper) - 为函数参数和返回值生成类型的工具。 RightTyper 让您的代码几乎全速运行，几乎没有内存开销。
- [auto-optional](https://github.com/Luttik/auto-optional) - 当默认参数为“None”时，使类型参数可选。

### Mypy 插件

- [kubernetes-typed](https://github.com/gordonbondon/kubernetes-typed) - 用于 Kubernetes [CRD](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) 类型检查的插件。
- [loguru-mypy](https://github.com/kornicameister/loguru-mypy) - 用于 [loguru](https://github.com/Delgan/loguru) 支持的插件。
- [mypy-zope](https://github.com/Shoobx/mypy-zope) - 用于 [zope.interface](https://zopeinterface.readthedocs.io/en/latest/) 支持的插件。
- [mypy/plugins](https://github.com/python/mypy/tree/master/mypy/plugins) - 插件已集成到 mypy 中。
- [NumPy](https://numpy.org/devdocs/reference/typing.html) - 用于 [NumPy](https://numpy.org) 支持的插件。
- [pynamodb-mypy](https://github.com/pynamodb/pynamodb-mypy) - [PynamoDB](https://github.com/pynamodb/PynamoDB) 支持插件。
- [pydantic](https://docs.pydantic.dev/latest/integrations/mypy/) - 用于额外 [Pydantic](https://docs.pydantic.dev/latest/) 支持的插件。

## 集成

- [emacs-flycheck-mypy](https://github.com/lbolla/emacs-flycheck-mypy) - Emacs 的 Mypy 集成。
- [mypy-playground](https://github.com/ymyzk/mypy-playground) - mypy 的在线游乐场。
- [mypy-pycharm-plugin](https://github.com/dropbox/mypy-PyCharm-plugin) - PyCharm 的 Mypy 集成。
- [pylance](https://github.com/microsoft/pylance-release) - VSCode 的 PyRight 集成。
- [vim-mypy](https://github.com/Integralist/vim-mypy) - Vim 的 Mypy 集成。
- [nbQA](https://github.com/nbQA-dev/nbQA) - 在 Jupyter Notebook 上运行类型检查器（例如 Mypy）。

## 文章

### 政治公众人物

- [PEP-3107](https://www.python.org/dev/peps/pep-3107) - 函数注释。
- [PEP-482](https://www.python.org/dev/peps/pep-0482/) - 类型提示的文献概述。
- [PEP-483](https://www.python.org/dev/peps/pep-0483/) - 类型提示理论。
- [PEP-484](https://www.python.org/dev/peps/pep-0484/) - 类型提示。
- [PEP-526](https://www.python.org/dev/peps/pep-0526/) - 变量注释的语法。
- [PEP-544](https://www.python.org/dev/peps/pep-0544/) - 协议：结构子类型（静态鸭子类型）。
- [PEP-557](https://www.python.org/dev/peps/pep-0557/) - 数据类。
- [PEP-560](https://www.python.org/dev/peps/pep-0560/) - 对类型模块和泛型类型的核心支持。
- [PEP-561](https://www.python.org/dev/peps/pep-0561/) - 分发和包装类型信息。
- [PEP-563](https://www.python.org/dev/peps/pep-0563/) - 推迟对注释的评估。
- [PEP-585](https://www.python.org/dev/peps/pep-0585/) - 标准集合中的类型提示泛型。
- [PEP-586](https://www.python.org/dev/peps/pep-0586/) - 文字类型。
- [PEP-589](https://www.python.org/dev/peps/pep-0589/) - TypedDict：具有固定键集的字典的类型提示。
- [PEP-591](https://www.python.org/dev/peps/pep-0591/) - 为打字添加最终限定符。
- [PEP-593](https://www.python.org/dev/peps/pep-0593/) - 灵活的函数和变量注释。
- [PEP-604](https://www.python.org/dev/peps/pep-0604/) - Union[] 的补充语法。
- [PEP-612](https://www.python.org/dev/peps/pep-0612/) - 参数规范变量。
- [PEP-613](https://www.python.org/dev/peps/pep-0613/) - 显式类型别名。

### 第三方文章

- [1-minute guide to real constants in Python](https://sobolevn.me/2018/07/real-python-contants) - 关于“Final”常量和继承的完整教程。
- [Simple dependent types in Python](https://sobolevn.me/2019/01/simple-dependent-types-in-python) - 关于“Literal”类型的完整教程。
- [Testing mypy stubs, plugins, and types](https://sobolevn.me/2019/08/testing-mypy-types) - 关于测试 mypy 类型的完整教程。
- [Our journey to type checking 4 million lines of Python](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python) - Dropbox 是首批采用这种规模的 Python 静态类型检查的公司之一。
- [PyTest MonkeyType Introduction](https://dev.to/ldrscke/type-annotate-an-existing-python-django-codebase-with-monkeytype-254i) - 类型 使用 MonkeyType 注释现有的 Python Django 代码库。
- [The state of type hints in Python](https://bernat.tech/posts/the-state-of-type-hints-in-python/) - 截至 2018 年 5 月。
- [Type hints cheat sheet](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html) - MyPy 团队编写类型注释的备忘单。
- [Typechecking Django and DRF](https://sobolevn.me/2019/08/typechecking-django-and-drf) - 关于 Django 类型检查的完整教程。
- [Type Check Your Django Application](https://kracekumar.com/post/type_check_your_django_app/) - 这篇文章基于最近两次有关向 Django 添加类型检查的讨论。
- [typing](https://docs.python.org/3/library/typing.html) - “typing”模块的官方 Python 文档。
- [Python-typing-koans](https://github.com/kracekumar/python-typing-koans/) - 一组用于学习 Python 中可选静态类型的示例。
- [Python Type Checking (Guide)](https://realpython.com/python-type-checking/) - 在本指南中，您将了解 Python 类型检查。
- [Adding type hints to urllib3](https://sethmlarson.dev/blog/2021-10-18/tests-arent-enough-case-study-after-adding-types-to-urllib3) - 测试还不够：案例研究向 urllib3 添加类型提示。
- [Adam Johnsons Blog](https://adamj.eu/tech/tag/mypy/) - Adam Johnson 撰写了有关打字练习的博客。
- [ParamSpec Guide](https://sobolevn.me/2021/12/paramspec-guide) - “PEP612”中新发布的功能允许您使用函数及其签名执行许多高级输入操作。
- [Static Typing Python Decorators](https://rednafi.github.io/reflections/static-typing-python-decorators.html) - Python 中准确的静态类型装饰器是一件棘手的事情。包装函数混淆静态确定包装函数的参数类型和返回值所需的类型信息。
- [How do mypy, Pyright, and ty compare?](https://pydevtools.com/handbook/explanation/how-do-mypy-pyright-and-ty-compare/) - 三个主要 Python 静态类型检查器的详细比较，涵盖功能、性能和权衡。
- [ty: A Complete Guide](https://pydevtools.com/handbook/explanation/ty-complete-guide/) - ty 的综合指南，来自 Astral 的快速 Python 类型检查器。

## 相关

- [awesome-python](https://github.com/vinta/awesome-python) - 精彩的 Python 框架、库、软件和资源的精选列表。
- [Python Developer Tooling Handbook](https://pydevtools.com/) - 全面的手册，涵盖 Python 类型检查器、linter 和开发工具，以及 [mypy](https://pydevtools.com/handbook/reference/mypy/)、[Pyright](https://pydevtools.com/handbook/reference/pyright/) 和 [ty](https://pydevtools.com/handbook/reference/ty/) 的参考页。
- [python-typecheckers](https://github.com/ethanhs/python-typecheckers) - Python 类型检查器列表：静态和运行时。
