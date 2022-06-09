#https://www.codewars.com/kata/5b16490986b6d336c900007d/train/python
results = {"Java": 10, "Ruby": 80, "Python": 65}
results = {"Hindi": 60, "Dutch": 93, "Greek": 71}

results = {'Lua': 51, 'Swift': 83, 'CoffeeScript': 47, 'java': 60, 'PowerShell': 55, 'Linex': 47, 'C++': 71, 'Julia': 62}
print(sorted([k for k,v in results.items() if v>=60],reverse=True))
def my_languages(results):
    re = sorted([(k,v) for k,v in results.items() if v>=60],key= lambda x:x[1],reverse=True)
    return [i[0] for i in re]
print(my_languages(results))

def my_languages(results):
    return sorted((l for l,r in results.items() if r>=60), reverse=True, key=results.get)
print(my_languages(results))

'''
 Random tests
 Log
{'Estonian': 94, 'Irish': 46}
Test Passed
 Log
{'ASM': 13, 'Java': 71, 'Kotlin': 6}
Test Passed
 Log
{'Russian': 42, 'Hungarian': 43, 'French': 13, 'Bulgarian': 92, 'Portuguese': 99, 'Estonian': 95}
Test Passed
 Log
{'Solidity': 93, 'Objective-C': 89, 'Ruby': 73, 'PHP': 32}
Test Passed
 Log
{'Objective-C': 34, 'R': 65, 'Crystal': 26, 'Nim': 3, 'OCaml': 60, 'Swift': 10, 'SQL': 85}
Test Passed
 Log
{'Lua': 51, 'Swift': 63, 'CoffeeScript': 17, 'Elixir': 24, 'PowerShell': 5, 'OCaml': 47, 'C++': 71, 'Julia': 62}
Test Passed
 Log
{'JavaScript': 9, 'Erlang': 93, 'Objective-C': 97, 'Crystal': 50, 'Groovy': 90, 'Go': 65, 'Ruby': 39}
Test Passed
 Log
{'Irish': 80}
Test Passed
 Log
{'French': 79, 'Polish': 33, 'Lithuanian': 81, 'Irish': 87, 'Greek': 41, 'Korean': 92}
Test Passed
 Log
{'Lua': 21, 'JavaScript': 69, 'Dart': 66, 'SQL': 42}
Test Passed
 Log
{'Greek': 64, 'Danish': 5, 'Swedish': 32}
Test Passed
 Log
{'Polish': 59, 'Danish': 52, 'Korean': 89}
Test Passed
 Log
{'Italian': 22, 'Russian': 70, 'Arabic': 52, 'Spanish': 74, 'Chinese': 46, 'Slovak': 44}
Test Passed
 Log
{'PHP': 43, 'OCaml': 13, 'R': 97, 'C#': 9, 'PowerShell': 71, 'CoffeeScript': 60}
Test Passed
 Log
{'Erlang': 76, 'Ruby': 20, 'ASM': 41, 'R': 31}
Test Passed
 Log
{'Irish': 98, 'Japanese': 21, 'Lithuanian': 67, 'Greek': 74, 'Russian': 40, 'Swedish': 54, 'Latvian': 95, 'Hungarian': 49}
Test Passed
 Log
{'F#': 19, 'C': 11}
Test Passed
 Log
{'Hindi': 90, 'Lithuanian': 35, 'Arabic': 43, 'Spanish': 60}
Test Passed
 Log
{'Turkish': 63, 'Portuguese': 41, 'Irish': 5, 'Bengali': 67, 'Arabic': 48}
Test Passed
 Log
{'Latvian': 42, 'Romanian': 89}
Test Passed
 Log
{'Italian': 33, 'Irish': 4, 'Bengali': 58}
Test Passed
 Log
{'PHP': 34, 'Groovy': 29, 'Java': 7, 'Nim': 23, 'C++': 2, 'Scala': 56, 'Elixir': 24}
Test Passed
 Log
{'German': 69, 'Hungarian': 71}
Test Passed
 Log
{'Czech': 61, 'Punjabi': 6, 'Maltese': 89, 'Spanish': 30, 'German': 54, 'Italian': 31, 'Japanese': 74, 'Greek': 60}
Test Passed
 Log
{'Elixir': 44, 'Solidity': 40, 'Shell': 59, 'Scala': 89, 'C++': 73, 'Kotlin': 98}
Test Passed
 Log
{'PHP': 11, 'Objective-C': 45, 'Erlang': 61, 'Ruby': 46}
Test Passed
 Log
{'C#': 95, 'PowerShell': 37, 'Erlang': 7}
Test Passed
 Log
{'English': 80, 'Hindi': 87, 'Italian': 97, 'Maltese': 50, 'Irish': 16, 'Hungarian': 12, 'Chinese': 66}
Test Passed
 Log
{'R': 11, 'Erlang': 98, 'Julia': 57, 'PowerShell': 71, 'Kotlin': 45, 'Python': 15}
Test Passed
 Log
{'Java': 35, 'JavaScript': 75, 'R': 61, 'Scala': 82, 'PowerShell': 54, 'Lua': 78, 'F#': 94, 'Go': 88}
Test Passed
 Log
{'TypeScript': 11, 'Julia': 5, 'Fortran': 21}
Test Passed
 Log
{'Greek': 61, 'Punjabi': 58, 'Hungarian': 26, 'Czech': 79, 'Slovak': 44, 'Russian': 39, 'Chinese': 54}
Test Passed
 Log
{'Russian': 89, 'Latvian': 41, 'Turkish': 54, 'Czech': 28, 'English': 93, 'Arabic': 46, 'Swedish': 33, 'Slovenian': 48}
Test Passed
 Log
{'Clojure': 23, 'Nim': 6, 'Shell': 26, 'PowerShell': 30}
Test Passed
 Log
{'ASM': 95, 'Clojure': 62, 'Python': 85, 'C': 50}
Test Passed
 Log
{'Danish': 50, 'Irish': 22, 'Estonian': 53, 'Hindi': 42, 'Croatian': 61, 'Maltese': 32}
Test Passed
 Log
{'Bulgarian': 5, 'Hindi': 59, 'Croatian': 91, 'Danish': 23, 'Latvian': 32, 'Polish': 35}
Test Passed
 Log
{'Lithuanian': 94, 'Japanese': 6, 'Chinese': 40}
Test Passed
 Log
{'Shell': 24, 'Python': 32, 'PowerShell': 31, 'Rust': 95, 'Groovy': 27, 'Haskell': 1, 'JavaScript': 81}
Test Passed
 Log
{'Chinese': 92, 'Romanian': 70}
Test Passed
 Log
{'Julia': 7, 'Lua': 79, 'ASM': 42, 'Clojure': 60}
Test Passed
 Log
{'Finnish': 94, 'Italian': 76}
Test Passed
 Log
{'Go': 32, 'Nim': 72, 'Groovy': 7, 'JavaScript': 63, 'TypeScript': 48}
Test Passed
 Log
{'Python': 31, 'Java': 34}
Test Passed
 Log
{'Czech': 65, 'Swedish': 8, 'Arabic': 3, 'Greek': 77}
Test Passed
 Log
{'Finnish': 90, 'Czech': 19, 'Lithuanian': 51, 'Slovenian': 31}
Test Passed
 Log
{'Shell': 19, 'Solidity': 13, 'TypeScript': 55, 'PHP': 40, 'Java': 61, 'Julia': 71}
Test Passed
 Log
{'Japanese': 26, 'Estonian': 46, 'Italian': 91, 'Czech': 34, 'Maltese': 71, 'Finnish': 79, 'Korean': 60, 'Arabic': 74}
Test Passed
 Log
{'Slovak': 40}
Test Passed
 Log
{'Polish': 80, 'Greek': 60}
Test Passed
Completed in 9.44ms
'''