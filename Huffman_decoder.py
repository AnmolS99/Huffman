
def Huffman_decoder(string):
    decoded_str = ""
    tmp_str = ""
    i = 0
    while len(string) != 0:
        tmp_str = string[0:i]
        if tmp_str in dictionary:
            letter = dictionary[tmp_str]
            decoded_str = decoded_str + letter
            if len(decoded_str.split()) % 15 == 0 and decoded_str[len(
                    decoded_str) - 1] == " ":
                decoded_str += "\n"
            string = string[i:]
            i = 0
        else:
            i += 1
    return decoded_str


def convert_to_dict(list):
    dictionary = dict()
    for element in list:
        tmp_list = element.split("=")
        dictionary.update({tmp_list[1]: tmp_list[0]})
    return dictionary


# Example of Huffman-encoding of text

dictionary = convert_to_dict(["\n=11101100",
                              " =00",
                              "!=0111011110111110",
                              "'=1011101111",
                              "(=0111011110111111",
                              ")=011101111011110",
                              ",=101111",
                              ".=0101110",
                              "0=1101011110",
                              "1=11101010",
                              "2=11010110",
                              "3=01111110",
                              "4=01110110",
                              "5=010111101",
                              "6=1110101111",
                              "7=1110110110",
                              "8=1101011100",
                              "9=1110101100",
                              ":=1110100",
                              ";=111011010",
                              "?=11101011011",
                              "A=0111110",
                              "B=0111111110",
                              "C=10111011000",
                              "D=0111111111",
                              "E=1110101110",
                              "F=1110101101011",
                              "G=1110110111",
                              "H=0101111000",
                              "I=01011111",
                              "J=011111110",
                              "K=0111011110110",
                              "L=011101110",
                              "M=10111011001",
                              "N=10111011010",
                              "O=0111011111",
                              "P=0101111001",
                              "R=1101011111",
                              "S=1101011101",
                              "T=1011101110",
                              "U=11101011010101",
                              "W=01110111100",
                              "Y=01110111101110",
                              "Z=011101111010",
                              "a=1010",
                              "b=1110111",
                              "c=010110",
                              "d=11100",
                              "e=1111",
                              "f=101101",
                              "g=1101010",
                              "h=1000",
                              "i=11001",
                              "j=101110110111",
                              "k=10111010",
                              "l=01010",
                              "m=110100",
                              "n=0110",
                              "o=0100",
                              "p=1011100",
                              "q=11101011010100",
                              "r=11000",
                              "s=11011",
                              "t=1001",
                              "u=101100",
                              "v=0111010",
                              "w=011110",
                              "x=111010110100",
                              "y=011100",
                              "z=101110110110"])

# Decoding the Huffman code for "z"
print(Huffman_decoder("101110110110"))
