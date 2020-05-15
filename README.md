
# Visual Search Engine

> The Visual Seach Engine allows to find visually similar images in the dataset.





***Example : Top 5 similar watches***

[![INSERT YOUR GRAPHIC HERE](Figure_1.png)]()

## Table of Contents 

- [Installation](#installation)
- [Features](#features)

---

## Installation

- The is a guide how to run my application, it assumes you have Python and pip installed. 

### Clone

- Clone this repo to your local machine using `https://github.com/danilredko/VisualSearchEngine.git`

### Dataset

- download the dataset using `https://www.kaggle.com/paramaggarwal/fashion-product-images-small`
- rename the dataset folder to `dataset`
- place `dataset` into `VisualSeachEngine`

### Setup

- Install the requirments.txt: 

> 

```shell
$ pip install -r requirements.txt
```

> Run this command to build index

```shell
$ python src/compute_index.py
```
>Run this command `help` to see the optins:
```shell
$python src/find_most_similar.py -h
```
>Run this command to display top `k` similar image to the one you want, example:
```shell
$python src/find_most_similar.py -img 10000.jpg -k 5
```

---

### Docker
>To build a docker image

```shell
$ docker build --tag visual-search-engine
```
>To run a docker image

```shell
$ docker run -it visual-search-engine 
```

### Project Structure
```bash
├── src                          #source files of the project
│   ├── model                    #model files 
│   ├── compute_index.py         #compute index file used for command line interface
│   ├── find_most_similar.py     #main file of the project, runs the whole application
├── data                         #dir for project files such as extracted features
├── dataset                      #dataset for this project
├── config.json                  #json file that contains all the config for the project
├── Dockerfile                   #docker file needed for a docker image
├── requirments.txt              #all the dependencies needed to run this project
├── README.md                    #info about the project
└── .gitignore                   #ignore some dirs for git
```

