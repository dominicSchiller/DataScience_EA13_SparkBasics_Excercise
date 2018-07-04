# DataScience: EA13 - Spark Basics Exercise
Exercise from the course Data Science at Beuth University of Applied Sciences

### Author
 -----------
* **Name**<br />Dominic Schiller<br />
* **University**<br />Brandenburg University of Applied Sciences<br />
* **E-Mail**<br />dominic.schiller@th-brandenburg.de

---------
### Tasks
> 1. Load the complete Shakespeare writings from [here](https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt), clean the file (there is some legal text at the beginning and in the file; you can do it by hand if needed) and search for the #24 most used word in his writings. Provide your code + result in one pdf, txt or by one link.

---------
### Solution
Please find the implementation for determining the #24 most used words with Apache Spark in the following python script:  [**Spark_Shakespeare_Demo.py**](https://github.com/dominicSchiller/DataScience_EA13_SparkBasics_Excercise/blob/develop/Spark_Shakespeare_Demo.py)
<br /><br />
This python script determines the most frequently ued words in the given book *The Sunset*, generates the file [**most_frequent_words.txt**](https://github.com/dominicSchiller/DataScience_EA13_SparkBasics_Excercise/blob/develop/most_frequent_words.txt) and writes the #24 top most used words into it.
<br /><br />
To avoid determining more or less irrelevant fill words, the python script filters all collected words against a set of so called *stop words* defined in the python file [**English_Stop_Words.py**](https://github.com/dominicSchiller/DataScience_EA13_SparkBasics_Excercise/blob/develop/English_Stop_Words.py) which won't be taken into account.
<br />
<br />
The result is shown by the following table (also have a look here: [**most_frequent_words.txt**](https://github.com/dominicSchiller/DataScience_EA13_SparkBasics_Excercise/blob/develop/most_frequent_words.txt)):<br />

| Word 	| Occurences 	|
|:------:	|:----------:	|
| thou 	| 5485 	|
| shall 	| 3591 	|
| lord 	| 3555 	|
| thee 	| 3181 	|
| king 	| 3155 	|
| come 	| 3125 	|
| good 	| 2835 	|
| love 	| 2371 	|
| enter 	| 2122 	|
| make 	| 1992 	|
| hath 	| 1939 	|
| know 	| 1880 	|
| like 	| 1729 	|
| speak 	| 1297 	|
| time 	| 1287 	|
| heart 	| 1238 	|
| hand 	| 1160 	|
| duke 	| 1151 	|
| look 	| 1133 	|
| father 	| 1111 	|
| tell 	| 1106 	|
| think 	| 1087 	|
| exeunt 	| 1021 	|
| queen 	| 987 	|