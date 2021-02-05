def emotions(emotions):
    res = {}
    i = 1

    while i < 6:
        maxValue = 0
        num = 0
        for key, value in emotions.items():
            num = value
            if num > maxValue:
                maxValue = num 
                maxKey = key
        if maxValue == 0:
            maxKey = key
        res.update({maxKey:emotions.get(maxKey)})
        emotions.pop(maxKey)
        i += 1
    return res
  

