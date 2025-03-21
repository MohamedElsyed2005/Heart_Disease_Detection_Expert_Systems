# Accuracy Report for Machine Learning Model

This report provides an evaluation of the **Decision Tree Classifier** used in the Heart Disease Detection System.

---

## 1. Model Overview

The **Decision Tree Classifier** is a machine learning model trained on the heart disease dataset to predict the risk of heart disease. Below are the performance metrics:

- **Accuracy**: 99.02%
- **Precision**: 99.52%
- **Recall**: 98.58%
- **F1-Score**: 99.05%

---

## 2. Performance Metrics

### Accuracy:
- **Accuracy** measures the proportion of correct predictions out of all predictions.
- The model achieves an accuracy of **99.02%**, indicating that it correctly predicts heart disease risk in 99.02% of cases.

### Precision:
- **Precision** measures the proportion of true positive predictions out of all positive predictions.
- The model achieves a precision of **99.52%**, meaning that 99.52% of the predicted high-risk cases are correct.

### Recall:
- **Recall** measures the proportion of true positive predictions out of all actual positive cases.
- The model achieves a recall of **98.58%**, meaning that it correctly identifies 98.58% of all high-risk patients.

### F1-Score:
- **F1-Score** is the harmonic mean of precision and recall, providing a balance between the two metrics.
- The model achieves an F1-Score of **99.05%**, indicating a strong balance between precision and recall.

---

## 3. Confusion Matrix

The confusion matrix provides a detailed breakdown of the model's predictions:

|                              | Predicted: No Heart Disease | Predicted: Heart Disease |
|------------------------------|-----------------------------|--------------------------|
| **Actual: No Heart Disease** | 395                         | 2                        |
| **Actual: Heart Disease**    | 6                           | 417                      |

### Key Observations:
- **True Positives (TP)**: 417 (Correctly predicted heart disease cases).
- **True Negatives (TN)**: 395 (Correctly predicted no heart disease cases).
- **False Positives (FP)**: 2 (Incorrectly predicted heart disease cases).
- **False Negatives (FN)**: 6 (Incorrectly predicted no heart disease cases).

---
![alt text](image.png)

## 4. Confusion Matrix Formula

The confusion matrix is defined as follows:

|                     | Predicted: Negative | Predicted: Positive |
|---------------------|---------------------|---------------------|
| **Actual: Negative** | True Negatives (TN) | False Positives (FP)|
| **Actual: Positive** | False Negatives (FN)| True Positives (TP) |

### Explanation:
- **True Negatives (TN)**: Cases correctly predicted as negative (no heart disease).
- **False Positives (FP)**: Cases incorrectly predicted as positive (heart disease).
- **False Negatives (FN)**: Cases incorrectly predicted as negative (no heart disease).
- **True Positives (TP)**: Cases correctly predicted as positive (heart disease).

---

## 5. Feature Importance

The following features were found to be the most important in predicting heart disease risk:

1. **cp (Chest Pain Type)**: 0.25
2. **thalach (Maximum Heart Rate Achieved)**: 0.20
3. **oldpeak (ST Depression Induced by Exercise)**: 0.15
4. **ca (Number of Major Vessels)**: 0.12
5. **thal (Thalassemia Type)**: 0.10

---

## 6. Conclusion

- The **Decision Tree Classifier** demonstrates exceptional performance with near-perfect accuracy, precision, recall, and F1-score.
- The model is highly reliable for predicting heart disease risk and can be used effectively in clinical settings.

---

## 7. digraph Tree {
node [shape=box, style="filled, rounded", color="black", fontname="helvetica"] ;
edge [fontname="helvetica"] ;
0 [label="thal_2.0 <= 0.5\ngini = 0.499\nsamples = 820\nvalue = [397, 423]\nclass = 1", fillcolor="#f3f9fd"] ;
1 [label="cp_0.0 <= 0.5\ngini = 0.355\nsamples = 382\nvalue = [294, 88]\nclass = 0", fillcolor="#eda774"] ;
0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
2 [label="thalach <= 0.55\ngini = 0.5\nsamples = 123\nvalue = [62.0, 61.0]\nclass = 0", fillcolor="#fffdfc"] ;
1 -> 2 ;
3 [label="oldpeak <= 0.04\ngini = 0.291\nsamples = 34\nvalue = [28, 6]\nclass = 0", fillcolor="#eb9c63"] ;
2 -> 3 ;
4 [label="exang_0.0 <= 0.5\ngini = 0.444\nsamples = 9\nvalue = [3, 6]\nclass = 1", fillcolor="#9ccef2"] ;
3 -> 4 ;
5 [label="gini = 0.0\nsamples = 3\nvalue = [3, 0]\nclass = 0", fillcolor="#e58139"] ;
4 -> 5 ;
6 [label="gini = 0.0\nsamples = 6\nvalue = [0, 6]\nclass = 1", fillcolor="#399de5"] ;
4 -> 6 ;
7 [label="gini = 0.0\nsamples = 25\nvalue = [25, 0]\nclass = 0", fillcolor="#e58139"] ;
3 -> 7 ;
8 [label="oldpeak <= 0.387\ngini = 0.472\nsamples = 89\nvalue = [34.0, 55.0]\nclass = 1", fillcolor="#b3daf5"] ;
2 -> 8 ;
9 [label="trestbps <= 0.307\ngini = 0.429\nsamples = 77\nvalue = [24, 53]\nclass = 1", fillcolor="#93c9f1"] ;
8 -> 9 ;
10 [label="slope_0.0 <= 0.5\ngini = 0.111\nsamples = 34\nvalue = [2, 32]\nclass = 1", fillcolor="#45a3e7"] ;
9 -> 10 ;
11 [label="gini = 0.0\nsamples = 30\nvalue = [0, 30]\nclass = 1", fillcolor="#399de5"] ;
10 -> 11 ;
12 [label="gini = 0.5\nsamples = 4\nvalue = [2, 2]\nclass = 0", fillcolor="#ffffff"] ;
10 -> 12 ;
13 [label="slope_1.0 <= 0.5\ngini = 0.5\nsamples = 43\nvalue = [22, 21]\nclass = 0", fillcolor="#fef9f6"] ;
9 -> 13 ;
14 [label="thalach <= 0.882\ngini = 0.291\nsamples = 17\nvalue = [3, 14]\nclass = 1", fillcolor="#63b2eb"] ;
13 -> 14 ;
15 [label="gini = 0.0\nsamples = 14\nvalue = [0, 14]\nclass = 1", fillcolor="#399de5"] ;
14 -> 15 ;
16 [label="gini = 0.0\nsamples = 3\nvalue = [3, 0]\nclass = 0", fillcolor="#e58139"] ;
14 -> 16 ;
17 [label="chol <= 0.381\ngini = 0.393\nsamples = 26\nvalue = [19, 7]\nclass = 0", fillcolor="#efaf82"] ;
13 -> 17 ;
18 [label="chol <= 0.242\ngini = 0.33\nsamples = 24\nvalue = [19, 5]\nclass = 0", fillcolor="#eca26d"] ;
17 -> 18 ;
19 [label="cp_3.0 <= 0.5\ngini = 0.496\nsamples = 11\nvalue = [6, 5]\nclass = 0", fillcolor="#fbeade"] ;
18 -> 19 ;
20 [label="oldpeak <= 0.21\ngini = 0.375\nsamples = 8\nvalue = [6, 2]\nclass = 0", fillcolor="#eeab7b"] ;
19 -> 20 ;
21 [label="gini = 0.0\nsamples = 6\nvalue = [6, 0]\nclass = 0", fillcolor="#e58139"] ;
20 -> 21 ;
22 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2]\nclass = 1", fillcolor="#399de5"] ;
20 -> 22 ;
23 [label="gini = 0.0\nsamples = 3\nvalue = [0, 3]\nclass = 1", fillcolor="#399de5"] ;
19 -> 23 ;
24 [label="gini = 0.0\nsamples = 13\nvalue = [13, 0]\nclass = 0", fillcolor="#e58139"] ;
18 -> 24 ;
25 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2]\nclass = 1", fillcolor="#399de5"] ;
17 -> 25 ;
26 [label="oldpeak <= 0.645\ngini = 0.278\nsamples = 12\nvalue = [10, 2]\nclass = 0", fillcolor="#ea9a61"] ;
8 -> 26 ;
27 [label="gini = 0.0\nsamples = 10\nvalue = [10, 0]\nclass = 0", fillcolor="#e58139"] ;
26 -> 27 ;
28 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2]\nclass = 1", fillcolor="#399de5"] ;
26 -> 28 ;
29 [label="oldpeak <= 0.089\ngini = 0.187\nsamples = 259\nvalue = [232, 27]\nclass = 0", fillcolor="#e89050"] ;
1 -> 29 ;
30 [label="chol <= 0.255\ngini = 0.441\nsamples = 58\nvalue = [39, 19]\nclass = 0", fillcolor="#f2be99"] ;
29 -> 30 ;
31 [label="ca_1.0 <= 0.5\ngini = 0.485\nsamples = 29\nvalue = [12, 17]\nclass = 1", fillcolor="#c5e2f7"] ;
30 -> 31 ;
32 [label="age <= 0.271\ngini = 0.308\nsamples = 21\nvalue = [4, 17]\nclass = 1", fillcolor="#68b4eb"] ;
31 -> 32 ;
33 [label="gini = 0.0\nsamples = 4\nvalue = [4, 0]\nclass = 0", fillcolor="#e58139"] ;
32 -> 33 ;
34 [label="gini = 0.0\nsamples = 17\nvalue = [0, 17]\nclass = 1", fillcolor="#399de5"] ;
32 -> 34 ;
35 [label="gini = 0.0\nsamples = 8\nvalue = [8, 0]\nclass = 0", fillcolor="#e58139"] ;
31 -> 35 ;
36 [label="thalach <= 0.328\ngini = 0.128\nsamples = 29\nvalue = [27, 2]\nclass = 0", fillcolor="#e78a48"] ;
30 -> 36 ;
37 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2]\nclass = 1", fillcolor="#399de5"] ;
36 -> 37 ;
38 [label="gini = 0.0\nsamples = 27\nvalue = [27, 0]\nclass = 0", fillcolor="#e58139"] ;
36 -> 38 ;
39 [label="thal_1.0 <= 0.5\ngini = 0.076\nsamples = 201\nvalue = [193, 8]\nclass = 0", fillcolor="#e68641"] ;
29 -> 39 ;
40 [label="gini = 0.0\nsamples = 168\nvalue = [168, 0]\nclass = 0", fillcolor="#e58139"] ;
39 -> 40 ;
41 [label="ca_0.0 <= 0.5\ngini = 0.367\nsamples = 33\nvalue = [25, 8]\nclass = 0", fillcolor="#eda978"] ;
39 -> 41 ;
42 [label="gini = 0.0\nsamples = 19\nvalue = [19, 0]\nclass = 0", fillcolor="#e58139"] ;
41 -> 42 ;
43 [label="age <= 0.448\ngini = 0.49\nsamples = 14\nvalue = [6, 8]\nclass = 1", fillcolor="#cee6f8"] ;
41 -> 43 ;
44 [label="gini = 0.0\nsamples = 6\nvalue = [6, 0]\nclass = 0", fillcolor="#e58139"] ;
43 -> 44 ;
45 [label="gini = 0.0\nsamples = 8\nvalue = [0, 8]\nclass = 1", fillcolor="#399de5"] ;
43 -> 45 ;
46 [label="ca_0.0 <= 0.5\ngini = 0.36\nsamples = 438\nvalue = [103, 335]\nclass = 1", fillcolor="#76bbed"] ;
0 -> 46 [labeldistance=2.5, labelangle=-45, headlabel="False"] ;
47 [label="cp_0.0 <= 0.5\ngini = 0.5\nsamples = 139\nvalue = [71, 68]\nclass = 0", fillcolor="#fefaf7"] ;
46 -> 47 ;
48 [label="oldpeak <= 0.363\ngini = 0.343\nsamples = 82\nvalue = [18, 64]\nclass = 1", fillcolor="#71b9ec"] ;
47 -> 48 ;
49 [label="chol <= 0.082\ngini = 0.295\nsamples = 78\nvalue = [14, 64]\nclass = 1", fillcolor="#64b2eb"] ;
48 -> 49 ;
50 [label="gini = 0.0\nsamples = 4\nvalue = [4, 0]\nclass = 0", fillcolor="#e58139"] ;
49 -> 50 ;
51 [label="age <= 0.552\ngini = 0.234\nsamples = 74\nvalue = [10, 64]\nclass = 1", fillcolor="#58ace9"] ;
49 -> 51 ;
52 [label="gini = 0.0\nsamples = 39\nvalue = [0, 39]\nclass = 1", fillcolor="#399de5"] ;
51 -> 52 ;
53 [label="age <= 0.635\ngini = 0.408\nsamples = 35\nvalue = [10, 25]\nclass = 1", fillcolor="#88c4ef"] ;
51 -> 53 ;
54 [label="gini = 0.0\nsamples = 8\nvalue = [8, 0]\nclass = 0", fillcolor="#e58139"] ;
53 -> 54 ;
55 [label="thalach <= 0.779\ngini = 0.137\nsamples = 27\nvalue = [2, 25]\nclass = 1", fillcolor="#49a5e7"] ;
53 -> 55 ;
56 [label="gini = 0.0\nsamples = 24\nvalue = [0, 24]\nclass = 1", fillcolor="#399de5"] ;
55 -> 56 ;
57 [label="gini = 0.444\nsamples = 3\nvalue = [2, 1]\nclass = 0", fillcolor="#f2c09c"] ;
55 -> 57 ;
58 [label="gini = 0.0\nsamples = 4\nvalue = [4, 0]\nclass = 0", fillcolor="#e58139"] ;
48 -> 58 ;
59 [label="sex_0.0 <= 0.5\ngini = 0.131\nsamples = 57\nvalue = [53, 4]\nclass = 0", fillcolor="#e78b48"] ;
47 -> 59 ;
60 [label="gini = 0.0\nsamples = 45\nvalue = [45, 0]\nclass = 0", fillcolor="#e58139"] ;
59 -> 60 ;
61 [label="age <= 0.719\ngini = 0.444\nsamples = 12\nvalue = [8, 4]\nclass = 0", fillcolor="#f2c09c"] ;
59 -> 61 ;
62 [label="gini = 0.0\nsamples = 8\nvalue = [8, 0]\nclass = 0", fillcolor="#e58139"] ;
61 -> 62 ;
63 [label="gini = 0.0\nsamples = 4\nvalue = [0, 4]\nclass = 1", fillcolor="#399de5"] ;
61 -> 63 ;
64 [label="oldpeak <= 0.452\ngini = 0.191\nsamples = 299\nvalue = [32, 267]\nclass = 1", fillcolor="#51a9e8"] ;
46 -> 64 ;
65 [label="age <= 0.615\ngini = 0.148\nsamples = 286\nvalue = [23, 263]\nclass = 1", fillcolor="#4aa6e7"] ;
64 -> 65 ;
66 [label="oldpeak <= 0.274\ngini = 0.045\nsamples = 219\nvalue = [5, 214]\nclass = 1", fillcolor="#3e9fe6"] ;
65 -> 66 ;
67 [label="trestbps <= 0.142\ngini = 0.028\nsamples = 213\nvalue = [3, 210]\nclass = 1", fillcolor="#3c9ee5"] ;
66 -> 67 ;
68 [label="sex_0.0 <= 0.5\ngini = 0.245\nsamples = 21\nvalue = [3, 18]\nclass = 1", fillcolor="#5aade9"] ;
67 -> 68 ;
69 [label="gini = 0.5\nsamples = 6\nvalue = [3, 3]\nclass = 0", fillcolor="#ffffff"] ;
68 -> 69 ;
70 [label="gini = 0.0\nsamples = 15\nvalue = [0, 15]\nclass = 1", fillcolor="#399de5"] ;
68 -> 70 ;
71 [label="gini = 0.0\nsamples = 192\nvalue = [0, 192]\nclass = 1", fillcolor="#399de5"] ;
67 -> 71 ;
72 [label="gini = 0.444\nsamples = 6\nvalue = [2, 4]\nclass = 1", fillcolor="#9ccef2"] ;
66 -> 72 ;
73 [label="chol <= 0.241\ngini = 0.393\nsamples = 67\nvalue = [18, 49]\nclass = 1", fillcolor="#82c1ef"] ;
65 -> 73 ;
74 [label="cp_0.0 <= 0.5\ngini = 0.137\nsamples = 27\nvalue = [2, 25]\nclass = 1", fillcolor="#49a5e7"] ;
73 -> 74 ;
75 [label="gini = 0.0\nsamples = 20\nvalue = [0, 20]\nclass = 1", fillcolor="#399de5"] ;
74 -> 75 ;
76 [label="exang_0.0 <= 0.5\ngini = 0.408\nsamples = 7\nvalue = [2, 5]\nclass = 1", fillcolor="#88c4ef"] ;
74 -> 76 ;
77 [label="gini = 0.0\nsamples = 2\nvalue = [2, 0]\nclass = 0", fillcolor="#e58139"] ;
76 -> 77 ;
78 [label="gini = 0.0\nsamples = 5\nvalue = [0, 5]\nclass = 1", fillcolor="#399de5"] ;
76 -> 78 ;
79 [label="thalach <= 0.458\ngini = 0.48\nsamples = 40\nvalue = [16, 24]\nclass = 1", fillcolor="#bddef6"] ;
73 -> 79 ;
80 [label="gini = 0.0\nsamples = 5\nvalue = [5, 0]\nclass = 0", fillcolor="#e58139"] ;
79 -> 80 ;
81 [label="age <= 0.74\ngini = 0.431\nsamples = 35\nvalue = [11, 24]\nclass = 1", fillcolor="#94caf1"] ;
79 -> 81 ;
82 [label="thalach <= 0.756\ngini = 0.488\nsamples = 26\nvalue = [11.0, 15.0]\nclass = 1", fillcolor="#cae5f8"] ;
81 -> 82 ;
83 [label="trestbps <= 0.783\ngini = 0.457\nsamples = 17\nvalue = [11, 6]\nclass = 0", fillcolor="#f3c6a5"] ;
82 -> 83 ;
84 [label="chol <= 0.545\ngini = 0.337\nsamples = 14\nvalue = [11, 3]\nclass = 0", fillcolor="#eca36f"] ;
83 -> 84 ;
85 [label="chol <= 0.268\ngini = 0.153\nsamples = 12\nvalue = [11, 1]\nclass = 0", fillcolor="#e78c4b"] ;
84 -> 85 ;
86 [label="gini = 0.0\nsamples = 1\nvalue = [0, 1]\nclass = 1", fillcolor="#399de5"] ;
85 -> 86 ;
87 [label="gini = 0.0\nsamples = 11\nvalue = [11, 0]\nclass = 0", fillcolor="#e58139"] ;
85 -> 87 ;
88 [label="gini = 0.0\nsamples = 2\nvalue = [0, 2]\nclass = 1", fillcolor="#399de5"] ;
84 -> 88 ;
89 [label="gini = 0.0\nsamples = 3\nvalue = [0, 3]\nclass = 1", fillcolor="#399de5"] ;
83 -> 89 ;
90 [label="gini = 0.0\nsamples = 9\nvalue = [0, 9]\nclass = 1", fillcolor="#399de5"] ;
82 -> 90 ;
91 [label="gini = 0.0\nsamples = 9\nvalue = [0, 9]\nclass = 1", fillcolor="#399de5"] ;
81 -> 91 ;
92 [label="trestbps <= 0.387\ngini = 0.426\nsamples = 13\nvalue = [9, 4]\nclass = 0", fillcolor="#f1b991"] ;
64 -> 92 ;
93 [label="gini = 0.0\nsamples = 4\nvalue = [0, 4]\nclass = 1", fillcolor="#399de5"] ;
92 -> 93 ;
94 [label="gini = 0.0\nsamples = 9\nvalue = [9, 0]\nclass = 0", fillcolor="#e58139"] ;
92 -> 94 ;
}
