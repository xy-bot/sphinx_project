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
需要已经安装sphinx，未安装的话可以执行如下命令进行安装
```bash
pip install sphinx
```
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

[img1]:data:image/jpeg;base64,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
