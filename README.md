# regression-model-using-scikit-learn
In this assignment, you will experiment and write a report on building regression models. Unlike the ordinary regression model that predicts the value of a dependent variable from a collection of independent variables, you will study the logistic regression that can be used for classification. The python library scikit-learn exposes an API that can accomplish this task easily. You will study the API (see documentation at https://scikit-learn.org/stable/modules/generated/sklearn .linear model.LogisticRegression.html) to gain insight on the various parameters. A set of book chapters (from G ́eron (2019)) has been put together to help you with modifying the codes in scikit-learn documentation to complete the task in this assignment. The chapter “End-to-End Machine Learning Project” is particularly helpful in preparing data ((G ́eron, 2019, chp.2)). Chapter 4, “Training Models” is useful in building various regression models ((G ́eron, 2019, Ch. 4)).
The dataset (https://archive.ics.uci.edu/dataset/942/rt-iot2022) for this assignment can be imported into your code as follows (Do not forget to install the ucimlrepo package in your environment):
from ucimlrepo import fetch_ucirepo # fetch dataset
rt_iot2022 = fetch_ucirepo(id=942) # data (as pandas dataframes)
X = rt_iot2022.data.features
y = rt_iot2022.data.targets
# The next lines of code are only informative/diagnostic
print(rt_iot2022.metadata) # this allows you to see the dataset metadata print(rt_iot2022.variables) # allows you to see the variables
1

Sharmila and Nagapadma (2023) generated a real-time internet-of-things (IOT) dataset (Sharmila & Nagapadma, 2024) for normal and attack traffic. An intrusion detection method based on a quantized autoencoder was proposed and tested on the dataset. In this assignment the focus is not on the method the authors proposed. Rather, we are interested in developing a series of binary classifier models that can detect normal and attack traffic based on the features in the dataset. The logistic regression is a regression model suitable for binary classification. As a regression model it can also be used with regularization including ridge, Lasso, and elastic-net to obtain different effect on the weight vector and classification accuracy. Your task is to experiment with these regularizations and report on your findings. Additionally, you will use the principal component analysis (PCA) to reduce the dimension of the features and generate a logistic regression classifier model based on the reduced number of features. Note that you are to experiment with the number of features to retain.
What needs to be done or considered
1. Read the excerpts from the book by G ́eron (2019) provided with this specification. You do not need to read the whole excerpt. Skim through first and the focus on what is relevant for this assignment. It has to be emphasised that for those who do not know how to start writing code for this assignment, this excerpt provides ample sample codes to get you started. Use the codes freely and customize them for the task at hand.
2. Understand (visualize/investigate) the dataset using information from Chapter 2. You will report on your finding. While there may be no missing data, this dataset may exhibit other effects. Investigate and report on what you find as well as how you deal with it.
3. You will report on the best accuracy obtained with each of your models:
• No regularization
• L2 regularization (ridge)
• L1 regularization (Lasso)
• L1-L2 regularization (elastic-net) • PCA dimensionality reduction
Study the documentation of the scikit-learn logistic regression API and build your models using scikit-learn. Report on your results for each norm and explain why the results might be different. Did you notice any difference in the importance of the independent variables? You will also notice the choice of solvers available in the API. Explore them and report on any difference in the results.
4. Study the documentation of the scikit-learn PCA dimensionality reduction API. Build a logistic regression model using the reduced features obtained and report on the best accuracy you are able to obtain.
2

5. Write a report according to the template provided. You MUST follow the template in setting out your sections. You can have subsections tailored to your presentation style, but the sec- tion headings MUST not be changed. A LaTeX template has been provided along with this specification. Your report MUST not be more than 5 pages of text, figures and tables. This excludes the title page and references.
6. Your report must cite at least 3 sources (journal or conference or books) to support the theory section. You must cite the source of the dataset (already provided).
7. Your report must include graphical outputs. However, you need to be judicious in your choice of the plots that you include. Remember that every graphical plot must have a label and caption, and must be described in the text of your report. Otherwise you will lose substantial marks.
8. It is possible that you will use jupyter notebook to develop your code. Please note that you cannot submit a notebook file for this assignment. Only a python source code can be submitted (i.e. a .py file).
9. If your source code does not work or emits error messages, your code will not be debugged or fixed. Your report will be marked out of 50% of the total marks for this assignment.
What needs to be submitted
• You will prepare a “zip” or “rar” file containing your report (5-page text plus title and references pages as PDF file) and Python code (named : logistic_regression_intrusion.py) file.
• Your code must be executable as a Python version 3.10 (or higher) code and run from command line as:
            python logistic_regression_intrusion.py
and write results indicating that your code works (e.g. classification accuracy for each method) to standard output (stdout).
• Submit the “zip” or “rar” via Moodle dropbox provided on or before the deadline. References
G ́eron, A. (2019). Hands-on machine learning with scikit-learn, keras &and tensorflow: Concepts, tools, and techniques to build intelligent systems (2nd ed.). CA, USA: O’Reilly Media, Inc.
Sharmila, B., & Nagapadma, R. (2023). Quantized autoencoder (QAE) intrusion detection system for anomaly detection in resource-constrained IoT devices using RT-IoT2022 dataset. Cyber- security, 6(41(2023)), 1-15.
Sharmila, B., & Nagapadma, R. (2024). RT-IoT2022 . UCI Machine Learning Repository. (DOI: https://doi.org/10.24432/C5P338)
3
