import os
import sys
import webbrowser
import threading
from app import create_app, db

# This function ensures proper paths inside PyInstaller bundle
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # used by PyInstaller
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Update template & static folder paths for PyInstaller
template_dir = resource_path('templates')
static_dir = resource_path('app/static')

# Pass template/static paths to Flask app
app = create_app(template_folder=template_dir, static_folder=static_dir)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1, open_browser).start()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
