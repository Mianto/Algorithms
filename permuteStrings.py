def permute(word, l, r):
    if l == r:
        print toString(word)
    else:
        for i in xrange(l, r+1):
            word[l], word[i] = word[i], word[l]
            permute(word, l+1, r)
            word[l], word[i] = word[i], word[l]

def toString(li):
    return ''.join(li)

def main():
    s = "I am great"
    permute(list(s), 0, len(s)-1)

if __name__ == '__main__':
    main()
