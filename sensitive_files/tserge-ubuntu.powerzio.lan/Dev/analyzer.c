#include <stdio.h>

int main(int argc, char **argv) {
  int controller_id = 0;
  printf("Logic controller %s : initializing", controller_id);
  int fd = open("/controller.pid");
  if (fd > 0) {
    //TODO connect to the controller and send information to the SCADA system
  } else {
    printf("Error: no controller is running on this host");
  }
  return 0;
}
