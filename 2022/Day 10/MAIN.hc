Cd(__DIR__);
#include "E:/AoC/HELPER.HC"

Bool isNOOP(SV *sv) {
  U8 *str = getString("%c",sv->begin[0]); 
  return str[0] == 'n';
}


U0 part1() {
  I64 signalstrengths = 0;
  I64 curX = 1;
  I64 curTime = 1;
  I64 add = 0;
  I64 outputCounter = 1;

  SV sv;
  SV word;
  sv.begin = FileRead("E:/AoC/inputday10.txt", &sv.size);
  U8 *saved_begin = sv.begin;
 
  while(sv.size > 1) {
      SVChopWord(&sv, &word);
      SVChopLeft(&sv);
      if(isNOOP(&word)) {
          if((curTime+20)%40 == 0) {
              signalstrengths += (curX * curTime);
          }
	  if(-1 <= (((curTime-1)%40)-curX) <= 1) {
		"#";
	  } else {
  	 	".";
	  }
	  if(outputCounter == 40) {
		"\n";
		outputCounter = 0;
	  }
	  outputCounter += 1;
          curTime += 1;
      } 
      else {
          add = SVChopI64(&sv);
	  SVChopLeft(&sv);
          if((curTime+20)%40 == 0) {
              signalstrengths += (curX * curTime);
          }
	  if(-1 <= (((curTime-1)%40)-curX) <= 1) {
		"#";
	  } else {
  	 	".";
	  }
	  if(outputCounter == 40) {
		"\n";
		outputCounter = 0;
	  }
	  outputCounter += 1;
          curTime += 1;
          if((curTime+20)%40 == 0) {
              signalstrengths += (curX * curTime);
          }
	  if(-1 <= (((curTime-1)%40)-curX) <= 1) {
		"#";
	  } else {
  	 	".";
	  }
	  if(outputCounter == 40) {
		"\n";
		outputCounter = 0;
	  }
	  outputCounter += 1;
          curTime += 1;
          curX += add;
      }

  }

  Free(saved_begin);

  "\nPart 1: %d\n", signalstrengths;
}
part1;