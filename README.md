
# Visual Search Engine

> The Visual Seach Engine allows to find visually similar images in the dataset.





***Example : Top 5 similar watches***

[![INSERT YOUR GRAPHIC HERE](Figure_1.png)]()

## Table of Contents 
- [Main goal](#main-goal)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Similarity Computation](#similarity-computation)
- [Features](#features)
- [How it works](#how-it-works)
- [System Requirements](#system-requirements)

---
## Main goal
- E-commerce is a big industry, people less go to the shopping malls, people start to shop online more. As marketing shows people tend to buy an item based on its visual components. Thus, pictures of the products are really important for successful e-commerce businesses. 
The main goal of this project is to show a user visually similar items based on the item he/she is looking at the moment. This project creates a back-end where you can feed a current product image a user is interested in, and provide him/her visually similar items. It increases the chances of buying. This project uses mobile-net-v2 to extract the features of images and computes how similar the images are based on extracted features (however, the config file provides an option to change a model depending on your needs).

## Installation

- The is a guide how to run my application, it assumes you have Python and pip installed. 

### Clone

- Clone this repo to your local machine using `https://github.com/danilredko/VisualSearchEngine.git`

### Dataset

- download the dataset using `https://www.kaggle.com/paramaggarwal/fashion-product-images-small`
- unzip rename the dataset folder to `dataset`
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

The behavior of each class and function are expained in depth in the doc strings. 

### Setup

- Install the requirments.txt: 

> 

```shell
$ pip install -r requirements.txt
```

> Run this command to build index

```shell
$ python src/compute_and_save_features.py
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

### Similarity Computation

- As a human user can say that images are similar or not, however since visual similarity is not a mathematical term, we need a way to compute this similarity. Since the dataset contains metadata about each image we can use cosine similarity to compute similarity using only non-visual features(called similarity on the final plot). This way we have cosine similarity of image features to compute visual similarity, as well as non-visual similarity. The focus of this project is a visual similarity, thus we sort the results by visual similarity based on extracted image features. The non-visual similarity is an additional metric that could be used if we trained our model.

### Features
- This application allows a user pass an image from a dataset and a number how many sinmilar images user wants to get. The app outplot a plot of top k images, where the first one is an original image, and the rest are the most similar images in the dataset to the original image.

### How it works
- First, we extract the features form each image using mobile net v2(the model can be changed in the config). Then using faiss library(Faiss is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python (versions 2 and 3). Some of the most useful algorithms are implemented on the GPU) we compute similarities for each image. Then we can access it using indecies. Main choice of using this library is bacause it is fast. GPU can be used during implementation. Then we save extracted features and filenames for future use. Once we have the features, we can use the application. Application builds index and find top 5 images requested by a user. 

### System Requirements

This application has been tested on linux 18.04 LTS.
```bash
$lshw
ubuntu                      
    description: Computer
    width: 64 bits
    capabilities: smp vsyscall32
  *-core
       description: Motherboard
       physical id: 0
     *-memory
          description: System memory
          physical id: 0
          size: 11GiB
     *-cpu:0
          product: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz
          vendor: Intel Corp.
          physical id: 1
          bus info: cpu@0
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp x86-64 constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xsaves arat md_clear flush_l1d arch_capabilities
     *-cpu:1
          product: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz
          vendor: Intel Corp.
          physical id: 2
          bus info: cpu@1
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp x86-64 constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xsaves arat md_clear flush_l1d arch_capabilities
     *-cpu:2
          product: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz
          vendor: Intel Corp.
          physical id: 3
          bus info: cpu@2
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp x86-64 constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xsaves arat md_clear flush_l1d arch_capabilities
     *-cpu:3
          product: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz
          vendor: Intel Corp.
          physical id: 4
          bus info: cpu@3
          width: 64 bits
          capabilities: fpu fpu_exception wp vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp x86-64 constant_tsc arch_perfmon nopl xtopology tsc_reliable nonstop_tsc cpuid pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xsaves arat md_clear flush_l1d arch_capabilities

```

```bash
$ python src/find_most_similar.py -img 24953.jpg -k 4
```
Show top 4 similar images to the given image: Time -  0.40841955298674293
```bash
$ python src/find_most_similar.py -img 24953.jpg -k 40
```
Show top 4 similar images to the given image: Time -  0.940446972992504


### Ways to improve 
- There are a lot of ways to improve. First, model can be retrained for this specific task. Since now, we only extract the features from the images, but the model is not trained for this specific task. Model can be retrained for fashion items. Next, there is a better way of managing extracted features. They can be saved to a file, storted in cache while application is running. We could keep track how often each image is used and store its similar images in cache. Docker can be improved to support GUI. In this set up we only print similar images. However, we could make docker image support matpotlib to show the resulted images. 

### Final Thoughts

I enjoyed the process of developing this project. It makes me excited how it can be used in e-commerce business. Visual aspect is very important for E-commerce. Thank you, `the Fitting Room` and `Advait` for this experience!
