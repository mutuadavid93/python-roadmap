def padding(f):
    def padder():
        print()
        f()
        print()
    return padder