'''
기본 이진 트리 생성

- 노드 입력
- 부모 노드 보다 작은 숫자는 왼쪽, 큰 숫자는 오른쪽
- 잘못하면 한쪽에 노드가 몰리는 현상 발생

모양에 따른 분류

- 포화 이진 트리; 모든 부모 노드에 2개의 자식 노드
- 완전 이진 트리
- 편향 이진 트리

사용 및 응용

- 입력
- 검색
- 삭제

=> 연결 리스트

순회 알고리즘과 스택

- refs) 
  - 대멀쌤 Youtube:  이진탐색 트리 순회 알고리즘과 스택

- 전위 순회: root - left- right
  1. 루트에서 단말까지 왼쪽 경로 노드 방문하면서, 방문 노드 오른쪽 자식 있으면 push
  2. stack에서 pop(방문)하고, 방문한 노드를 루트로 하는 서브트리에 대해 1부터 반복, 스택 비어있으면 종료

- 중위 순회: left - root - right
  1. 루트에서 단말까지 왼쪽 경로 서브트리 루트 노드를 push
  2. 왼쪽 자식 없는 노드 만나면 pop(방문), 방문 노드 오른족 자식 있으면 push
  3. 1~2. 반복하다가 스택 비면 종료,

- 후위 순회: left - right - root
  1. 루트부터 왼쪽 경로 따라 push, 오른쪽 자식 있으면 먼저 push
  2. 스택에서 top을 pop(방문)하되 만약 top이 오른쪽 자식이면 pop하지말고 top을 루트로하는 서브트리에 대해 1~2반ㄴ복
  3. 스택 비면 종료
'''

