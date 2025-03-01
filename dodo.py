import yaml, pathlib        

def task_build_docs():
    return dict(
        actions=[
            "jb build --toc qww/toc.yml --config qww/config.yml .",
            "touch _build/html/.nojekyll"
        ],
        targets=["_build/html/index.html"]
    )