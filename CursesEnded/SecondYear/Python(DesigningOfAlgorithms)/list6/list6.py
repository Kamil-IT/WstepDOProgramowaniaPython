# Huffman

ciag = 'BCAADDDCCACACACąś'

usun_nieobsl = str.maketrans('', '', 'ąęćżźś')
ciag = ciag.translate(usun_nieobsl)
print(ciag)


# tworzenie wierzchołków
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# algorytm huffmana
def huffman_code_tree(node, left=True, binCiag=''):
    if type(node) is str:
        return {node: binCiag}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binCiag + '0'))
    d.update(huffman_code_tree(r, False, binCiag + '1'))
    return d


# szacowanie prawdopodobieństw
freq = {}
for c in ciag:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

for (char, frequency) in freq:
    print((char, huffmanCode[char]))
