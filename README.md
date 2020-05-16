
# Visual Search Engine

> The Visual Seach Engine allows to find visually similar images in the dataset.





***Example : Top 5 similar watches***

[![INSERT YOUR GRAPHIC HERE](Figure_1.png)]()

## Table of Contents 
- [Main goal](# Main goal of the project)
- [Installation](#installation)
- [Features](#features)

---
## Main goal of the project
- E-commerce is a big industry, people less go to the shopping malls, people start to shop online more. As marketing shows people tend to buy an item based on its visual components. Thus, pictures of the products are really important for successful e-commerce bussiness. 
The main goal of this project is to show a user visual similar items based on the item he/she is looking at the moment. This project creates a back-end where you can feed a current product image a user is interested in, and provide him/her visually similar items. It increases the chances of buying. This project uses mobile net v2 to extract the features of images, and computes how similar the images are based on extracted features (however, config file provides an option to change a model depending on your needs). 
## Installation

- The is a guide how to run my application, it assumes you have Python and pip installed. 

### Clone

- Clone this repo to your local machine using `https://github.com/danilredko/VisualSearchEngine.git`

### Dataset

- download the dataset using `https://www.kaggle.com/paramaggarwal/fashion-product-images-small`
- rename the dataset folder to `dataset`
- place `dataset` into `VisualSeachEngine`


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




