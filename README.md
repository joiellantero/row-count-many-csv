## Getting Started

> Prerequisite: Python 3 must be installed.

- Download or clone the repository

    ```shell
    git clone https://github.com/joiellantero/row-count-many-csv.git
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

- Run the program

    ```shell
    # command format
    python count-csv.py <filepath>

    # if the folder is in the same directory as count-csv.py...
    python count-csv.py ./myFolder
    ```
