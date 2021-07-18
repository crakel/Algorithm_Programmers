def solution(participant, completion):
    i = 0
    while (len(participant) > 1):
        if participant[i] in completion:
            completion.remove(participant[i])
            del participant[i]
            i -= 1
        i += 1
    return participant.pop()