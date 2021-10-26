from package.configuration import BASE_PATH, BASE_TITLE, DEBUG_MODE

from flask import Flask, render_template
from shutil import copyfile

def flask_template_render(template: str = 'index.html',
    title: str = BASE_TITLE,
    args: dict = {},
    debug: bool = DEBUG_MODE
) -> str:
    copyfile(BASE_PATH + '../../grid.css', BASE_PATH + '../static/css/grid.css')
    return render_template(template,
        title = title,
        args = args,
        debug = debug
    )

app = Flask(__name__)

@app.route('/')
def index():
    return flask_template_render()

if __name__ == '__main__':
    app.run(debug = DEBUG_MODE)
