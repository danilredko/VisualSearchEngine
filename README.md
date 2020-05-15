
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

## Features

- Going into more detail on code and technologies used
- I utilized this nifty <a href="https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet" target="_blank">Markdown Cheatsheet</a> for this sample `README`.


