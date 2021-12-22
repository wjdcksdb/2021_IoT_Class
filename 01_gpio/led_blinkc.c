#include <wiringPi.h>
#define LED 7

int main(void){
	wiringPiSetupGpio();
	pinMode(LED, OUTPUT);
	for (int i=0; i<10; i++){
		digitalWrite(LED,HIGH); delay(1000);
		digitalWrite(LED,LOW);
	}
	return 0;
}