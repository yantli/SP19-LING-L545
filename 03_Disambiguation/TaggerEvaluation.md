# Tagger evaluation

Below is the performance evaluation of UDpipe when applied on the UD_Finnish-TDT treebank. The UPOS precision was 94.64.
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.64 |     94.64 |     94.64 |     94.64
XPOS       |     95.81 |     95.81 |     95.81 |     95.81
Feats      |     90.77 |     90.77 |     90.77 |     90.77
AllTags    |     89.75 |     89.75 |     89.75 |     89.75
Lemmas     |     84.52 |     84.52 |     84.52 |     84.52
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00


Below is the performance evaluation of the perceptron-based tagger when applied on the same data. The UPOS precision was 90.36.
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     90.36 |     90.36 |     90.36 |     90.36
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     90.36 |     90.36 |     90.36 |     90.36
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

Turned out that UDpipe achieved a better performance on this language.



When it comes to Portuguese (UD_Portuguese-GSD), the performance evaluation of UDpipe is displayed below:
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     97.19 |     97.19 |     97.19 |     97.19
XPOS       |     97.19 |     97.19 |     97.19 |     97.19
Feats      |     99.88 |     99.88 |     99.88 |     99.88
AllTags    |     97.18 |     97.18 |     97.18 |     97.18
Lemmas     |     95.93 |     95.93 |     95.93 |     95.93
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00


And here is the performance evaluation of perceptron-based tagger:
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.28 |     96.28 |     96.28 |     96.28
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.28 |     96.28 |     96.28 |     96.28
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00

While UDpipe outperformed the perceptron-based tagger, the difference between their UPOS is smaller.
