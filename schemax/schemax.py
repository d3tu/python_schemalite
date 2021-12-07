class Schema:
    def __init__(self, d: dict):
        self.__d = d

    def test(self, d: dict) -> bool:
        return self.__test(d, self.__d)

    def parse(self, d: dict) -> dict:
        __final = {}
        return self.__parse(d, self.__d, __final)

    def __test(self, d: dict, __d: dict) -> bool:
        for k in __d.keys():
            if not k in d:
                return False
            elif type(__d[k]) == dict:
                if type(d[k]) == dict:
                    if not self.__test(d[k], __d[k]):
                        return False
                else:
                    return False
            elif type(d[k]) != __d[k]:
                return False
        return True

    def __parse(self, d: dict, __d: dict, __final: dict) -> dict:
        for k in __d.keys():
            __final[k] = __d[k]
            if not k in d:
                if (type(__d[k])) == dict:
                    d[k] = {}
                    self.__parse(d[k], __d[k], __final[k])
                else:
                    d[k] = __d[k]()
            elif type(__d[k]) == dict:
                self.__parse(d[k], __d[k], __final[k])
            elif type(d[k]) != __d[k]:
                d[k] = __d[k]()
            __final[k] = d[k]
        return __final
