def hash(inp_str,len_=16):
    hash_value_ =0xDEADBEEF
    prime = 2654435761
    
    for char in inp_str:
        hash_value_ ^= ord(char) 
        hash_value_ *= prime
        hash_value_ &=0xFFFFFFFF
    for i in range(min(10,len_)):
        hash_value_ ^= i*i*i
        hash_value_ *= prime

    hashed_hex = format(hash_value_,f"0{len_}8x")
    return hashed_hex[-len_:]


def convert_byte_to_binary(byte_arr):
    final_str = "";
    for each in byte_arr:
        final_str += format(each,"08b")
    return final_str

def convert_binary_to_string(byte_arr):
    final_str = ""
    for i in range(0,len(byte_arr),8):
        curr_str = byte_arr[i:i+8]
        final_str += chr(int(curr_str,2))
    return final_str

def run_length_encode(inp_str):
    encoded_str = ""
    count = 1;
    for i in range(1,len(inp_str)):
        if(inp_str[i] == inp_str[i-1]) and count < 10:
            count +=1
        else:
            encoded_str  += str(count) + inp_str[i-1]
            count = 1;
    encoded_str += str(count) + inp_str[-1]
    return encoded_str


def run_length_decode(inp_str):
    decoded_str = ""
    for i in range(0,len(inp_str),2):
        count_ = int(inp_str[i])
        char_ = inp_str[i+1]
        decoded_str += (char_* count_)
    return decoded_str
