class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.fail_link = None
        self.isEnd = False

class Aho_Chorasick():
    def __init__(self, pattern_array):
        self.root = Node(None)
        for pattern in pattern_array:
            self.insert(pattern)

    def insert(self, string):
        current_node = self.root
        self.root.data = ""

        for ch in string:
            tmp = current_node.data
            if ch not in current_node.children:
                current_node.children[ch] = Node(ch)
            current_node = current_node.children[ch]
            current_node.data = tmp+ch

        current_node.data = string
        current_node.isEnd = True

    def gen_fail_function(self):
        self.root.fail_link = self.root

        queue = []
        queue.append(self.root)
        while not (len(queue) == 0):
            parent = queue.pop(0)
            for child in parent.children.values():
                
                if(parent == self.root):
                    child.fail_link = self.root
                else:
                    node = parent.fail_link
                    while(node != self.root and child.key not in node.children):
                        node = node.fail_link
                    if (child.key in node.children):
                        child.fail_link = node.children[child.key]
                    else:
                        child.fail_link = self.root
                
                # if(child.fail_link.isEnd == True):
                #     child.isEnd = True
                print(child.data, child.fail_link.data)
                queue.append(child)
        
        
                        

                    

    def search(self, given_string):
        answer = []
        node = self.root
        for idx, c in enumerate(given_string):
            while(node != self.root and c not in node.children):
                node = node.fail_link

            if(c in node.children):
                node = node.children[c]
            # if(node.isEnd == True):
            #     answer.append((node.data, idx))
            search_node = node
            
            while(search_node != self.root):
                if(search_node.isEnd == True):
                    answer.append((search_node.data, idx))
                search_node = search_node.fail_link

        return answer


if __name__ == "__main__":
    test_word = ["cache", "he", "chef", "achy"]
    aho = Aho_Chorasick(test_word)
    aho.gen_fail_function()
    search_text = "cacachefcachy"
    answer = aho.search(search_text)
    print(answer)
