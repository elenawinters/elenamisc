
def msg_compare(mode: str = 'eq', actual: str = 'test', compare: str = 'test') -> bool:
    match mode.lower():
        case 'eq' | 'equals':
            if actual == compare:
                return True
        case 'sw' | 'startswith':
            return actual.startswith(compare)
        case 'ew' | 'endswith':
            return actual.endswith(compare)
        case 'in' | 'contains':
            if compare in actual:
                return True


mode = 'in'
possible = ['zaqHeart', 'zaqLurkie', 'zaqCool', 'zaqHayes', 'zaqClap']
actual = 'zaqHeart'

if any(msg_compare(mode, actual, msg) for msg in possible):
    print(actual)
    
