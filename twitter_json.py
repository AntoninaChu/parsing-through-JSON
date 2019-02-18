import json


def get_arg():
    '''
    This function asks you to enter options and programm will search through
    JSON file looking for this option.
    '''
    arg = input("Enter the option to search or 'CLOSE' to recieve data: ")
    return arg


def file_processing(filename):
    '''
    This functions checks filename, reads file and returns you an information.
    '''
    if ".json" not in filename:
        print("Your file must be a JSON file.")
        return main() #returns you to start if your file is not JSON
    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print("There is no such file.")
        return main() #returns you to start if there is no such file
    ff = json.load(f)
    while True:
        arg = get_arg()
        if arg == "CLOSE":
            return ff
        else:
            try:
                if type(ff) == list:   # try to convert option to int
                    arg = int(arg)     # if we are in list
                ff = ff[arg]
            except KeyError:
                print("There is no way with this option.")
                pass
            except TypeError:
                print("We can't go deeper or this data is a list")
                pass
            except IndexError as err:
                print(err)
                pass
            except ValueError:
                print("Enter a number because we are searching in list.")
                pass


def main():
    '''
    This is main function that puts together whole programm.
    '''
    filename = input("Enter a name of file: ")
    return file_processing(filename)

print(main()) # calling main function and printing results
