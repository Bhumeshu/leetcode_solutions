class TupleAttributes:

    def touple_att(self, sample_tuple):
        if sample_tuple is None:
            sample_tuple = ()

        sample_tuple.count()
        sample_tuple.index()
        return True


print(TupleAttributes.tuple_att((1, 2, 10, 3, 15)))
