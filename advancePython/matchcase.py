def status(opt):
    match opt:
        case 200:
            return 'ok'
        case 404:
            return "not found"
        case 500:
            return "initernal error"
        case _:
            return"unkowm"

print(status(200))