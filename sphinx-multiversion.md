# 简介
sphinx-multiversion是sphinx的一个扩展，主要用于多版本的控制，效果如下
![avatar][img1]
# 安装
直接使用pip进行安装即可
```bash
pip install sphinx-multiversion
```
# 使用方式
## 前提
1. 需要已经安装sphinx，未安装的话可以执行如下命令进行安装
```bash
pip install sphinx
```
2. 必须基于git仓库
## 操作步骤
1. 设置sphinx扩展
```python
extensions = ["sphinx_multiversion"]
```
2. 设置多版本的模板文件
```python
# 设置模板文件的存放路径
templates_path = ['_templates']
# 设置模板文件
html_sidebars = {
    '**': [
        'versions.html',
    ],
}

```
3. 在`_templates`路径下新建一个名为`versions.html`，示例内容如下:
```html
{%- if current_version %}
<div class="rst-versions" data-toggle="rst-versions" role="note" aria-label="versions">
  <span class="rst-current-version" data-toggle="rst-current-version">
    <span class="fa fa-book"> Other Versions</span>
    v: {{ current_version.name }}
    <span class="fa fa-caret-down"></span>
  </span>
  <div class="rst-other-versions">
    <!-- 显示tag -->
    {%- if versions.tags %}
    <dl>
      <dt>Tags</dt>
      {%- for item in versions.tags %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </dl>
    {%- endif %}
    <!-- 显示分支 -->
    {%- if versions.branches %}
    <dl>
      <dt>Branches</dt>
      {%- for item in versions.branches %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </dl>
    {%- endif %}
    {% if versions.releases %}
    <!-- 显示 release-->
    <dt>{{ _('Releases') }}</dt>
    <dl>
      {%- for item in versions.releases %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </ul>
    {% endif %}
    <!-- 显示 in_development -->
    {% if versions.in_development %}
    <dt>{{ _('In Development') }}</dt>
    <dl>
      {%- for item in versions.in_development %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </ul>
    {% endif %}
  </div>
</div>
{%- endif %}
```
4. 执行sphinx-multiversion命令
```bash
usage: sphinx-multiversion [-h] [-c PATH] [-C] [-D setting=value] [--dump-metadata] sourcedir outputdir [filenames ...]

positional arguments:
  sourcedir         path to documentation source files
  outputdir         path to output directory
  filenames         a list of specific files to rebuild. Ignored if -a is specified

options:
  -h, --help        show this help message and exit
  -c PATH           path where configuration file (conf.py) is located (default: same as SOURCEDIR)
  -C                use no config file at all, only -D options
  -D setting=value  override a setting in configuration file
  --dump-metadata   dump generated metadata and exit
```
- sourcedir: 需要编译生成文档的源文件(包含conf.py的文件夹)。
- outputdir: 编译完生产的html的路径。
- filenames: 需要重新编译的文件，因为默认情况下编译完一次后再次编译会使用之前的缓存。
- -c Path: conf.py文件的路径，默认为`sourcedir`目录。当conf不在`sourcedir`设置的path时，可以使用此参数单独设置conf的属性。
- -C: 不使用conf.py中的配置，直接使用`-D`的参数。
- -D setting=value: 覆盖conf.py中的配置，涉及到的配置主要是与`sphinx-multiversion`模块**不相关**的参数。
- --dump-metadata: 导出元配置信息, 一般是json格式，示例如下:
```json
{
  "1.4": {
    "name": "1.4",
    "version": "",
    "release": "0.1",
    "is_released": true,
    "source": "tags",
    "creatordate": "2022-12-16 20:46:00 +0800",
    "basedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc",
    "sourcedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "outputdir": "D:\\workspace\\sphinx_project\\build\\html\\1.4",
    "confdir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "docnames": [
      "index",
      "resources/\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
      "resources/\u8fed\u4ee3\u5668",
      "resources/index"
    ]
  },
  "develop": {
    "name": "develop",
    "version": "",
    "release": "0.1",
    "is_released": false,
    "source": "heads",
    "creatordate": "2022-12-16 20:46:00 +0800",
    "basedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc",
    "sourcedir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "outputdir": "D:\\workspace\\sphinx_project\\build\\html\\develop",
    "confdir": "C:\\Users\\32621\\AppData\\Local\\Temp\\tmp4_sc3ptu\\0e76ed34331768575e65ce69260bdc0db845aefc\\source",
    "docnames": [
      "index",
      "resources/\u6570\u636e\u7ed3\u6784\u4e0e\u7b97\u6cd5",
      "resources/\u8fed\u4ee3\u5668",
      "resources/index"
    ]
  }
}
```

## 常见配置及含义
```python
# 多版本需要拉取和展示的tag，可通过git tag查看所有tag
smv_tag_whitelist = r'1.4'
# 多版本需要拉取和展示的branch，可通过git branch查看所有分支
smv_branch_whitelist = r"develop"
# 多版本需要拉取和展示的remote，可通过git remote查看所有分支
smv_remote_whitelist = None
# 多版本存在Release时需要展示在Release一栏的tag、branch等
smv_released_pattern = r'refs/tags/*'  
# 设置多版本的最新版本
smv_latest_version = '1.4'
# 默认生成的html的文件夹名称，默认以分支或tag名命名
smv_outputdir_format = r"{ref.name}"
```
```python
# 指定相关元属性配置，可直接根据元属性进行文档生成
smv_metadata = {}
# 指定相关元属性配置的路径，一般是json文件格式
smv_metadata_path = "" 
```
- smv_metadata格式
主要包含git的相关信息, 示例可见上述的`--dump-metadata`中的配置信息, 需要注意的是metadata中的路径问题，自动生成的都是临时文件，不过一般直接使用上述的组合配置即可，不需要自己手动指定内容。
```python
metadata[gitref.name] = {
    "name": gitref.name,
    "version": current_config.version,
    "release": current_config.release,
    "is_released": bool(
        re.match(config.smv_released_pattern, gitref.refname)
    ),
    "source": gitref.source,
    "creatordate": gitref.creatordate.strftime(sphinx.DATE_FMT),
    "basedir": repopath,
    "sourcedir": current_sourcedir,
    "outputdir": os.path.join(
        os.path.abspath(args.outputdir), outputdir
    ),
    "confdir": confpath,
    "docnames": list(project.discover()),
}
```
# 原理
1. 读取指定的`sourcedir`中的`conf.py中的sphinx-multiversion相关配置`，详细可见上方常见配置和含义。
2. 依据配置中的branch和tag等信息，创建临时目录git拉取所需的branch和tag等。
3. 使用sphinx的命令生成对应的html文档，不同branch或tag存放于不同的文件夹下。

# 更简单的操作方式
`sphinx-multiversion`插件需要两个元素:
- 需要拉取的repo/git，即执行命令所在路径必须存在git环境(.git文件夹)
- 需要在`sourcedir`中存在`conf.py`文件且conf配置中需包含`sphinx-multiversion`的配置即可。
由上述两个元素可以得出`sphinx-multiversion`最简单的执行环境如下:
```‘
│ .git
└─source
    │  conf.py 
    └─_templates
            versions.html
```
- .git: 多版本所需的git环境，即需要拉取的branch、tag所在的环境。
- source: 源文件路径，一般为conf.py所在路径
- _templates: 存放多版本所需的模板文件
- conf.py: 配置文件,sphinx的conf.py，需包含`sphinx-multiversion`配置，详细可见上述配置和含义
- versions.html: 多版本模板文件
```html
{%- if current_version %}
<div class="rst-versions" data-toggle="rst-versions" role="note" aria-label="versions">
  <span class="rst-current-version" data-toggle="rst-current-version">
    <span class="fa fa-book"> Other Versions</span>
    v: {{ current_version.name }}
    <span class="fa fa-caret-down"></span>
  </span>
  <div class="rst-other-versions">
    <!-- 显示tag -->
    {%- if versions.tags %}
    <dl>
      <dt>Tags</dt>
      {%- for item in versions.tags %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </dl>
    {%- endif %}
    <!-- 显示分支 -->
    {%- if versions.branches %}
    <dl>
      <dt>Branches</dt>
      {%- for item in versions.branches %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </dl>
    {%- endif %}
    {% if versions.releases %}
    <!-- 显示release -->
    <dt>{{ _('Releases') }}</dt>
    <dl>
      {%- for item in versions.releases %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </ul>
    {% endif %}
    <!-- 显示in_development -->
    {% if versions.in_development %}
    <dt>{{ _('In Development') }}</dt>
    <dl>
      {%- for item in versions.in_development %}
      <dd><a href="{{ item.url }}">{{ item.name }}</a></dd>
      {%- endfor %}
    </ul>
    {% endif %}
  </div>
</div>
{%- endif %}
```

# 注意事项
1. 关于release中如何显示分支或tag?示意图如下:
![avatar][img2]

使用`smv_released_pattern`配置去控制是否在`Releases`中显示,如与此配置相匹配则放在`Releases`中，否则放在`in_development`中。
需要注意的是`smv_released_pattern`配置中匹配的是`refname`，不是直接的分支或者`tag`名称，可通过下述代码在git环境下执行获取
```python
import subprocess


def get_all_refs(gitroot):
    cmd = (
        "git",
        "for-each-ref",
        "--format",
        "%(objectname)\t%(refname)\t%(creatordate:iso)",
        "refs",
    )
    output = subprocess.check_output(cmd, cwd=gitroot).decode()
    print(f"output:{output}")

# 包含.git的文件夹
git_root = ""


get_all_refs(git_root)

```
执行效果如下:
```
daa326dc6529e4ace1322a3ce359fcd978929dbc refs/heads/develop      2022-12-17 17:21:44 +0800        
e571a3b958bb3c6b829b973149c2f119774c0ecd        refs/heads/main 2022-12-16 19:53:00 +0800
e571a3b958bb3c6b829b973149c2f119774c0ecd        refs/remotes/origin/HEAD        2022-12-16 19:53:00 +0800
daa326dc6529e4ace1322a3ce359fcd978929dbc        refs/remotes/origin/develop     2022-12-17 17:21:44 +0800
e571a3b958bb3c6b829b973149c2f119774c0ecd        refs/remotes/origin/main        2022-12-16 19:53:00 +0800
9a93e7ab36e2a37cf862f692c3e24914e14f5d26        refs/remotes/origin/master      2022-11-17 16:18:45 +0800
0e76ed34331768575e65ce69260bdc0db845aefc        refs/tags/1.4   2022-12-16 20:46:00 +0800
```
其中的格式为refs/*均为`refname`。
例如需要将`refs/tags/1.4`显示在Releases中，直接设置`smv_released_pattern="refs/tags/1.4"`即可

2. 如何添加自定义的属性，类似于Releases、Branchs等，例如添加一个Testing？
需修改`sphinx-multiversion`源码, windows一般是位于
`python3.*\Lib\site-packages\sphinx_multiversion`,修改内容如下:
main.py
```python
metadata[gitref.name] = {
  "name": gitref.name,
  "version": current_config.version,
  "release": current_config.release,
  "is_released": bool(
      re.match(config.smv_released_pattern, gitref.refname)
  ),
  "source": gitref.source,
  "creatordate": gitref.creatordate.strftime(sphinx.DATE_FMT),
  "basedir": repopath,
  "sourcedir": current_sourcedir,
  "outputdir": os.path.join(os.path.abspath(args.outputdir), outputdir),
  "confdir": confpath,
  "docnames": list(project.discover()),
  # 添加内容
  "is_testing": bool(
      re.match(config.smv_testing_whitelist, gitref.refname)
  ),
}

***
current_config.add(
    "smv_released_pattern",
    sphinx.DEFAULT_RELEASED_PATTERN,
    "html",
    str,
)
current_config.add(
    "smv_outputdir_format",
    sphinx.DEFAULT_OUTPUTDIR_FORMAT,
    "html",
    str,
)
# 添加内容
current_config.add(
    "smv_testing_whitelist", sphinx.DEFAULT_TEST_WHITELIST, "html", str
)
```
sphinx.py
```python
***
@property
def releases(self):
    return [
        self._dict_to_versionobj(v)
        for v in self.metadata.values()
        if v["is_released"]
    ]

@property
def in_development(self):
    return [
        self._dict_to_versionobj(v)
        for v in self.metadata.values()
        if not v["is_released"]
    ]

# 添加内容
@property
def tests(self):
    return [
        self._dict_to_versionobj(v)
        for v in self.metadata.values()
        if v["is_testing"]
    ]

***
app.add_config_value("smv_branch_whitelist", DEFAULT_BRANCH_WHITELIST, "html")
app.add_config_value("smv_remote_whitelist", DEFAULT_REMOTE_WHITELIST, "html")
app.add_config_value("smv_released_pattern", DEFAULT_RELEASED_PATTERN, "html")
app.add_config_value("smv_outputdir_format", DEFAULT_OUTPUTDIR_FORMAT, "html")
# 添加内容
app.add_config_value("smv_testing_whitelist", DEFAULT_TEST_WHITELIST, "html")
```
修改完上述源码后，`sphinx-multiversion`的配置多了一个`smv_testing_whitelist`，此配置和`smv_released_pattern`类似，都是refsname，不直接是分支名。

[img1]:data:image/jpeg;base64,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

[img2]:data:image/jpeg;base64,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