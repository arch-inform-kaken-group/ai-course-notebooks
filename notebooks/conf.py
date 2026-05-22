project = "AI Course Notebooks"
author = "arch-inform-kaken-group"

extensions = [
    "myst_nb",
    "sphinx_copybutton",
]

exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "OLD_*",
]

# 既存 notebook の出力:off  ビルド時に再実行: "force" , "cache" 
nb_execution_mode = "off"

html_theme = "sphinx_book_theme"

html_theme_options = {
    "repository_url": "https://github.com/arch-inform-kaken-group/ai-course-notebooks",
    "repository_branch": "main",
    "path_to_docs": "notebooks",

    # 右上ボタン
    "use_repository_button": True,
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_download_button": True,

    # Colab 起動
    "launch_buttons": {
        "colab_url": "https://colab.research.google.com",
        "notebook_interface": "jupyterlab",
    },
}

html_context = {
    "default_mode": "light",
}

def setup(app):
    app.add_js_file("https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js")

html_static_path = ["_static"]
html_css_files = ["custom.css"]

nb_mime_priority_overrides = [
    ("html", "application/vnd.plotly.v1+json", None),
    ("html", "application/javascript", None),
]
