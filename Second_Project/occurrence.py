#string = 'فیضی خر است! گاو من است! این پروژه اول ما است که مثل خر در ان گیر کرده ایم.'

def uniquify(string):
    output = []
    seen = set()
    for word in string.split():
        if word not in seen:
            output.append(word)
            seen.add(word)
    return ' '.join(output)

#print(uniquify(string))