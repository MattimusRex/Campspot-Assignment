# Campspot-Assignment
Python modules and test cases for Campspot coding assignment.

# How to build and run the program
1) Install Python 3. The python 3 installation files can be found at https://www.python.org/downloads/. macOS users may want to use Homebrew to install python 3 per this guide https://docs.python-guide.org/starting/install3/osx/. Be sure to add python to your system PATH during installation if not using Homebrew.
2) Clone this repo.
3) Open a terminal/command prompt and navigate into the campspot_coding_assignment directory in the repo. You should be in the directory with reservation_solver.py.
4) Execute the reservation_solver.py script with a required input file argument.
"python reservation_solver.py test_modules/test_cases/test-case.json"
You can also add an optional minimum reservation length argument of 1, 2, or 3.
"python reservation_solver.py test_modules/test_cases/test-case.json -mrl 1"
If you have not added python 3 to your system path, you may need to give the absolute path to python 3 in the command like "C:\Users\matth\AppData\Local\Programs\Python\Python37\python reservation_solver.py test_modules/test_cases/"
5) The program will print the names of the campsites which are valid for the given data.

# Explanation of approach to solving the problem
First I needed to read the json file and parse it into a search, the campsites, and the reservations. Making these separate classes allows for them to more easily be reused or expanded later. Once the data is in a usable state, I needed to analyse the reservations at each campsite and the search to find campsites where the new reservation could be made. For a search to be valid, it must either be entirely before or entirely after each existing reservation. Anything else causes an overlap and is invalid. Then the gap between the search and the reservation must be checked to make sure it is either 0 or at least as large as the minimum reservation length. If not, then the gap could never be filled and the search is not valid.

# Assumptions and Special Considerations
My program allows for a minimum reservation length of 1, 2, or 3, and this could easily be expanded to include longer lengths. Although I am accepting a single minimum reservation length for all of the campsites in a json file, the code could easily be expanded to except different minimum reservation lengths for each campsite by adding a corresponding property to the campsite class, removing the command line argument, and changing the structure of the input files. 

I also made the assumption that any given date for a reservation was for that entire day and no other day rather then a checkout/checkin system with guests leavining in the morning and arriving in the afternoon. This means that a reservation ending on 6/03/2018 and another reservation starting on 6/04/2018 produce no gap as each day is entirely reserved. 

I chose Python 3 because I have used it for small projects like this one while doing coding in my personal time. Howevever, I have never had an formal training in Python or its coding standards so certain aspects, like comments, may not match the Python standards.
