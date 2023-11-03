## Getting Started

> Prerequisite: Python 3 must be installed.

- Download or clone the repository
  
    ```shell
    git clone https://github.com/joiellantero/name-roulette.git
    ```

- Navigate to the directory of the project.
- Create a virtual environment.

    ```shell
    virtualenv env
    ```

- Activate the virtual environment.

    > for macOS and linux

    ```shell
    source env/bin/activate
    ```

    > for windows

    ```shell
    Scripts/activate.bat
    ```

- Install the dependencies

    ```shell
    pip install -r requirements.txt
    ```

- Run the program

    > Format: `python3 name-roulette.py <fileName> <amount> <flags>`

    ```shell
    python3 name-roulette.py names.csv 3 --cowsay
    ```