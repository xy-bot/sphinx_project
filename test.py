from pathlib import Path
import re


def replace_index(resource_path, resource_path2):
    if not isinstance(resource_path, Path):
        resource_path = Path(resource_path)
    if not isinstance(resource_path2, Path):
        resource_path2 = Path(resource_path2)
    BUFF_SIZE = 1024 * 1024

    with open(resource_path2, "r", encoding="utf8") as r_f, open(
        resource_path, "r+", encoding="utf8"
    ) as r_f2:
        content = r_f.read(BUFF_SIZE)
        ret = re.findall(
            f'<section id="{resource_path2.stem}">(.*?)</section>',
            content,
            re.S,
        )
        print(ret)
        sub_content = re.sub(
            f'<section id="{resource_path.stem}">(.*?)</section>',
            ret[0],
            r_f2.read(BUFF_SIZE),
            count=1,
            flags=re.S,
        )
        r_f2.seek(0)
        r_f2.write(sub_content)
        r_f2.truncate()
    # resource_path2.unlink()


resource_path2 = r"D:\workspace\sphinx_project\build\html\resources\resource.html"

resource_path = r"D:\workspace\sphinx_project\build\html\resources\resources.html"

replace_index(resource_path, resource_path2)
