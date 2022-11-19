from createflaskapp import app
from createflaskapp.config import is_dev

if __name__ == '__main__':
    # Change debug=True for local development
    app.run(debug=is_dev, host='0.0.0.0')
