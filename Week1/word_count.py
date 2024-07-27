'''
Write a program to count the number of  words and then return them in the descending order of frequency 

'''
def main(sentence):
    map = dict()
    words = sentence.lower().split()
    for i in words:
        if i in map.keys():
            map[i]+=1
        else:
            map[i] = 1
    map = sorted(map, key = map.get, reverse = True)
    print(map)


if __name__ == "__main__":
    main("Cat bat ball cat cat bat cat")
    
