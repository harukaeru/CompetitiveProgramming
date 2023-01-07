#!/usr/bin/env python3.8
N = int(input())
T = input()

VOCAB_SIZE = 128
class TrieNode:
    """
    Trie木の1ノードを表すクラス
 
    Attributes
    ----------
    item : str
        登録された単語の読み方
        単語終端ノード以外の場合はNone
 
    children : list
        子ノードのリスト
    """
 
 
    def __init__(self, item = None):
        self.item = item
        self.children = [-1 for i in range(VOCAB_SIZE)]
 
    def __str__(self):
        ret = ""
        ret = ret + "item = {}\n".format(self.item)
        ret = ret + "children = \n{}".format(self.children)
        return ret
 
class Trie:
    """
    Trie木を表すクラス
 
    Attributes
    ----------
    nodes : TrieNode
        ノードのリスト
    """
 
    def __init__(self):
        root = TrieNode()
        self.nodes = [root]
 
 
    def __add_node(self, node):
        """
        nodesにノードを追加する
        追加したノードのインデックスを返す
 
        Parameters
        ----------
        node : TrieNode
            追加するノード
 
        Returns
        -------
        index : int
            追加したノードのインデックス
        """
        self.nodes.append(node)
        return len(self.nodes) - 1
 
    def __get_char_num(self, c):
        """
        文字のidを返す
        aが1, bが2, ..., zが26となる
 
        Parameters
        ----------
        c : char
          idを取得したいしたい文字
 
        Returns
        -------
        id : int
          文字のid
        """
 
        return ord(c) - ord('a')
 
    def insert(self ,word, item, char_index=0, node_index=0):
        """
        Trieに新しい単語を登録する
 
        Parameters
        ----------
        word : str
            登録する単語
 
        item : str
            wordに対応する読み方
 
        char_index : int
            現在着目している文字の位置
 
        node_index : int
            現在着目しているノードの位置
        """
 
        char_num = self.__get_char_num(word[char_index])
        next_node_index = self.nodes[node_index].children[char_num]
        if next_node_index == -1:
            # 現在のノードにword[char_index]での遷移がなかった場合
            new_node = TrieNode()
            next_node_index = self.__add_node(new_node)
            self.nodes[node_index].children[char_num] = next_node_index
 
        if char_index == len(word) - 1:
            # 最後の文字だった場合
            self.nodes[next_node_index].item = item
        else:
            self.insert(word, item, char_index+1, next_node_index)
 
    def query(self, word):
        """
        作ったTrieを検索する
 
        Parameters
        ----------
        word : str
            検索したい単語
 
        Returns
        -------
        item : str or None
            検索結果
            見つからなかった場合はNone
        """
        node_index = 0
        entry = -1
 
        for c in word:
            char_num = self.__get_char_num(c)
            tmp_node = self.nodes[node_index]
            print('tmp_node', tmp_node)
            if entry == -1:
              entry = node_index
            
            node_index = tmp_node.children[char_num]
            if node_index == -1:
                return None
 
        return entry

trie = Trie()
for i in range(N):
  trie.insert('tfoo', 'tes')
print('foo', trie.query('foo'))
print('fo', trie.query('fo'))
# R = T[::-1]
# trie = Trie()
# for i in range(2 * N):
#   trie.insert(R, 'f')
# 
# print('trie', trie)
# for i in range(N):
#   s = T[:i + 1]
#   print('s', s)
#   print(trie.query(s))