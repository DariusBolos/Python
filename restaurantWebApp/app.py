from controller.config import app
from controller.routes import home, menu, order

if __name__ == "__main__":
    app.run(debug=True, port=8000)
