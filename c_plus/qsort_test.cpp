#include<iostream>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if(arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return i + 1;
}

void qsort(int arr[], int low, int high) {
    if (low < high) {
        int p = partition(arr, low, high);
        qsort(arr, low, p - 1);
        qsort(arr, p + 1, high);
    }
}

void printArray(int a[]) {
    for (int i = 0; i < 5; i++) 
        printf("%d ", a[i]);
    printf("\n");
}

int main() {
    int arr[] = {5, 4, 3, 2, 1};
    qsort(arr, 0, 5 - 1);
    printArray(arr);
}