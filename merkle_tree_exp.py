from hashlib import sha256 as sha

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def m_tree(transactions):
    """Takes an array of transactions and computes a Merkle root"""
    sub_t = []
    for i in chunks(transactions,2):
        if len(i) == 2:
            hash = sha(str(i[0]+i[1])).hexdigest()
        else:
            hash = sha(str(i[0]+i[0])).hexdigest()
        sub_t.append(hash)
    print (sub_t)
    if len(sub_t) == 1:
       return sub_t[0]
    else:
       return m_tree(sub_t)

m_tree(['a' , 'b' , 'c' , 'd' , 'e'])
