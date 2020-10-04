

def reorderLogFiles(logs):
    """
    Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    """

    def getKey(log):
        words = log.split(" ")
        ident = words[0]
        logMessage = words[1:]

        if logMessage[0][0].isalpha():
            return (0, logMessage, ident)
        else:
            return (1,)

    logs.sort(key=getKey)
    return logs

    """def get_key(log):
        _id, rest = log.split(" ", maxsplit=1)
        return (0, rest, _id) if rest[0].isalpha() else (1,)

    return sorted(logs, key=get_key)
    """



def main():
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    result = reorderLogFiles(logs)
    print ("Result is", result)




if __name__ == "__main__":
    main()