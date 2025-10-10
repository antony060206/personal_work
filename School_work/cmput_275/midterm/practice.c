// int main(){
//     int x = 10;
//     int *ptr = &x;
//     printf("%p\n",ptr);
//     printf("%d",*ptr);
//     return 0;
// }

int main() {
    int arr[] = {1, 2, 3, 4, 5};
     int *p = arr;
     printf("sizeof(arr): %lu\n", sizeof(arr));
     printf("sizeof(p): %lu\n", sizeof(p));
     printf("p: %p\n", p);
     printf("&p: %p\n", &p);
     printf("arr: %p\n", arr);
     printf("&arr: %p\n", &arr); // !!!
     }
    