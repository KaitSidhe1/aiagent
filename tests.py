# from functions.get_files_info import get_files_info
# from functions.get_file_content import get_file_content
# from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    # print("Result for current directory:")
    # print (get_files_info("calculator", "."))
    # print()

    # print("Result for 'pkg' directory:")
    # print (get_files_info("calculator", "pkg"))
    # print()

    # print("Result for '/bin' directory:")
    # print ("    " + get_files_info("calculator", "/bin"))
    # print()

    # print("Result for '../' directory:")
    # print ("    " + get_files_info("calculator", "../"))
    # print()

    # get_file_content
    # result = get_file_content("calculator", "lorem.txt")
    # print(result)

    # result = get_file_content("calculator", "main.py")
    # print(result)
    # print()

    # result = get_file_content("calculator", "pkg/calculator.py")
    # print(result)
    # print()

    # result = get_file_content("calculator", "/bin/cat")
    # print(result)
    # print()

    # result = get_file_content("calculator", "pkg/does_not_exist.py")
    # print(result)
    # print()


    # write_file

    
    # result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    # print(result)
    # print() 

    # result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print(result)
    # print() 

    # result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    # print(result)
    # print() 

    # run_file
    result = run_python_file("calculator", "main.py") 
    print(result)
    print() 

    result = run_python_file("calculator", "main.py", ["3 + 5"]) 
    print(result)
    print() 

    result = run_python_file("calculator", "tests.py") 
    print(result)
    print() 

    result = run_python_file("calculator", "../main.py") 
    print(result)
    print()

    result = run_python_file("calculator", "nonexistent.py") 
    print(result)
    print()  

    result = run_python_file("calculator", "lorem.txt") 
    print(result)
    print()  



if __name__ == "__main__":
    test()
    