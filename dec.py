import os
def print_file(path):
    def decorator(func):
        def wrapper():
            result=func()
            with open(path,"a") as text_file:
                for slice_of_info in result:
                    if isinstance(slice_of_info,str):
                        text_file.writelines(slice_of_info+" ")
                    else:
                        for part in slice_of_info:
                            text_file.writelines(str(part)+" ")
                        text_file.writelines("\n")            
                text_file.writelines("\n")
            return
        return wrapper
    return decorator
