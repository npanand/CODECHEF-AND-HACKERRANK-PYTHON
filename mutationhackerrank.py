def mutate_string(string, position, character):
    pos=position+1
    g=string[:position]+character+string[pos:]
    return g