import os
import glob
from pathlib import Path


def rm_docs_dir(basedir, path):
    return os.path.normpath(path.replace(basedir, '')).lstrip('/')


# TODO not represents depth in result list.
# needs to parse depth and add indent
def format_link(basedir, file):
    rel = rm_docs_dir(basedir, file)
    title = f"{rel.replace('.md', '').replace('_', ' ').title()}"
    title = get_title(file)
    target = rel
    return f"- [{title}]({target}) / {target}"


def toc_block(toctree_content):
    return f"Table of Contents:\n\n{toctree_content}"


def get_title(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('# '):
                return line[2:].strip()
        return os.path.basename(md_file).replace('.md', '').replace('_', ' ').title()


def get_md_files_depth(directory, depth):
    pattern = f"{'*/' * (depth - 1)}*.md"
    result = sorted(glob.glob(os.path.join(directory, pattern)))
    if depth < 2:
        return result
    else:
        return sorted(result + get_md_files_depth(directory, depth - 1))


def get_md_files_recursive(directory):
    return sorted(glob.glob(os.path.join(directory, "**/*.md"), recursive=True))


def get_md_files(directory, depth=None):
    files = get_md_files_recursive(
        directory) if depth is None else get_md_files_depth(directory, depth)
    return sorted([str(file) for file in files])


def get_md_files_without_index(directory, depth=None):
    return [file for file in get_md_files(directory, depth) if not file.endswith('index.md')]


def are_paths_related(parent_path, child_path):
    parent = Path(parent_path).resolve()
    child = Path(child_path).resolve()
    return child.is_relative_to(parent)


def define_env(env):
    """
    This is the hook for the functions (new form)
    """

    def docs_dir():
        return env.conf.docs_dir

    def _normpath(dir):
        join = os.path.join(docs_dir(), current_dir(), dir)
        normpath = os.path.normpath(join)
        return normpath

    def is_safe(dir):
        normpath = _normpath(dir)
        in_children = are_paths_related(docs_dir(), normpath)
        return in_children

    def current_dir():
        # return os.path.dirname(os.path.dirname(env.page.url))
        return os.path.dirname(env.page.url)

    def current_fullpath():
        return os.path.join(docs_dir(), current_dir())

    @env.macro
    def listfiles(dir='.', depth=None):
        if not is_safe(dir):
            return ''
        directory = _normpath(dir)
        files = [
            docs_dir(),
            current_dir(),
            current_fullpath(),
            "vvvvv"
        ]
        files += get_md_files_without_index(directory, depth)
        return "\n  - ".join(files)

    @env.macro
    def toctree(dir='.', depth=None):
        if not is_safe(dir):
            return ''
        directory = _normpath(dir)
        files = get_md_files_without_index(directory, depth)
        # print(files)
        toctree = [format_link(current_fullpath(), file)
                   for file in files]
        toctree_content = "\n".join(toctree)
        return toc_block(toctree_content)

    @env.macro
    def test(dir='.'):
        join = os.path.join(docs_dir(), dir)
        normpath = os.path.normpath(join)
        in_children = are_paths_related(docs_dir(), normpath)
        r = [
            "    - docs_dir: " + docs_dir(),
            "    - dir: " + dir,
            "    - join: " + join,
            "    - normpath: " + normpath,
            "    - in_children: " + ('true' if in_children else 'false'),
            "    - current_dir: " + current_dir()
        ]
        return "\n".join(r)
