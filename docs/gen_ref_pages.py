"""Auto-generate Reference pages from source code docstrings.

Executed by the mkdocs-gen-files plugin at build time.
Walks the `source/` directory (cloned by CI from the project's source repo),
creates one .md file per Python module under docs/reference/, and builds a
SUMMARY.md for literate-nav to consume.
"""

from pathlib import Path

import mkdocs_gen_files

src_root = Path("source")
ref_root = Path("reference")

nav = mkdocs_gen_files.Nav()

for path in sorted(src_root.rglob("*.py")):
    # Skip hidden files, test files, and setup scripts
    if any(part.startswith(("_", "test_", "setup", "conf")) for part in path.parts):
        continue

    module_path = path.relative_to(src_root).with_suffix("")
    doc_path = path.relative_to(src_root).with_suffix(".md")
    full_doc_path = ref_root / doc_path

    parts = tuple(module_path.parts)

    if parts[-1] == "__init__":
        parts = parts[:-1]
        doc_path = doc_path.with_name("index.md")
        full_doc_path = ref_root / doc_path
    elif parts[-1].startswith("_"):
        continue

    if not parts:
        continue

    nav[parts] = doc_path.as_posix()

    with mkdocs_gen_files.open(full_doc_path, "w") as fd:
        ident = ".".join(parts)
        fd.write(f"# `{parts[-1]}`\n\n::: {ident}\n")

    mkdocs_gen_files.set_edit_path(full_doc_path, path)

with mkdocs_gen_files.open(ref_root / "SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
