#include <stdio.h>

int main() {

  int id = 1;
  printf("id is %d\n", id);
  id -= '0' + 0x0;
  printf("id is %d == %x\n", id, id);
  return 0;
}
