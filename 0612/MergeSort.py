# 병합정렬 (Merge Sort)

class MergeSort:
    def main(self):
        num_list = []
        while True:
            try:
                input_num = int(input('정렬할 숫자 입력(입력종료=0): '))
            except ValueError:
                print('!!! 숫자만 입력하세요')
            else:
                if input_num == 0:
                    break
                num_list.append(input_num)
        self.merge_sort(num_list, 0, len(num_list) - 1)
        print(num_list)

    def merge_sort(self, A, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(A, left, mid)
            self.merge_sort(A, mid+1, right)
            self.merge(A, left, mid, right)

    def merge(self, A, left, mid, right):
        temp = [0] * len(A)
        k = left
        i = left
        j = mid + 1
        
        while i <= mid and j <= right:
            if A[i] <= A[j]:
                temp[k] = A[i]
                k, i = k+1, i+1
            else:
                temp[k] = A[j]
                k, j = k+1, j+1

        if i > mid:
            temp[k:k+right-j+1] = A[j:right+1]
        else:
            temp[k:k+mid-i+1] = A[i:mid+1]
        A[left:right+1] = temp[left:right+1]

if __name__ == '__main__':
    app = MergeSort()
    app.main()
