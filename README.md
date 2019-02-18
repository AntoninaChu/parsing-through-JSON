# parsing-through-JSON
this programm is interactive.
It will ask you to enter a name of JSON file and then it will ask where and how deep should we go.
you need to say step by step an option and and programm will go deeper into file. if it is enough you just need to enter CLOSE.

-------------------------------------------------------------------
an example:
-------------------------------------------------------------------

Enter a name of file: test.py
Your file must be a JSON file.

Enter a name of file: edfghn.json
There is no such file.

Enter a name of file: registrants.json

Enter the option to search or 'CLOSE' to recieve data: students

Enter the option to search or 'CLOSE' to recieve data: jk
Enter a number because we are searching in list.

Enter the option to search or 'CLOSE' to recieve data: 1

Enter the option to search or 'CLOSE' to recieve data: student

Enter the option to search or 'CLOSE' to recieve data: 4
There is no way with this option.

Enter the option to search or 'CLOSE' to recieve data: CLOSE
{'name': 'Білик Владислав', 'domain': 'physics'}

--------------------------------------------------------------------
To use this programm you need to know a stucture of your file.
