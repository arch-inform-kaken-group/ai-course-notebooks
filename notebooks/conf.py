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

    # 右上ボタン類
    "use_repository_button": True,
    "use_source_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_download_button": True,

    # Colab 起動ボタン
    "launch_buttons": {
        "colab_url": "https://colab.research.google.com",
        "notebook_interface": "jupyterlab",
    },
}

html_js_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js",
]

html_context = {
    "default_mode": "light",
}
