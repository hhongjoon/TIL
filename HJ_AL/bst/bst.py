import copy
class Node:
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class binaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    def get_size(self):
        return self.size
    def get_root(self):
        return self.root


    def insert1(self,key,value=None):
        #print(key)
        temp = self.root
        self.size += 1
        if self.root ==None:
            self.root = Node(key,value)
        elif self.root.key == key:
            self.root.value = value
        else:
            while temp != None:
                if temp.key > key:
                    if temp.left ==None:
                        temp.left = Node(key,value)        ## 여기 부분처럼 temp.left 이런식으로 설정을 해주어야 어디에 소속되었는지를 알 수 있음.
                        break
                    temp = temp.left
                else:
                    if temp.right ==None:
                        temp.right = Node(key,value)      ## 마찬가지
                        break
                    temp = temp.right


    def _findmin(self,temp):
        temp = temp.right
        if temp.left != None:
            while temp != None:
                temp = temp.left
                if temp.left == None :
                    return temp
        return temp


    def delete(self,key):
        #search_by_key 우선
        temp = self.root
        while temp != None:

            if temp.key == key:
                self.size -= 1

                if temp.left == None and temp.right == None :    # 1 딸린 자식 노드가 없을 때 -> 바로 삭제
                    if temp == self.root:
                        self.root = None
                        return True

                    #어느쪽에서 왔는지
                    if 'parents_l' in locals() and parents_l.left == temp:
                        parents_l.left = None
                        return True
                    if 'parents_r' in locals() and parents_r.right == temp:
                        parents_r.right = None
                        return True
                elif temp.left != None and temp.right == None:   # 2 왼쪽 자식만 있을 때 연결 후 삭제(연결만 해주면 가능)
                    if temp == self.root:
                        self.root = temp.left
                        return True

                    if 'parents_l' in locals() and parents_l.left == temp:
                        parents_l.left = temp.left
                        return True
                    if 'parents_r' in locals() and parents_r.right == temp:
                        parents_r.right = temp.left
                        return True

                elif temp.left == None and temp.right != None:  # 3 오른쪽 자식, (부모에 연결만 해줄 것)
                    if temp == self.root:
                        self.root = temp.right
                        return True

                    if 'parents_l' in locals() and parents_l.left == temp:
                        parents_l.left = temp.right
                        return True
                    if 'parents_r' in locals() and parents_r.right == temp:
                        parents_r.right = temp.right
                        return True

                else:                                       # 4 왼, 오 존재 할 때 오른쪽 의 가장 최소값으로 대체한다.
                    target = self._findmin(temp)
                    self.delete(target.key)
                    self.size += 1              ### target 찾고서 재귀 돌 때 size가 작아지니 + 1 해준다.

                    if temp == self.root:
                        target.left = temp.left
                        target.right = temp.right
                        self.root = target
                        return True

                    if 'parents_l' in locals() and parents_l.left == temp:
                        parents_l.left = target
                        target.left = temp.left
                        target.right = temp.right
                        return True
                    if 'parents_r' in locals() and parents_r.right == temp:
                        parents_r.right = target
                        target.left = temp.left
                        target.right = temp.right
                        return True


            elif temp.key > key:
                if temp.left == None:
                    return False
                parents_l, temp = temp, temp.left        ## 자식이 부모보다 어디에 있는지 기준
            else:
                if temp.right == None:
                    return False
                parents_r, temp = temp, temp.right


    def search_by_key(self,key):
        pass

    def print_preorder(self, temp = 'Imroot'):
        if temp == 'Imroot':
            temp = self.root

        if temp == None:
            return True
        print(temp.key, end = ' ')
        self.print_preorder(temp.left)
        self.print_preorder(temp.right)

    def print_inorder(self, temp = 'Imroot'):
        if temp == 'Imroot':
            temp = self.root
        if temp == None:
            return True
        self.print_inorder(temp.left)
        print(temp.key, end=' ')
        self.print_inorder(temp.right)

    def print_postorder(self, temp = 'Imroot'):
        if temp == 'Imroot':
            temp = self.root
        if temp == None:
            return True
        self.print_postorder(temp.left)
        self.print_postorder(temp.right)
        print(temp.key, end=' ')


def is_bst(root):
    isit = True
    queue = list()
    queue.append(root)
    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node.left is not None:
            queue.append(current_node.left)
            if current_node.key < current_node.left.key:
                isit = False
        if current_node.right is not None:
            queue.append(current_node.right)
            if current_node.key > current_node.right.key:
                isit = False

    return isit


def main():
    key_list = [
        (90, '이상해씨'),
        (50, '이상해풀'),
        (150, '이상해꽃'),
        (20, '파이리'),
        (75, '리자드'),
        (95, '리자몽'),
        (175, '꼬부기'),
        (5, '어니부기'),
        (25, '거북왕'),
        (66, '캐터피'),
        (80, '단데기'),
        (92, '버터플'),
        (111, '뿔충이'),
        (166, '딱충이'),
        (200, '독침붕')
    ]
    bst = binaryTree()
    for key, value in key_list:
        bst.insert1(key, value)
    # self.assertTrue(is_bst(bst.get_root()))
    bst.print_preorder()
    print('끝')
    for key, value in key_list:
        print(key, 'in')

        bst.print_preorder()
        print('끝')
        temp_bst = copy.deepcopy(bst)
        temp_bst.delete(key)
        temp_bst.print_preorder()
        print('제거 후')
        # self.assertTrue(is_bst(bst.get_root()))

    pass


if __name__ == '__main__':
    main()