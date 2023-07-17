#include<stdio.h>
#include<math.h>
#include<iostream>
#include<time.h>

using namespace std;

int main() {
	
	//가로와 세로 길이를 입력 받는다.
	long double w = 0,h = 0;
	scanf("%lf %lf", &w, &h);
	//inc는 기울기입니다. 다음 x 좌표의 y 값을 구하기 위해서 사용합니다.
	long double inc = h/w;

	long double beforeY = 0, currentY = 0;// 현재 Y좌표와 이전 Y좌표(정확히는 이전 y 좌표아님)를 저장할 변수를 선언합니다.
	long double block = 0;// 사용할 수 없는 칸의 갯수를 저장할 변수 block을 선언합니다.
	int ySize = 0;// 단위 블럭의 크기를 저장할 변수입니다. (사용할 수 없는 칸들은 규칙적으로 생성되고, 앞서 말한 단위 블럭이란 반복되는 칸들의 set 1 개를 의미합니다)

	// 시간을 측정할 변수들을 선언합니다.
	clock_t start, finish;
	long double duration;
	start = clock();

	// x의 좌표를 한 칸씩 옮기면서 y 값이 정수인지 아닌지 확인을 합니다.
	// y의 값이 정수라면
	// 단위 블록이 완성되었음을 의미합니다. 차후에도 단위 블록이 계속 반복 될 것입니다.
	// y의 값이 실수라면
	// 단위 블록이 아직 완성되지 않았음을 의미합니다. 그러므로 현재 x 좌표의 빈 블럭의 갯수를 세서 block에 더합니다.
	for (int x = 1; x < w+1; x++) {
		// 현재 x 좌표의 y 값을 구하기 위해 이전 currentY 값에 계속 기울기를 곱합니다.
		// x의 값이 1씩 증가하기 때문에 기울기만 곱하면 됩니다.
		currentY += inc;
		
		// 현재 y 좌표가 정수인지 실수 인지 구분을 합니다.
		if ((currentY - int(currentY)) == 0) {
			// 현재 y 좌표가 정수인 경우 
			// block에 현재 x ~ x+1 사이 한 칸에 빈 블럭들을 더합니다.
			// 앞서 말했다시피 x의 값은 1씩 증가하므로, 현재 Y의 값에서 이전 Y의 값을 빼면 현재 X 좌표의 빈 공간이 몇개인지 알 수 있습니다.
			block += currentY - beforeY;
			// 현재 y 좌표는 단위 블록의 높이와 같습니다.
			// 그러므로 ySize에 값을 저장합니다.
			ySize = int(currentY);
			// 단위 블록을 구했으므로 반복을 멈춥니다.
			break;
		}
		else {
			// 현재 y 좌표가 실수인 경우
			// 실수인 경우
			// 현재 좌표의 빈 공간 높이가 1일수도 있기 때문에, currentY를 올림하고, 이전 y 좌표를 뺌으로서 현재 x 좌표의 빈 공간을 구한다.
			// beforeY의 경우, 정확히는 이전 Y 좌표가 아니다
			// 단위 블록을 쪼개 보면 각 좌표마다 빈 공간들의 높이가 조금씩 겹쳐있다. 겹쳐있지 않을 경우 Y의 값이 정수이므로 단위블록이 이미 완성된 상태이다.
			// 즉 겹쳐 있는 블럭의 내림 값은 다음 X 좌표에서 빈 블럭의 y 시작 좌표가 된다.
			// beforeY에 겹쳐 있는 영역의 내림 값을 저장함으로 다음 좌표의 빈공간을 구할 수 있다
			// 또한 다음 y 좌표에서 beforeY 아래 값들은  사용할 수 있는 블록들을 명시한다.
			block +=  ceil(currentY) - beforeY;
			beforeY = floor(currentY);
		}
	}
	// 출력
	// 실행 시간과 결과 값을 출력합니다.
	finish = clock();
	duration = (double)(finish - start) / CLOCKS_PER_SEC;
	// 연산들을 주로 실수로 진행을 했지만, 사용할 수 있는 블록의 갯수는 정수이기에 정수 연산으로 치환합니다
	// 전체 블록의 수(w*h) - h 안에 들어갈 수 있는 블록의 갯수(h/ySize) * 단위 블록의 갯수(block)는 사용할 수 있는 블록의 갯수입니다.
	cout << int(w * h)-int(h/ySize)*int(block) << endl;
	cout << "실행시간: " << duration << "초" << endl;
}


5 8 8 10 ?
2 5 4 5 5 5 