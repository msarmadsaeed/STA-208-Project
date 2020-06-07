# STA-208-Project

## Deep Reinforcement Learning for Atari games

This repo is based on RL implementation of Atari games using Gym library. We have to aims in this project: (1) comparing different networks and their performance on these games and (2) comparing the parformance of different function approximtors like KNN, Ridge Regression and Tree based learner.

### Group Members

917845196 Ammar Haydari
917779990 Muhammed Sarmad Saeed

We suggest to read the files in this order.

1- [Main project report](https://github.com/msarmadsaeed/STA-208-Project/blob/master/STA_208_Project_Report.pdf) is given in this file.

2- [CartPole](https://github.com/msarmadsaeed/STA-208-Project/tree/master/Cartpole), [Breaokut](https://github.com/msarmadsaeed/STA-208-Project/tree/master/BreakOut) and [Breakout LSTM](https://github.com/msarmadsaeed/STA-208-Project/tree/master/BreakOut%20LSTM) folders have the code and results stored in text file.

Each folder has one single notebook file. Please refer those files for the detailed explanation of codes

## Summary

We studied Q learning based RL algorithms on two atari games namely Cartpole and Breakout. In this project, we employed regression based function approximators (K nearest neightbors, Ridge, XGBoost and Light GBM based gradient boosted tree model) and nonlinear neural network approximators on Cartpole game and image formatted state input structure with CNN and RNN neural networks on breakout game. In the cartpole game, we see that for linear function approximators, batch replay from experience replay memory does not perform well, therefore we change the setting as training the learners with whole memory. However we used batch sampling method on neural network models and this give very good results. The results indicates that, although LightGBM may reach the closest performance to the neural network based model, it is highly time consumed model, Hence, the optimum learning model even in simpler problems is neural network base RL. In the breakout game, we compared two configurations with the besaline models (1) CNN with maxpooling and Adam optimizer and  (2) LSTM model. Our results shows that our first configuration performs the worst while take shortest training time. The second model which uses LSTM aldo do not overerforms the baseline CNN model. LSTM model requires more training time than CNN.




