def __recurssivWordBuilder(word: str, index, out: list):

    if word not in out:
        out.append(word)

    if index < len(word):
        __recurssivWordBuilder(word, index+1, out)

        beg = word[0:(index)]
        mid = word[index].upper()
        end = word[(index+1):(len(word))]

        nw = beg+mid+end
        # print(nw)
        # import time
        # time.sleep(4)
        __recurssivWordBuilder(nw, index+1, out)


def buildkeyWordPossibilieties(word):
    """
    Builds all possiblie words (lowercase / upercase)

    in: word  
    out: list[]
    """

    out = []
    w = word.lower()
    __recurssivWordBuilder(w, 0, out)

    print("[+] generated {} words for {}".format(len(out), w))
    return out


def checkIfInText2(keyword: str, text: str):
    """
    checks if keyword in text

    NOT CASE SENSITIVE
    """

    for keyPart in buildkeyWordPossibilieties(keyword):
        if keyPart in text:
            print("     [+] found keyword")
            return True

    print("     [-] cannot find keyword")
    return False


def checkIfInText(keyword: str, text: str):
    """
    new mehtode
    """
    if keyword.lower() in text.lower():
        print("     [+] found keyword")
        return True

    print("     [-] cannot find keyword")
    return False
