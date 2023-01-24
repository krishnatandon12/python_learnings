# In python, we can use match case statement as an alternative to if, elif and else
# This is like switch in other programming languages.

http_status = 200

match http_status:
    case 200 | 210:
        print("Success")
    case 400:
        print("Bad Requst")
    case 404:
        print("Not found")
    case 500 | 501:
        print("Server error")
    case _:
        print("Unknown")
