# SocialMediaAnalysis

![GitHub repo size](https://img.shields.io/github/repo-size/Nazanin-Abbasi/SocialMediaAnalysis)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

This repository includes two projects, SNA 01 and SNA 02. The goal of this project was to analyze a Dataset using graph theories.

## SNA 01

In this project, we first load the dataset, then analyzed it through graph theory.

### Dataset

Here is how we load dataset:

![02](https://user-images.githubusercontent.com/120925422/210345859-db263de7-d14f-47fc-8524-bd97ebd5e685.PNG)

### Degree

We calcualte each node's degree:

![05](https://user-images.githubusercontent.com/120925422/210345970-9e5cc3d4-46b8-4ce7-9e66-6149d300c1c2.PNG)

Here is the degree distribution chart:

![07](https://user-images.githubusercontent.com/120925422/210346046-54087509-363d-413c-8aa7-87d724ba8e03.PNG)

Then we calculate average neighbor degree along with its chart:

![09](https://user-images.githubusercontent.com/120925422/210346138-6f1a70a2-1c48-4829-a6cc-d50e341cfdc0.PNG)
![10](https://user-images.githubusercontent.com/120925422/210346189-f65e1b10-587e-46dd-95e9-0ec54a6325f2.PNG)

Finally, we calculate the average common neighbor along with its chart:

![12](https://user-images.githubusercontent.com/120925422/210346365-2527b53c-25f9-4d62-8d1e-d09d00469140.PNG)
![13](https://user-images.githubusercontent.com/120925422/210346411-d40a4f04-01d5-4c52-a7de-78bfe52c4b29.PNG)

## SNA 02

We first defined a graph on the given dataset. Then we randomly selected 380 nodes and structured a new graph.

Here is the new graph:
![04](https://user-images.githubusercontent.com/120925422/210349139-50af75cb-e1c3-41ca-9fa7-682e1d729b54.PNG)

![03](https://user-images.githubusercontent.com/120925422/210349156-43926c19-1710-47bd-8ee5-600e2a1e4da9.PNG)

Then we extracted 100 important nodes based on Degree Centrality:

![13](https://user-images.githubusercontent.com/120925422/210349325-e031c0b7-2d92-4b9a-8971-d78079cbae09.PNG)

We again created a new sample graph by choosing 380 edges randomely:
 
 ![07](https://user-images.githubusercontent.com/120925422/210349470-8acb4c71-4bdb-4fc1-88db-7d51055a8f67.PNG)
![06](https://user-images.githubusercontent.com/120925422/210349475-765baa57-9bb1-4470-b204-c7d43bc42c74.PNG)

We again defined 100 important nodes based on Degree Centrality:

![15](https://user-images.githubusercontent.com/120925422/210349681-61b42262-86cb-4978-9035-b95128dbbca1.PNG)

We used Random Walk algorithm to sample graph once more:

![08](https://user-images.githubusercontent.com/120925422/210349859-8e55b378-22c2-4f71-85d7-fdd0dccbe542.PNG)
![09](https://user-images.githubusercontent.com/120925422/210349867-434e4321-09dc-4840-a61b-150d21c03361.PNG)

We again defined 100 important nodes based on Degree Centrality:

![17](https://user-images.githubusercontent.com/120925422/210349926-d81f0c51-3e20-414d-bf0d-670ae7e7b728.PNG)

For the last step, we compared 100 important nodes from each graph and found their common nodes:

![11](https://user-images.githubusercontent.com/120925422/210350122-76bdd6ce-4c2c-4002-9df9-0a44756f9153.PNG)



