from word_src.moods import moods


def check_for_feelingInMsg(msg:str):

    for w in msg.split(" "):
        if w in moods:
            print("[+] found mood: {}",format(w))
            return "I feel {} too.".format(w)

    return None