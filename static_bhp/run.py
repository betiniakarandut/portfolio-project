import sys
import os

project_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_dir)

from app import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)
