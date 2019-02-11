## Binary Search Tree

- binary search Tree는 root를 기준으로 작으면 왼쪽, 크면 오른쪽으로 배치된 Tree이다.

### description

```python
class Node:
    def __init__(self,key,value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinaryTree
    def __init__(self):
        self.root = None
        self.size = 0
    def get_size(self):
    def get_root(self):
    def insert(self,key,value=None):
    def delete(self,key)
    def _findmin(node)
    def print_preorder()
    def print_inorder()
    def print_postorder()
```



### contents

- insert

```python
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
                        temp.left = Node(key,value)
                        ## 여기 부분처럼 temp.left 이런식으로 설정을 해주어야 어디에 소속되었는지를 알 수 있음.
                        break
                    temp = temp.left
                else:
                    if temp.right ==None:
                        temp.right = Node(key,value)      ## 마찬가지
                        break
                    temp = temp.right
```

```
node에는 left, right가 존재하기에 위 노드와 연결해주는 것이 중요하다.
	node.left = Node(key)
	node.right = Node(key)
이런 방법으로 추가를 시켜주자.
```

- delete

```python
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
```

```python
가장 복잡한 delete 이다.

- 순서
1. 해당 노드를 찾을 때 까지 반복, 없다면 return False, 크기로 접근 가능
2. 찾았다면 case 4가지로 나누어서 처리

- case 4가지로 나누어서 진행한다.
1. 자식이 둘 다 존재
	오른쪽 자식중에 가장 작은 값
    왼족 자식중애 가장 큰 값
    둘 중 하나의 값이 대체된다.  
2. 자식이 오른쪽만
3. 자식이 왼쪽만
4. 자식이 둘다 없는 경우

- 예외
	진행하다보면 root를 제거해야 할 경우가 있는데 각 경우마다 root인지를 확인한 후 따로 구현하였다.

- 안쓰던 문법 중에
   'parents_l' in locals()
    '변수명' in globals()
    이렇게 두가지가 있다. 이것은 locals 또는 globals에 해당 이름의 변수가 있는지 확인 할 수 있다.
    
    
```



- inorder _ 왼 - root - 오

  ```python
  def print_inorder(self, temp = 'Imroot'):
          if temp == 'Imroot':            # 처음 들어올 때는 root, 인자 없이 들어오기 때문
              temp = self.root
          if temp == None:
              return True
          self.print_inorder(temp.left)
          print(temp.key, end=' ')
          self.print_inorder(temp.right)
  ```

- preoreder _ root  - 왼 - 오

  ```python
  def print_preorder(self, temp = 'Imroot'):
          if temp == 'Imroot':    # 처음 들어올 때는 root, 인자 없이 들어오기 때문
              temp = self.root
  
          if temp == None:
              return True
          print(temp.key, end = ' ')
          self.print_preorder(temp.left)
          self.print_preorder(temp.right)
  ```

- postorder _ 왼 - 오 - root

  ```python
  def print_postorder(self, temp = 'Imroot'):
          if temp == 'Imroot':
              temp = self.root
          if temp == None:
              return True
          self.print_postorder(temp.left)
          self.print_postorder(temp.right)
          print(temp.key, end=' ')
  ```
