class DictAttributes:

    def dict_att(self, sample_dict):
        if sample_dict is None:
            sample_dict = {}

        sample_dict.get()
        sample_dict.pop()
        sample_dict.clear()
        sample_dict.copy()
        sample_dict.fromkeys()
        sample_dict.items()
        sample_dict.keys()
        sample_dict.popitem()
        sample_dict.setdefault()
        sample_dict.update()
        sample_dict.values()
        return True


print(DictAttributes.dict_att({1: 5, 2: 10, 3: 15}))
