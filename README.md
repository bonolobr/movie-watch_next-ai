# Movie Watch Next AI Program

## Table of Contents

1. [Project Description](#project_description)
2. [Installation](#installation) 
3. [Usage](#usage)
4. [Credit and Contribution](#credit_and_contribution)
5. [License](#license)

## Project Description <a name="project_description"><a>
The purpose of this program is to recommend the movie title that the user should watch next, based on the similarity to the movie they have just watched.
It makes a suggestion from a list of movies available in a file.

The program makes this suggestion of what to watch next based on word vector similarity of the description of the available movies to the movie watched.

## Installation <a name="installation"><a> 

There are two different ways to run the program: using Docker or a virtual environment.

### Docker

You can either use docker on your desktop or by using Docker Playground. Descriptions for using both options are included.

**Run container using Desktop**

1. If you don't already have Docker installed on your desktop, install Docker on your desktop.

2. Once installed, enter the following command in the terminal:

```
docker run -i bonolor/movie-watch_next-ai
```

**Run container using Docker Playground**

1. Go to Docker Playground at the following link and enter "Start": https://labs.play-with-docker.com/.

2. Add a new instance.
  
3. Enter the following command in the terminal:

```
docker run -i bonolor/movie-watch_next-ai
```

### Virtual Environment

1. Download the followiing files in the repository.

2. Create a project folder named "watch_next".
 
3. Move and save the downloaded files to the watch_next folder.
  
4. Open your local Integrated Development Environment (IDE) such as VSCode.
 
5. Add the watch_next folder to your IDE.
 
6. In the same parent directory, create a virtual environment named .venv by entering the following command in the terminal (use relevant python version):
   
  ```
  python3.11 -m venv .venv
  ```
  
7. Activate the virtual environment using the following command (for macOS):
  
  ```
  source .venv/bin/activate
  ```
  
8. Once the virtual environment is created and activated, enter the following command to move into the garden_ai directory (if you are not already in the directory):
  
  ```
  cd watch_next
  ```
 
9. Run the requirements.txt file to install all the relevant packages:
  
  ```
  pip install -r requirements.txt
  ```
  
10. If prompted to upgrade pip, enter:

  ```
  pip install --upgrade pip
  ```

11. Install language model:

  ```
  python -m spacy download en_core_web_md

  ```
  
  _Note: Check to ensure that the virtual environment has been activated_

12. Select watch_next.py and run the program.

## Usage <a name="usage"><a>

Movie description of movie just watched:

<img width="1140" alt="Screenshot 2023-05-05 at 00 15 56" src="https://user-images.githubusercontent.com/127111801/236341325-3d59b049-bc2e-4208-a2ce-f380f7686c2f.png">

Available movies the program analyses to find the most similar to the movie just watched:

<img width="1140" alt="Screenshot 2023-05-05 at 00 11 31" src="https://user-images.githubusercontent.com/127111801/236340718-51623084-092a-4d7b-b6a5-8767ef2e23fb.png">

Output recommended movie to watch next:

<img width="772" alt="Screenshot 2023-05-05 at 00 09 12" src="https://user-images.githubusercontent.com/127111801/236340416-e2566144-24a6-4cae-b2ba-404559f40e5f.png">

## Credit and Contribution <a name="credit_and_contribution"><a> 

This program has been developed by Bonolo Ramasedi.

## License <a name="license"><a> 
  
This project is not licensed and is intended for display purposes only. All rights reserved. No usage, distribution, or modification rights are granted.
