from department_app import app
from department_app.populate import Populate


if __name__ == "__main__":
    Populate.populate()
    app.run()
    