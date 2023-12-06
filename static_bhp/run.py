import sys
import os

project_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append('static_bhp')

from app import app

if __name__ == '__main__':
    app.run(debug=True)
