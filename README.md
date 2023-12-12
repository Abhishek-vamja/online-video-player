# online-video-player
The Online Video Player is a web application built to provide users with a seamless and immersive experience in exploring and watching a variety of videos. The platform includes features such as category-based navigation, search functionality, and detailed video information.

## SETUP

Ensure you have the following prerequisites installed:

1. **Python**
2. **Pip**
3. **Virtualenv:**

   Install Virtualenv in your system:

   ```bash
   python3 -m pip install --upgrade pip
   python3 -m pip install virtualenv

4. **Verify the installation:**

    ```bash
    virtualenv --version

5. **Make New Directory:**

    ```bash
    mkdir directory_name

    # Now Change Directory
    cd directory_name

6. **Create Virtual Environment:**

    ```bash
    virtualenv env

7. **Activate Virtual Environment:**

        # For Linux/macOS
        source env/bin/activate

        # For Windows:
        .\env\Scripts\activate

8. **Clone Project:**

    ```bash
    git clone https://github.com/Abhishek-vamja/Fruits-Shop.git

9. **Install All Requirements:**

    ```bash
    pip install -r requirements.txt

10. **Change Directories:**

    - [your_directory]
        - [online-video-player]
            - [video_player]

11. **Apply Migrations:**
 
    ```bash
    python manage.py makemigrations

    python manage.py migrate

12. **Create Admin:**

    ```bash
    python manage.py createsuperuser

13. **Run Server:**

    ```bash
    python manage.py runserver
