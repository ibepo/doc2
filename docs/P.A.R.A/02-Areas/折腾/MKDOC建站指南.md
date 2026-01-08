## material theme
### 特性
 features:
    - navigation.expand 展开全部侧边栏
    - navigation.indexes
    - navigation.sections 侧边栏大标题
    - navigation.tabs 头部导航
     - navigation.tabs.sticky 向上滑动本主题滑动
    - navigation.instant
    - navigation.tracking
    - navigation.path
    - toc.follow
    - header.autohide

mkdocs.yml
``` yml
site_name: BPWiki
theme:
  name: material
  shortcuts:
    help: 191 # ?
    next: 78 # n
    previous: 80 # p
    search: 83 # s
  palette:
    primary: white
  language: zh
  logo: assets/lemons.png
  favicon: assets/favicon.ico
  features:
    # - navigation.expand
    - navigation.indexes
    # - navigation.sections
    - navigation.tabs
    # - navigation.tabs.sticky
    - navigation.instant
    - navigation.tracking
    - navigation.path
    - toc.follow
    - header.autohide
markdown_extensions:
  - tables
  - attr_list
  - pymdownx.tabbed
  - nl2br
  - toc:
      permalink: '#'
      slugify: !!python/name:pymdownx.slugs.uslugify # 解决中文标题解析问题
  - admonition
  # - codehilite:
  #     guess_lang: false
  #     linenums: false
  - footnotes
  - meta
  - def_list
  - pymdownx.arithmatex
  - pymdownx.betterem:
      smart_enable: all
  #MkDocs 的材料支持多个 HTML 元素，这些元素可用于突出显示文档的各个部分或应用特定格式。 此外，还支持 Critic Markup，增加了显示文档更改建议的功能。
  - pymdownx.critic
  - pymdownx.caret
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.tilde
  - pymdownx.details
  - pymdownx.inlinehilite
  - pymdownx.magiclink
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tasklist
plugins:
  - search
  - roamlinks
  - exclude:
      glob:
        - '*.tmp'
        - '*.pdf'
        - '*.gz'
      regex:
        - '.*\.(tmp|bin|tar)$'
``` 

## reference
[Mkdoc document](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/)
[Material theme document](https://squidfunk.github.io/mkdocs-material/setup/changing-the-logo-and-icons/)
