from flask import Flask, render_template, request, session
from flask import copy_current_request_context

from vsearch import search4letters

from dbcm import UseDatabase, ConnectionsError, CredentialsError, SQLError
from checker import check_logged_in

from threading import Thread
from time import sleep

app = Flask(__name__)

app.config["dbconfig"] = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "vsearch",
    "database": "vsearchlogdb"
}


@app.route("/login")
def do_login() -> str:
    session["logged_in"] = True
    return "You are now logged in"


@app.route("/logout")
@check_logged_in
def do_logout() -> str:
    session.pop("logged_in")
    return "You are now logged out"


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    """Извлекает данные из запроса, выполняет поиск, возвращает результаты"""

    @copy_current_request_context
    def log_request(req: "flask_request", res: str) -> None:
        """Журналирует веб-запрос и возвращает результаты"""
        sleep(15)
        with UseDatabase(app.config["dbconfig"]) as cursor:
            sql = """
                  insert into log (phrase, letters, ip, browser_string, results)
                  values (%s, %s, %s, %s, %s)
                  """
            cursor.execute(sql, (req.form["phrase"], req.form["letters"], req.remote_addr, req.user_agent.browser, res))

    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print("Logging failed with this error:", str(err))

    return render_template("results.html", the_phrase=phrase, the_letters=letters, the_title=title, the_results=results)


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    """"Выводит HTML-форму"""
    return render_template("entry.html", the_title="Welcome to search4letters on the web!")


@app.route("/viewlog")
@check_logged_in
def view_the_log() -> "html":
    """Выводит данные из БД в HTML-таблицы"""
    try:
        with UseDatabase(app.config["dbconfig"]) as cursor:
            sql = """
                  select phrase, letters, ip, browser_string, results
                    from log
                  """
            cursor.execute(sql)
            contents = cursor.fetchall()

        titles = ("Phrase", "Letters", "Remote Address", "User Agent", "Results")
        return render_template("viewlog.html", the_title="View Log", the_row_titles=titles, the_data=contents)
    except ConnectionsError as err:
        print("Is your database switched on? Error:", str(err))
    except CredentialsError as err:
        print("User ID/Password issues. Error:", str(err))
    except SQLError as err:
        print("Is your query correct? Error:", str(err))
    except Exception as err:
        print("Something went wrong:", str(err))
    return "Error"


app.secret_key = "YouWillNeverGuessMySecretKey"

if __name__ == "__main__":
    app.run(debug=True)
