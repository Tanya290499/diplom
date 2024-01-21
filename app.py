""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """

import subprocess
from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route("/run-ui")
def run_ui():
    """Эта функция запускает и отвечает за процесс возврата результата test selenium"""

    cmd = ["./script/selenium.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return out

@app.route("/run-api")
def run_api():
    """Эта функция запускает и отвечает за процесс возврата результата api test"""

    cmd = ["./script/api.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return out

@app.route("/runallure")
def run_allure():
    """ Эта функция запускает и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return out


@app.route("/")
def run():
    """ Эта функция запуская и отвечает за тесты страницы /. """

    cmd = ["./script/api.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
