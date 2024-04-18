# InstructABSA: Instruction learning for Aspect Based Sentiment Classification


## Introduction

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/instructabsa-instruction-learning-for-aspect/aspect-extraction-on-semeval-2014-task-4-sub-2)](https://paperswithcode.com/sota/aspect-extraction-on-semeval-2014-task-4-sub-2?p=instructabsa-instruction-learning-for-aspect)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/instructabsa-instruction-learning-for-aspect/aspect-extraction-on-semeval-2014-task-4-sub-1)](https://paperswithcode.com/sota/aspect-extraction-on-semeval-2014-task-4-sub-1?p=instructabsa-instruction-learning-for-aspect)

[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/instructabsa-instruction-learning-for-aspect/sentiment-analysis-on-semeval-2014-task-4)](https://paperswithcode.com/sota/sentiment-analysis-on-semeval-2014-task-4?p=instructabsa-instruction-learning-for-aspect)

This repository is the official implementation of the [paper](https://arxiv.org/abs/2302.08624). As part of our approach we show the efficacy of instruction tuned language models. This approach surpasses previous SOTA on downstream ABSA subtasks by significant margin.


## Model Checkpoints

All the model weights can be found [here](https://huggingface.co/kevinscaria). The best performing models for each ABSA subtask based on our experiments are presented in the table below:
| Task  | Model Name | Dataset Trained | Model Type | Instruction Configuration |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| ATE| kevinscaria/ate_tk-instruct-base-def-pos-neg-neut-combined | SemEval 2014 Laptops + Restaurants | InstructABSA-2 | Definition + 2 pos + 2 neg + 2 neut examples |
| ATSC| kevinscaria/atsc_tk-instruct-base-def-pos-combined | SemEval 2014 Laptops + Restaurants | InstructABSA-1 | Definition + 2 pos examples |
| Joint Task| kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined | SemEval 2014 Laptops + Restaurants | InstructABSA-2 | Definition + 2 pos + 2 neg + 2 neut examples |

### A sample inference notebook is found [here](https://github.com/kevinscaria/InstructABSA/blob/main/inference_notebook.ipynb).

## Aspect Term Extraction

The ATE models can be trained from scratch or alternatively can be used to run inference on your datasets directly. This can be done through CLI (check the [Scripts](https://github.com/kevinscaria/InstructABSA/tree/main/Scripts) folder) or by adapting your code similar to run_model.py. An example shell command to run inference on individual samples is shown below.

A sample notebook for training and evluating ATE can be found [here](https://github.com/kevinscaria/InstructABSA/blob/main/ATE_Training_&_Inference.ipynb).

## Joint Tasks

The Joint task models can be trained from scratch or alternatively can be used to run inference on your datasets directly. This can be done through CLI (check the [Scripts](https://github.com/kevinscaria/InstructABSA/tree/main/Scripts) folder) or by adapting your code similar to run_model.py. An example shell command to run inference on individual samples is shown below.

A sample notebook for training and evluating Joint Task can be found [here](https://github.com/kevinscaria/InstructABSA/blob/main/JointTask_Training_&_Inference.ipynb).

To evaluate the Joint Task on a single input using CLI run the following:
```shell
python run_model.py -mode cli -task joint \
-model_checkpoint kevinscaria/joint_tk-instruct-base-def-pos-neg-neut-combined \
-test_input <input_file_path>
```
## Aspect Based Opinion Extraction ⬆️

## Aspect Opinion Pair Extraction ⬆️

## Aspect Opinion Sentiment Triplet Extraction ⬆️

## BibTeX Entry and Citation Info

If you find our work useful, please cite our work: 

```bibtex
article{scaria2023instructabsa,
  title={InstructABSA: Instruction Learning for Aspect Based Sentiment Analysis},
  author={Scaria, Kevin and Gupta, Himanshu and Sawant, Saurabh Arjun and Mishra, Swaroop and Baral, Chitta},
  journal={arXiv preprint arXiv:2302.08624},
  year={2023}
}
```
