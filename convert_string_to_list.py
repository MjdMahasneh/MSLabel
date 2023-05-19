import numpy as np

def string_to_list(input_string):
    input_string = (input_string.replace('[',''))
    input_string = (input_string.replace(']',''))
    input_string = (input_string.replace('(',''))
    input_string = (input_string.replace(')',''))
    input_string = (input_string.replace(',',''))

    output_list = [int(x) for x in input_string.split()]
    output_list = np.reshape(output_list, (-1 , 4))

    return(output_list)


#res = string_to_list(input_string = '[(492, 428, 192, 166), (424, 586, 274, 200)]')
#print(res)

