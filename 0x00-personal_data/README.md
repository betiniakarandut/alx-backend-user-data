<p><h1>0x00. Personal data :fire:</h1></p>
<p><h1>Description :house:</h1></p>
In this project I began to learn about PII(Personally Identifiable Information) and what it entails. Personally Identifiable Information(PII) refers to any data that can be used to identify an individual uniquely.<br>
It's important to handle PII with care and protect it from unauthorized access to prevent identity theft, fraud, and privacy breaches. Organizations and individuals should follow best practices for data security and ensure compliance with relevant privacy laws and regulations.

## Learning Objectives<br>

- Examples of Personally Identifiable Information (PII)<br>
- How to implement a log filter that will obfuscate PII fields<br>
- How to encrypt a password and check the validity of an input password<br>
- How to authenticate to a database using environment variables

## Tasks :pencil:

- [Read and filter data](./filtered_logger.py)

#

Write a function called filter_datum that returns the log message obfuscated:<br>Arguments:<br>

- fields: a list of strings representing all fields to obfuscate<br>
- redaction: a string representing by what the field will be obfuscated<br>
- message: a string representing the log line<br>
- separator: a string representing by which character is separating all fields in the log line (message)<br>
- The function should use a regex to replace occurrences of certain field values.<br>
- filter_datum should be less than 5 lines long and use re.sub to perform the substitution with a single regex.

#

- [Encrypting passwords](./encrypt_password.py)

#

User passwords should NEVER be stored in plain text in a database.<br>Implement a hash_password function that expects one string argument name password and returns a salted, hashed password, which is a byte string.<br>Use the bcrypt package to perform the hashing (with hashpw).

#

## Author

[Betini Akarandut](https://github.com/betiniakarandut)
