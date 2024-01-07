---
title: "docs precision voltage shield"
slug: docs-precision-voltage-shield
author: Brandon Stafford
lastmod: 2014-05-13T12:56:48.000Z
date: 2014-03-06T18:37:57.000Z
source: rascalmicro.com
---
The Precision Voltage Shield is an 8-channel, 16-bit analog-to-digital converter that plugs on top of an [Arduino microcontroller][1]. It is similar to the analog input pins on the Arduino Uno, but with 64 times better resolution and 8 channels instead of 6.

### What could I use this for? ###

With an Arduino Uno, the Precision Voltage Shield can be used to make a simple, precise data acquisition system that sends data to a PC via the Arduino's USB port.

You could use the shield to:

* Measure 8 sensors at the same time, like 8 multimeters in one board
* Measure a few sensors and then make decisions based on the readings from the sensors
* Measure voltages of several batteries at once while keeping them electrically isolated from one another
* Using a resistive shunt, measure the current flowing through a circuit

### Technical details ###

The shield is based around the Analog Devices AD7606BSTZ data acquisition chip, which includes a successive approximation A/D converter, as well as input clamp protection and analog input filtering. The shield brings the AD7606's SPI interface out to pins 10-13 on its Arduino headers. The shield also provides additional chip select lines on pins 8, 9 and A3, and uses pins 2-5 for additional control signals. The remaining pins are not connected. The AD7606 also has a parallel interface, which the shield does not connect to.

### Shield settings ###

**Range**

The shield can accept two input ranges: &plusmn;5 V or &plusmn;10 V, depending on the location of the small black jumper labeled "Range." When the jumper bridges the two leftmost pins on the range header, the shield scales its 16 bits of resolution (65,536 readings) from -5 to 5 V, so the steps between readings are equivalent to 0.000153 V.

When the jumper is on the rightmost pins on the range header, the same 65,536 readings are spread across the range from -10 V to 10 V. In this case, the steps between readings are twice as big, or 0.000305 V.

No Arduino code modification is needed to switch ranges; the AD7606 chip reads the jumper and switches automatically.

**Chip select** (experimental)

If you want to use multiple Precision Voltage Shields stacked on one Arduino to get more than 8 channels, you can use the chip select lines to pick between them. The CSx pin pair that is jumpered routes the Arduino's SPI chip select signal to the AD7606's chip select input. When SPI signals are sent to multiple stacked shields at once, only the shield connected to the chip select line that is activated by the Arduino will respond.

The other shields will still be triggered to take measurements. There may be a problem in which the shields' output lines (the MISO, FRSTDATA, and BUSY pins) clash with each other, but this has not been tested.

**Oversampling**

As shipped, the Precision Voltage Shield oversamples by 64x. This means that when a set of 8 measurements is triggered, the shield performs 64 measurements very quickly and returns the average result. This helps filter out high-frequency noise, which is generally very desirable. The headers for modifying this are not included with the shield.

If you needed to sample so fast that the oversampling was slowing you down, you could cut the traces that hardwire the oversampling pins, and then solder headers into the provided holes to choose whatever oversampling rate you'd like. Keep in mind that the likely result is that in less than a second, you will gather more data than the Arduino can store. There are probably situations when this is worthwhile (maybe some kind of low-latency control system?), but they are very rare.

### Software ###

**The Precision Voltage Shield itself runs no software.** It does all of its signal conditioning, measurement, and communication in hardware.

I designed the shield to talk to an Arduino Uno. The code below, loaded on an Arduino Uno, will query all 8 channels of the shield once per second and print the results to the Arduino's USB port.

```language-c
#include <SPI.h>

#define SCALE_FACTOR 0.000152587890625

// 10/(2^16) = 0.000152587890625

#define BUSY 3
#define RESET 4
#define START_CONVERSION 5
#define CHIP_SELECT 10
#define MISO 12
#define LED 13
#define TOTAL_RAW_BYTES 16

int bytesToRead = TOTAL_RAW_BYTES;  
byte raw[TOTAL_RAW_BYTES];  
signed long parsed[8];

void setup() {  
  pinMode(BUSY, INPUT);
  pinMode(RESET, OUTPUT);
  pinMode(LED, OUTPUT);
  pinMode(START_CONVERSION, OUTPUT);
  pinMode(MISO, INPUT);

  Serial.begin(115200);
  SPI.begin();

  digitalWrite(START_CONVERSION, HIGH);  
  digitalWrite(CHIP_SELECT, HIGH);
  digitalWrite(RESET, HIGH);
  delay(1);
  digitalWrite(RESET, LOW);
}

void loop() {  
  int i;

  digitalWrite(START_CONVERSION, LOW);
  delayMicroseconds(10);
  digitalWrite(START_CONVERSION, HIGH);

  while (digitalRead(BUSY) == HIGH) {
    // wait for conversion to complete
  }
  digitalWrite(CHIP_SELECT, LOW);
  while (bytesToRead > 0) {
    raw[TOTAL_RAW_BYTES - bytesToRead] = SPI.transfer(0x00);
    bytesToRead--;
  }
  digitalWrite(CHIP_SELECT, HIGH);
  bytesToRead = TOTAL_RAW_BYTES;

  parseRawBytes();

  //Serial.write(raw, 16);

  for(i=0; i<8; i++) {
    Serial.print((float)parsed[i] * SCALE_FACTOR, 5);
    Serial.print(",");
  }
  Serial.print("\r\n");
  delay(1000);
}

void parseRawBytes() {
  parsed[0] = (raw[0] << 8) + raw[1];
  parsed[1] = (raw[2] << 8) + raw[3];
  parsed[2] = (raw[4] << 8) + raw[5];
  parsed[3] = (raw[6] << 8) + raw[7];
  parsed[4] = (raw[8] << 8) + raw[9];
  parsed[5] = (raw[10] << 8) + raw[11];
  parsed[6] = (raw[12] << 8) + raw[13];
  parsed[7] = (raw[14] << 8) + raw[15];
}
```

[1]: http://arduino.cc/